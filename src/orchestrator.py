from __future__ import annotations

from pathlib import Path
import re

from openai import OpenAI

from src.agent import ExpertAgent
from src.analytics_gate import AnalyticsGate
from src.io_utils import build_task_output_dir, read_markdown_file, read_markdown_folder, write_output
from src.offline_fallback import (
    build_offline_recommendation,
    build_offline_review,
    is_insufficient_quota_error,
)
from src.task_context import parse_task_context


class AdvisoryBoardOrchestrator:
    def __init__(
        self,
        client: OpenAI | None,
        model: str,
        agents_dir: str = "agents",
        knowledge_dir: str = "knowledge",
        governance_dirs: tuple[str, ...] = ("board", "gates", "prompts", "standards"),
    ) -> None:
        self.client = client
        self.model = model
        self.agents_dir = Path(agents_dir)
        self.knowledge_dir = Path(knowledge_dir)
        self.governance_dirs = tuple(Path(path) for path in governance_dirs)

    def load_agents(self) -> list[ExpertAgent]:
        agents: list[ExpertAgent] = []
        for path in sorted(self.agents_dir.glob("*.md")):
            if path.name == "chairman.md":
                continue
            agents.append(
                ExpertAgent(
                    name=path.stem,
                    instructions=path.read_text(encoding="utf-8"),
                    client=self.client,
                    model=self.model,
                )
            )
        return agents

    def load_governance(self) -> str:
        return "\n\n".join(read_markdown_folder(path) for path in self.governance_dirs)

    def load_task(self, task_path: str) -> str:
        task = read_markdown_file(task_path)
        match = re.search(r"^PROJEKTAUFTRAG:\s*(.+?)\s*$", task, flags=re.MULTILINE)
        if not match:
            return task

        referenced_path = Path(match.group(1).strip())
        if not referenced_path.is_absolute():
            referenced_path = Path(task_path).parent / referenced_path

        project_brief = read_markdown_file(referenced_path)
        return (
            f"{task}\n\n"
            "## Geladener Projektauftrag\n\n"
            "BEGINN PROJEKTAUFTRAG\n\n"
            f"{project_brief}\n\n"
            "ENDE PROJEKTAUFTRAG\n"
        )

    def run(self, task_path: str) -> str:
        task = self.load_task(task_path)
        task_context = parse_task_context(task, task_path)
        task_context_block = task_context.to_prompt_block()
        knowledge = read_markdown_folder(self.knowledge_dir)
        governance = self.load_governance()
        task_output_dir = build_task_output_dir(task_path)
        reviews_output_dir = task_output_dir / "reviews"
        recommendation_output_dir = task_output_dir / "recommendation"
        reviews: list[str] = []
        offline_mode = self.client is None

        if offline_mode:
            print(
                "INFO: Kein OpenAI-API-Client verfuegbar. "
                "Der Runner startet im lokalen Offline-Fallback."
            )

        for agent in self.load_agents():
            print(f"Starte Agent: {agent.name}")
            if offline_mode:
                review = build_offline_review(agent.name, task)
            else:
                try:
                    review = agent.review(
                        task=f"{task_context_block}\n\n# Vollstaendiger Task\n\n{task}",
                        knowledge=f"{knowledge}\n\n{governance}",
                    )
                except Exception as error:
                    if not is_insufficient_quota_error(error):
                        raise
                    offline_mode = True
                    print(
                        "WARNUNG: Das OpenAI-API-Kontingent ist erschoepft "
                        "(insufficient_quota). Der Runner wird im lokalen "
                        "Offline-Fallback fortgesetzt."
                    )
                    review = build_offline_review(agent.name, task)
            review_md = f"# Expertenreview: {agent.name}\n\n{review}"
            reviews.append(review_md)
            write_output(reviews_output_dir, f"review-{agent.name}", review_md)

        chairman_instructions = read_markdown_file(self.agents_dir / "chairman.md")
        combined_reviews = "\n\n---\n\n".join(reviews)

        final_prompt = f"""
Aufgabe:
{task}

Erkannter TaskContext:
{task_context_block}

Wissensbasis:
{knowledge}

Governance, Gates und Standards:
{governance}

Expertenbewertungen:
{combined_reviews}

Erstelle die finale Empfehlung des Schueco Digital Advisory Boards 4.0.
Wichtig: Die Empfehlung muss die 12 Pflichtabschnitte aus der Charter enthalten.
Wichtig: Richte Struktur, Tonalitaet und Bewertung primaer am TaskContext aus. Wenn der Task eine Managementfrage oder Anforderungsbewertung ist, bewerte die gestellte Frage und schreibe keinen Projektauftrag.
Wichtig: Die Empfehlung muss bei Managementvorlagen, Budgetentscheidungen oder strategischen Empfehlungen das Financial Gate, Evidence Gate und Executive Communication Gate enthalten.
Wichtig: Die Empfehlung muss das Marketing Gate bei oeffentlichen, vertrieblichen oder kampagnennahen Initiativen sowie das Analytics Gate, Architecture Gate, Engineering Gate, Security Gate und Operations Gate vollstaendig enthalten.
"""
        if offline_mode:
            recommendation = build_offline_recommendation(task, reviews)
        else:
            try:
                response = self.client.responses.create(
                    model=self.model,
                    instructions=chairman_instructions,
                    input=final_prompt,
                )
                recommendation = response.output_text
            except Exception as error:
                if not is_insufficient_quota_error(error):
                    raise
                print(
                    "WARNUNG: Das OpenAI-API-Kontingent ist beim Chairman "
                    "erschoepft. Die finale Empfehlung wird lokal erzeugt."
                )
                recommendation = build_offline_recommendation(task, reviews)

        gate_result = AnalyticsGate().validate(recommendation)
        final_text = recommendation + "\n\n---\n\n" + gate_result.to_markdown()
        out_path = write_output(recommendation_output_dir, Path(task_path).stem, final_text)
        print(f"Finale Empfehlung geschrieben: {out_path}")
        return final_text
