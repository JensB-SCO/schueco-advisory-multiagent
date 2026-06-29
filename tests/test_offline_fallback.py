from __future__ import annotations

import unittest

from src.analytics_gate import AnalyticsGate
from src.offline_fallback import (
    build_offline_recommendation,
    build_offline_review,
    is_insufficient_quota_error,
)


class OfflineFallbackTest(unittest.TestCase):
    def test_detects_insufficient_quota(self) -> None:
        error = RuntimeError(
            "Error code: 429 - code=insufficient_quota; "
            "You exceeded your current quota"
        )
        self.assertTrue(is_insufficient_quota_error(error))
        self.assertFalse(is_insufficient_quota_error(RuntimeError("timeout")))

    def test_review_is_clearly_marked_as_offline(self) -> None:
        review = build_offline_review(
            "security",
            "PROJEKTNAME: Testprojekt\nAPI-Absicherung ueber Keycloak",
        )
        self.assertIn("Offline-Fallback", review)
        self.assertIn("Keycloak", review)
        self.assertIn("## 6. Offene Fragen", review)

    def test_marketing_review_uses_role_specific_focus(self) -> None:
        review = build_offline_review(
            "marketing",
            "PROJEKTNAME: Testprojekt\nNeue Kampagnenseite fuer Architekten",
        )
        self.assertIn("Markenfit", review)
        self.assertIn("Zielgruppenbotschaft", review)
        self.assertIn("CTA-Logik", review)

    def test_management_consulting_roles_use_specific_focus(self) -> None:
        cfo_review = build_offline_review(
            "cfo",
            "PROJEKTNAME: Testprojekt\nManagementvorlage fuer Budgetfreigabe",
        )
        executive_review = build_offline_review(
            "executive_communication",
            "PROJEKTNAME: Testprojekt\nVorstandsvorlage",
        )
        evidence_review = build_offline_review(
            "research_evidence",
            "PROJEKTNAME: Testprojekt\nBenchmark-basierte Empfehlung",
        )

        self.assertIn("Business Case", cfo_review)
        self.assertIn("TCO", cfo_review)
        self.assertIn("ROI", cfo_review)
        self.assertIn("Kernbotschaft", executive_review)
        self.assertIn("managementtaugliche Storyline", executive_review)
        self.assertIn("Quellen", evidence_review)
        self.assertIn("Evidenzgrad", evidence_review)

    def test_recommendation_contains_required_sections(self) -> None:
        recommendation = build_offline_recommendation(
            "PROJEKTNAME: Testprojekt",
            ["Review A", "Review B"],
        )
        for section in (
            "Executive Summary",
            "Expertenbewertungen",
            "Zielkonflikte",
            "Loesungsoptionen",
            "MVP",
            "Roadmap",
            "CoreMedia-Anforderungen",
            "SEO-/GEO-Anforderungen",
            "Leadmanagement-Auswirkungen",
            "Analytics Gate",
            "Risiken",
            "Entscheidungsempfehlung",
            "Gemeinsame Restpunkteliste",
        ):
            self.assertIn(section, recommendation)
        self.assertEqual("PASSED", AnalyticsGate().validate(recommendation).status)

    def test_ai_coding_task_is_assessment_not_project_brief(self) -> None:
        task = """
# Schueco Digital Advisory Board
## Task v2.0 - Strategische Bewertung des Einsatzes von KI-Coding-Systemen im Marketing

# Ausgangsfrage

> **Sollte Schueco KI-basierte Coding-Systeme zukuenftig strategisch im Marketing etablieren?**

# Deliverables

## SWOT
## Marktvergleich
## Business Case
"""
        recommendation = build_offline_recommendation(task, ["Review A"])

        self.assertIn("KI-Coding-Systeme im Marketing", recommendation)
        self.assertIn("Ja, bedingt und kontrolliert", recommendation)
        self.assertIn("bewertet die gestellte Anforderung", recommendation)
        self.assertIn("SWOT", recommendation)
        self.assertIn("Marktvergleich", recommendation)
        self.assertIn("Business Case", recommendation)
        self.assertIn("Management Storyline", recommendation)
        self.assertNotIn("Projektauftrag ist", recommendation)


if __name__ == "__main__":
    unittest.main()
