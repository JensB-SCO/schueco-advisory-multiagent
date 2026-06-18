# Installation: Codex + GitHub + OpenAI API

## 1. GitHub Repository anlegen
Lege ein neues privates Repository an, z. B. `schueco-advisory-multiagent`.

## 2. ZIP entpacken und Git initialisieren

```bash
cd schueco-advisory-multiagent
git init
git add .
git commit -m "Initial Schueco Advisory Multi-Agent setup"
git branch -M main
git remote add origin git@github.com:DEIN-USER/schueco-advisory-multiagent.git
git push -u origin main
```

Alternativ mit HTTPS:

```bash
git remote add origin https://github.com/DEIN-USER/schueco-advisory-multiagent.git
git push -u origin main
```

## 3. OpenAI API Key einrichten

```bash
cp .env.example .env
```

Dann `.env` bearbeiten:

```env
OPENAI_API_KEY=sk-proj-...
OPENAI_MODEL=gpt-5.1
```

Wichtig: `.env` ist in `.gitignore` und darf nicht committed werden.

## 4. Python installieren

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 5. Testlauf

```bash
python main.py --task tasks/001_architektenbereich.md
```

## 6. GitHub mit ChatGPT/Codex verbinden

In ChatGPT:
1. Settings öffnen
2. Apps öffnen
3. GitHub auswählen
4. GitHub autorisieren
5. Repository freigeben
6. Repository optional synchronisieren

## 7. Codex Web nutzen

1. `chatgpt.com/codex` öffnen
2. GitHub verbinden
3. Repository auswählen
4. Environment einrichten
5. Aufgabe starten

Beispielprompt:

```text
Lies AGENTS.md.
Erstelle einen neuen Task für die Optimierung des Produktfinders für Architekten.
Erweitere bei Bedarf knowledge/ und agents/.
Ändere keine .env.
```

## 8. Codex CLI optional

macOS/Linux:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Im Repository:

```bash
codex
```

Windows:
- Codex App oder CLI nutzen
- Git, Python und GitHub CLI installieren
- GitHub CLI anmelden:

```bash
gh auth login
```
