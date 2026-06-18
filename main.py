from __future__ import annotations
import argparse
from dotenv import load_dotenv
from src.openai_client import get_client, get_model
from src.orchestrator import AdvisoryBoardOrchestrator

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Schüco Digital Advisory Board Multi-Agent Runner")
    parser.add_argument("--task", required=True, help="Pfad zur Markdown-Aufgabe, z. B. tasks/001_architektenbereich.md")
    return parser.parse_args()

def main() -> None:
    load_dotenv()
    args = parse_args()
    orchestrator = AdvisoryBoardOrchestrator(client=get_client(), model=get_model())
    result = orchestrator.run(task_path=args.task)
    print("\n" + "=" * 80)
    print(result)
    print("=" * 80)

if __name__ == "__main__":
    main()
