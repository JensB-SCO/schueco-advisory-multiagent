from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re


@dataclass(frozen=True)
class TaskContext:
    source_path: str
    title: str
    task_type: str
    mission: str = ""
    management_question: str = ""
    thesis: str = ""
    goal: str = ""
    project_brief_path: str = ""
    process_gates: list[str] = field(default_factory=list)
    requested_roles: list[str] = field(default_factory=list)
    scoring_dimensions: list[str] = field(default_factory=list)
    evaluation_criteria: list[str] = field(default_factory=list)
    deliverables: list[str] = field(default_factory=list)
    final_output: str = ""

    @property
    def is_management_assessment(self) -> bool:
        return self.task_type in {
            "management_assessment",
            "strategic_assessment",
            "board_review",
        }

    @property
    def display_name(self) -> str:
        return self.management_question or self.title or "Anforderungsbewertung"

    def to_prompt_block(self) -> str:
        lines = [
            "# TaskContext",
            f"- Quelle: {self.source_path}",
            f"- Task-Typ: {self.task_type}",
            f"- Titel: {self.title or 'Nicht angegeben'}",
        ]
        optional_items = (
            ("Mission", self.mission),
            ("Managementfrage", self.management_question),
            ("These", self.thesis),
            ("Ziel", self.goal),
            ("Projektauftrag-Referenz", self.project_brief_path),
            ("Finales Ergebnis", self.final_output),
        )
        for label, value in optional_items:
            if value:
                lines.append(f"- {label}: {value}")
        for label, values in (
            ("Prozess-Gates", self.process_gates),
            ("Rollen laut Task", self.requested_roles),
            ("Bewertungsdimensionen", self.scoring_dimensions),
            ("Bewertungskriterien", self.evaluation_criteria),
            ("Erwartete Deliverables", self.deliverables),
        ):
            if values:
                lines.append(f"- {label}: {', '.join(values)}")
        return "\n".join(lines)


def parse_task_context(task: str, source_path: str | Path = "") -> TaskContext:
    source = str(source_path)
    project_name = _single_line_directive(task, "PROJEKTNAME")
    title = (
        _first_heading(task)
        or project_name
        or Path(source).stem.replace("_", " ").replace("-", " ")
    )
    project_brief_path = _single_line_directive(task, "PROJEKTAUFTRAG")
    management_question = _management_question(task)
    thesis = _quoted_after_label(task, "These lautet") or _section_summary(task, "These")
    mission = _section_summary(task, "Mission")
    goal = _section_summary(task, "Ziel")
    final_output = _section_summary(task, "Finale Praesentation") or _section_summary(
        task, "Finale Präsentation"
    )
    task_type = _detect_task_type(
        task=task,
        title=title,
        project_brief_path=project_brief_path,
        management_question=management_question,
        deliverables=_subheadings_in_section(task, "Deliverables"),
    )
    return TaskContext(
        source_path=source,
        title=title,
        task_type=task_type,
        mission=mission,
        management_question=management_question,
        thesis=thesis,
        goal=goal,
        project_brief_path=project_brief_path,
        process_gates=_gate_headings(task),
        requested_roles=_subheadings_in_section(task, "Rollen des Advisory Boards"),
        scoring_dimensions=_subheadings_in_section(task, "Bewertungsrahmen"),
        evaluation_criteria=_subheadings_in_section(task, "Bewertungskriterien"),
        deliverables=_subheadings_in_section(task, "Deliverables"),
        final_output=final_output,
    )


def _detect_task_type(
    task: str,
    title: str,
    project_brief_path: str,
    management_question: str,
    deliverables: list[str],
) -> str:
    lower = f"{title}\n{task}".lower()
    if project_brief_path:
        return "project_brief_review"
    if management_question:
        if "strategische bewertung" in lower or "managemententscheidung" in lower:
            return "strategic_assessment"
        return "management_assessment"
    if "review" in lower or "gremienreview" in lower:
        return "board_review"
    if "powerpoint" in lower or "präsentation" in lower or "praesentation" in lower:
        return "presentation_request"
    if deliverables:
        return "deliverable_request"
    return "general_task"


def _first_heading(task: str) -> str:
    headings = re.findall(r"^\s{0,3}#{1,2}\s+(.+?)\s*$", task, flags=re.MULTILINE)
    for heading in headings:
        clean = _clean_inline(heading)
        lower = clean.lower()
        if clean and "digital advisory board" not in lower:
            return clean
    return _clean_inline(headings[0]) if headings else ""


def _single_line_directive(task: str, label: str) -> str:
    match = re.search(rf"^{re.escape(label)}:\s*(.+?)\s*$", task, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def _management_question(task: str) -> str:
    section = _section_text(task, "Ausgangsfrage")
    quote = re.search(r">\s*\*\*(.+?)\*\*", section or task, flags=re.DOTALL)
    if quote:
        return _clean_inline(quote.group(1))
    if section:
        lines = [
            _clean_inline(line)
            for line in section.splitlines()
            if _clean_inline(line) and not line.strip().startswith("---")
        ]
        return lines[0] if lines else ""
    return ""


def _quoted_after_label(task: str, label: str) -> str:
    pattern = rf"{re.escape(label)}.*?>\s*\*\*(.+?)\*\*"
    match = re.search(pattern, task, flags=re.DOTALL | re.IGNORECASE)
    return _clean_inline(match.group(1)) if match else ""


def _section_summary(task: str, heading: str, max_chars: int = 700) -> str:
    text = _section_text(task, heading)
    if not text:
        return ""
    lines = []
    for line in text.splitlines():
        clean = _clean_inline(line)
        if clean and clean != "---":
            lines.append(clean)
    summary = " ".join(lines)
    return summary[:max_chars].rstrip()


def _section_text(task: str, heading: str) -> str:
    pattern = rf"^\s{{0,3}}(#{{1,6}})\s+{re.escape(heading)}\s*$"
    match = re.search(pattern, task, flags=re.MULTILINE | re.IGNORECASE)
    if not match:
        return ""
    current_level = len(match.group(1))
    start = match.end()
    end = len(task)
    for next_heading in re.finditer(r"^\s{0,3}(#{1,6})\s+", task[start:], flags=re.MULTILINE):
        if len(next_heading.group(1)) <= current_level:
            end = start + next_heading.start()
            break
    return task[start:end].strip()


def _subheadings_in_section(task: str, heading: str) -> list[str]:
    section = _section_text(task, heading)
    if not section:
        return []
    values = []
    for match in re.finditer(r"^\s{0,3}#{2,6}\s+(.+?)\s*$", section, flags=re.MULTILINE):
        value = _clean_inline(match.group(1))
        if value and not value.lower().startswith("gate "):
            values.append(value)
    return _dedupe(values)


def _gate_headings(task: str) -> list[str]:
    values = re.findall(r"^\s{0,3}#\s+Gate\s+\d+\s*[-–]\s*(.+?)\s*$", task, flags=re.MULTILINE)
    return _dedupe(_clean_inline(value) for value in values)


def _clean_inline(text: str) -> str:
    clean = re.sub(r"[*_`]+", "", text)
    clean = re.sub(r"\s+", " ", clean)
    return clean.strip(" #>-:")


def _dedupe(values) -> list[str]:
    seen = set()
    result = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result
