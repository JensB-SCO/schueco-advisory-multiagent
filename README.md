# Schüco Advisory Multi-Agent Starter

Python-Starter-Repository für ein Schüco Digital Advisory Board mit OpenAI API, Markdown-Agenten, Markdown-Wissensbasis, Chairman-Orchestrierung und Analytics Gate.

## Schnellstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python main.py --task tasks/001_architektenbereich.md
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
python main.py --task tasks/001_architektenbereich.md
```


So startest du es aus dem Projektordner:

```powershell
.\.venv\Scripts\python.exe main.py --task tasks/001_architektenbereich.md
```

Falls die virtuelle Umgebung vorher aktiviert werden soll:

```powershell
.\.venv\Scripts\Activate.ps1
python main.py --task tasks/001_architektenbereich.md
```

Die Ergebnisse landen danach unter:

```text
outputs/reviews/
outputs/recommendations/
```

