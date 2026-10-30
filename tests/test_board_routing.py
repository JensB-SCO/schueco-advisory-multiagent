from __future__ import annotations

import unittest
from pathlib import Path

from src.orchestrator import AdvisoryBoardOrchestrator
from src.board_routing import select_roles, select_skills
from src.task_context import parse_task_context


AVAILABLE = {
    "strategy", "cfo", "executive_communication", "research_evidence",
    "marketing", "coremedia", "engineering", "architecture", "operations",
    "analytics", "seo", "geo", "leadmanagement", "security",
}


class BoardRoutingTest(unittest.TestCase):
    def test_organizational_management_question_avoids_technical_roles(self) -> None:
        context = parse_task_context("# Ausgangsfrage\n> **Soll die Division ihre Führungsstruktur ändern?**")
        roles = select_roles(context, AVAILABLE)
        self.assertTrue({"strategy", "cfo", "executive_communication", "research_evidence"} <= set(roles))
        self.assertFalse({"engineering", "coremedia", "architecture", "operations"} & set(roles))
        self.assertEqual(["management-decision/SKILL.md"], select_skills(context, roles))

    def test_coremedia_handover_uses_explicit_roles(self) -> None:
        context = parse_task_context("""# Ausgangsfrage
> **Soll die CoreMedia-Entwicklung intern übernommen werden?**
# Rollen des Advisory Boards
## CFO Agent
## CoreMedia Architect und Engineering
## SRE und Operations Lead
## Marketing Lead und Leadmanagement
""")
        roles = select_roles(context, AVAILABLE)
        self.assertTrue({"coremedia", "engineering", "operations", "marketing", "leadmanagement"} <= set(roles))
        self.assertIn("cloud-agent-service-engineer/Skill.md", select_skills(context, roles))

    def test_task_009_reads_linked_evidence(self) -> None:
        path = "tasks/009_make_or_buy_coremedia.md"
        if not Path(path).is_file():
            self.skipTest("Task 009 is not in this checkout")
        board = AdvisoryBoardOrchestrator(None, "offline")
        sources = board.load_task_sources(path, board.load_task(path))
        self.assertIn("MAKE OR BUY: ARVATO", sources)
        self.assertIn("Die vier zentralen Annahmen", sources)
        self.assertNotIn("make-or-buy-assessment.md", sources)

    def test_selected_skill_paths_exist(self) -> None:
        context = parse_task_context("# Ausgangsfrage\n> **Soll die CoreMedia-Entwicklung intern erfolgen?**")
        roles = select_roles(context, AVAILABLE)
        for skill in select_skills(context, roles):
            self.assertTrue((Path("skills") / skill).is_file(), skill)

    def test_freeform_task_scope_selects_requested_disciplines(self) -> None:
        task = Path("tasks/003_branchennews_teamwork.md").read_text(encoding="utf-8")
        context = parse_task_context(task)
        roles = select_roles(context, AVAILABLE | {"ux", "backend_api", "frontend"}, task)
        self.assertTrue({"ux", "coremedia", "analytics", "security", "operations", "backend_api", "frontend"} <= set(roles))

    def test_management_process_scope_excludes_technical_roles(self) -> None:
        task = Path("tasks/009_make_or_buy_coremedia.md").read_text(encoding="utf-8")
        roles = select_roles(parse_task_context(task), AVAILABLE, task)
        self.assertEqual(
            ["cfo", "executive_communication", "marketing", "research_evidence", "strategy"],
            roles,
        )
        self.assertEqual(["management-decision/SKILL.md"], select_skills(parse_task_context(task), roles))


if __name__ == "__main__":
    unittest.main()
