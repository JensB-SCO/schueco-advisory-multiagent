from __future__ import annotations

import unittest

from src.task_context import parse_task_context


class TaskContextTest(unittest.TestCase):
    def test_parses_management_assessment_task(self) -> None:
        task = """
# Schueco Digital Advisory Board
## Task v2.0 - Strategische Bewertung des Einsatzes von KI-Coding-Systemen im Marketing

# Mission

Bereitet eine Managemententscheidung vor.

# Ausgangsfrage

> **Sollte Schueco KI-basierte Coding-Systeme strategisch im Marketing etablieren?**

# Gate 1 - Individuelle Expertenanalyse

# Gate 2 - Experten-Diskussion

# Rollen des Advisory Boards

## Board Chair
## Marketing Lead
## Information Security

# Bewertungsrahmen

## Strategischer Nutzen
## Wirtschaftlicher Nutzen

# Deliverables

## Executive Summary
## SWOT
## Business Case
"""
        context = parse_task_context(task, "tasks/005_codingsysteme_einsatz.md")

        self.assertEqual("strategic_assessment", context.task_type)
        self.assertIn("KI-Coding-Systemen im Marketing", context.title)
        self.assertIn("Sollte Schueco", context.management_question)
        self.assertIn("Individuelle Expertenanalyse", context.process_gates)
        self.assertIn("Marketing Lead", context.requested_roles)
        self.assertIn("Wirtschaftlicher Nutzen", context.scoring_dimensions)
        self.assertIn("Business Case", context.deliverables)
        self.assertIn("TaskContext", context.to_prompt_block())

    def test_parses_project_brief_review_task(self) -> None:
        task = """
PROJEKTNAME: Architektenbereich
PROJEKTAUFTRAG: ./briefing.md
"""
        context = parse_task_context(task, "tasks/001_architektenbereich.md")

        self.assertEqual("project_brief_review", context.task_type)
        self.assertEqual("Architektenbereich", context.title)
        self.assertEqual("./briefing.md", context.project_brief_path)
        self.assertEqual("Architektenbereich", context.display_name)


if __name__ == "__main__":
    unittest.main()
