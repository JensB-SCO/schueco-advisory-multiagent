from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GateResult:
    status: str
    missing: list[str]

    def to_markdown(self) -> str:
        missing_text = "\n".join(f"- {item}" for item in self.missing) if self.missing else "- Keine"
        return f"""# Advisory Board Gate Ergebnis

Status: **{self.status}**

Fehlende Bestandteile:
{missing_text}
"""


class AnalyticsGate:
    required_sections = {
        "Executive Summary": ["executive summary"],
        "Expertenbewertungen": ["expertenbewertungen"],
        "Zielkonflikte": ["zielkonflikte"],
        "Loesungsoptionen": ["loesungsoptionen", "lösungsoptionen"],
        "MVP": ["mvp"],
        "Roadmap": ["roadmap"],
        "CoreMedia-Anforderungen": ["coremedia"],
        "SEO-/GEO-Anforderungen": ["seo", "geo"],
        "Leadmanagement-Auswirkungen": ["leadmanagement", "lead management", "hubspot"],
        "Analytics Gate": ["analytics gate"],
        "Risiken": ["risiken"],
        "Entscheidungsempfehlung": ["entscheidungsempfehlung"],
    }

    required_terms = {
        "KPIs": ["kpi", "kennzahl", "erfolgsmetrik"],
        "Tracking": ["tracking", "event", "data layer"],
        "Dashboard": ["dashboard", "reporting"],
        "Monitoring": ["monitoring", "alert", "warnschwelle"],
        "Datenqualitaet": ["datenqualitaet", "datenqualität", "data quality", "consent"],
        "Architecture Gate": ["architecture gate", "architektur", "datenfluss", "integration"],
        "Engineering Gate": ["engineering gate", "test", "dokumentation", "readme"],
        "Security Gate": ["security gate", "security", "datenschutz", "secret"],
        "Operations Gate": ["operations gate", "betrieb", "rollback", "health"],
    }

    def validate(self, text: str, active_roles: set[str] | None = None) -> GateResult:
        lower = text.lower()
        missing: list[str] = []
        for label, terms in self.required_sections.items():
            if not any(term in lower for term in terms):
                missing.append(f"Pflichtabschnitt: {label}")
        role_for_gate = {
            "Architecture Gate": "architecture", "Engineering Gate": "engineering",
            "Security Gate": "security", "Operations Gate": "operations",
        }
        for label, terms in self.required_terms.items():
            if active_roles is not None and label in role_for_gate and role_for_gate[label] not in active_roles:
                continue
            if active_roles is not None and label in {"Tracking", "Dashboard", "Monitoring", "Datenqualitaet"} and "analytics" not in active_roles:
                continue
            if not any(term in lower for term in terms):
                missing.append(label)
        if missing:
            return GateResult(status="FAILED", missing=missing)
        return GateResult(status="PASSED", missing=[])
