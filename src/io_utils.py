from __future__ import annotations
from pathlib import Path
from datetime import datetime

def read_markdown_file(path: str | Path) -> str:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Datei nicht gefunden: {file_path}")
    return file_path.read_text(encoding="utf-8")

def read_markdown_folder(folder: str | Path) -> str:
    folder_path = Path(folder)
    if not folder_path.exists():
        return ""
    parts: list[str] = []
    for file_path in sorted(folder_path.rglob("*.md")):
        parts.append(f"\n\n# Quelle: {file_path.as_posix()}\n")
        parts.append(file_path.read_text(encoding="utf-8"))
    return "\n".join(parts)

def slugify(text: str) -> str:
    allowed = []
    for char in text.lower():
        if char.isalnum():
            allowed.append(char)
        elif char in [" ", "-", "_"]:
            allowed.append("-")
    slug = "".join(allowed)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")[:80] or "output"

def write_output(folder: str | Path, title: str, content: str) -> Path:
    out_dir = Path(folder)
    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_path = out_dir / f"{timestamp}-{slugify(title)}.md"
    file_path.write_text(content, encoding="utf-8")
    return file_path
