from __future__ import annotations
from dataclasses import dataclass

@dataclass
class GateResult:
    status: str
    missing: list[str]

    def to_markdown(self) -> str:
        missing_text = "\n".join(f"- {item}" for item in self.missing) if self.missing else "- Keine"
        return f"""# Analytics Gate Ergebnis

Status: **{self.status}**

Fehlende Bestandteile:
{missing_text}
"""

class AnalyticsGate:
    required_terms = {
        "KPIs": ["kpi", "kennzahl", "erfolgsmetrik"],
        "Tracking": ["tracking", "event", "data layer"],
        "Dashboard": ["dashboard", "reporting"],
        "Monitoring": ["monitoring", "alert", "warnschwelle"],
        "Datenqualität": ["datenqualität", "data quality", "consent"],
    }

    def validate(self, text: str) -> GateResult:
        lower = text.lower()
        missing: list[str] = []
        for label, terms in self.required_terms.items():
            if not any(term in lower for term in terms):
                missing.append(label)
        if missing:
            return GateResult(status="FAILED", missing=missing)
        return GateResult(status="PASSED", missing=[])
