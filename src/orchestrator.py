from __future__ import annotations
from pathlib import Path
from openai import OpenAI
from src.agent import ExpertAgent
from src.analytics_gate import AnalyticsGate
from src.io_utils import read_markdown_file, read_markdown_folder, write_output

class AdvisoryBoardOrchestrator:
    def __init__(self, client: OpenAI, model: str, agents_dir: str = "agents", knowledge_dir: str = "knowledge") -> None:
        self.client = client
        self.model = model
        self.agents_dir = Path(agents_dir)
        self.knowledge_dir = Path(knowledge_dir)

    def load_agents(self) -> list[ExpertAgent]:
        agents: list[ExpertAgent] = []
        for path in sorted(self.agents_dir.glob("*.md")):
            if path.name == "chairman.md":
                continue
            agents.append(ExpertAgent(
                name=path.stem,
                instructions=path.read_text(encoding="utf-8"),
                client=self.client,
                model=self.model,
            ))
        return agents

    def run(self, task_path: str) -> str:
        task = read_markdown_file(task_path)
        knowledge = read_markdown_folder(self.knowledge_dir)
        reviews: list[str] = []

        for agent in self.load_agents():
            print(f"Starte Agent: {agent.name}")
            review = agent.review(task=task, knowledge=knowledge)
            review_md = f"# Expertenreview: {agent.name}\n\n{review}"
            reviews.append(review_md)
            write_output("outputs/reviews", f"review-{agent.name}", review_md)

        chairman_instructions = read_markdown_file(self.agents_dir / "chairman.md")
        combined_reviews = "\n\n---\n\n".join(reviews)

        final_prompt = f"""
Aufgabe:
{task}

Wissensbasis:
{knowledge}

Expertenbewertungen:
{combined_reviews}

Erstelle die finale Empfehlung des Schüco Digital Advisory Boards.
Wichtig: Die Empfehlung muss das Analytics Gate vollständig enthalten.
"""
        response = self.client.responses.create(
            model=self.model,
            instructions=chairman_instructions,
            input=final_prompt,
        )
        recommendation = response.output_text

        gate_result = AnalyticsGate().validate(recommendation)
        final_text = recommendation + "\n\n---\n\n" + gate_result.to_markdown()
        out_path = write_output("outputs/recommendations", Path(task_path).stem, final_text)
        print(f"Finale Empfehlung geschrieben: {out_path}")
        return final_text
