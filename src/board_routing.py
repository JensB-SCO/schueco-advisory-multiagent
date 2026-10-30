from __future__ import annotations

import re

from src.task_context import TaskContext


ROLE_ALIASES = {
    "board chair": "chairman", "chairman": "chairman",
    "strategy": "strategy", "cfo": "cfo", "financial": "cfo",
    "marketing": "marketing", "executive communication": "executive_communication",
    "research": "research_evidence", "evidence": "research_evidence",
    "coremedia": "coremedia", "architecture": "architecture",
    "engineering": "engineering", "operations": "operations", "sre": "operations",
    "security": "security", "information security": "security",
    "seo": "seo", "geo": "geo", "analytics": "analytics",
    "leadmanagement": "leadmanagement", "sales": "sales",
    "ux": "ux", "design": "design", "frontend": "frontend",
    "backend": "backend_api", "compliance": "compliance",
}

TECHNICAL = {"coremedia", "architecture", "backend_api", "frontend", "engineering", "security", "operations"}
MANAGEMENT = {"cfo", "executive_communication", "research_evidence", "strategy"}


def select_roles(context: TaskContext, available: set[str], task: str = "") -> list[str]:
    """Choose a small board from the question and explicit task roles."""
    task_scope = re.split(r"^##?\s+(?:Erwartete Ergebnisstruktur|Deliverables|Finale Präsentation)", task, maxsplit=1, flags=re.MULTILINE | re.IGNORECASE)[0]
    signal = " ".join((context.title, context.management_question, context.mission, context.goal, task_scope)).lower()
    roles = {"strategy", "research_evidence"}
    if context.is_management_assessment or re.search(r"budget|kosten|wirtschaft|make.or.buy|invest|management", signal):
        roles.update(MANAGEMENT)
    if re.search(r"marke|marketing|kampagne|zielgruppe|website|content", signal):
        roles.add("marketing")
    if re.search(r"coremedia|cms", signal):
        roles.add("coremedia")
    if re.search(r"entwickl|implement|software|api|integration|technisch", signal):
        roles.update({"architecture", "engineering"})
    if re.search(r"betrieb|operations|incident|deployment|release", signal):
        roles.add("operations")
    if re.search(r"seo|suche|suchmaschine", signal):
        roles.add("seo")
    if re.search(r"\bgeo\b|generative engine", signal):
        roles.add("geo")
    if re.search(r"lead|crm|hubspot", signal):
        roles.add("leadmanagement")
    if re.search(r"analytics|tracking|messbar", signal):
        roles.add("analytics")
    if re.search(r"\bux\b|nutzerfuehrung|nutzerführung|bedien", signal):
        roles.add("ux")
    if re.search(r"\bapi\b|schnittstelle|datenbank", signal):
        roles.add("backend_api")
    if re.search(r"frontend|react|web.komponente", signal):
        roles.add("frontend")
    if re.search(r"security|datenschutz|berechtigung", signal):
        roles.add("security")
    for requested in context.requested_roles:
        normalized = requested.lower().replace("&", " und ")
        for phrase, role in ROLE_ALIASES.items():
            if re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", normalized):
                roles.add(role)
    return sorted((roles & available) - {"chairman"})


def select_skills(context: TaskContext, roles: list[str]) -> list[str]:
    skills = ["management-decision/Skill.md"] if context.is_management_assessment else []
    if {"engineering", "backend_api", "frontend"} & set(roles):
        skills.append("cloud-agent-service-engineer/Skill.md")
    return skills
