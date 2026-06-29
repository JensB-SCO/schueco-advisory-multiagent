# Schueco Advisory Multi-Agent System 4.0

Python-Repository fuer das Schueco Digital Advisory Board 4.0 mit OpenAI API, Markdown-Agenten, Markdown-Wissensbasis, Board-Orchestrierung, Governance-Artefakten und erweiterten Quality Gates inklusive Marketing-, Finance-, Executive-Communication- und Research/Evidence-Perspektive.

## Struktur

```text
agents/      Rollen und Personas des Advisory Boards
board/       Charter, Governance, Decision Framework und Definition of Done
gates/       Business-, Marketing-, Financial-, Evidence-, Executive-Communication-, UX-, SEO-, GEO-, Analytics-, Architecture-, Engineering-, Security- und Operations-Gates
knowledge/   Unternehmenswissen
prompts/     Master-, Orchestration- und Voting-Prompts
standards/   Dokumentations-, Testing-, Security-, Monitoring- und Agent-Policies
tasks/       Aufgaben als Markdown
outputs/     Generierte Reviews und Empfehlungen
templates/   Vorlagen fuer Architektur, README, Changelog, Operations und Evaluation
skills/      Wiederverwendbare Skills, z. B. Cloud Agent & Service Engineer
```

## Advisory Board 4.0

Der Runner laedt alle Markdown-Agenten aus `agents/` ausser `chairman.md`. Die finale Empfehlung wird durch den Chairman erzeugt und gegen die 4.0-Pflichtstruktur geprueft:

Das Gremium umfasst Rollen fuer Strategy, Business/Sales, CFO, Marketing, Executive Communication, Research & Evidence, UX, Design, SEO, GEO, Leadmanagement, Analytics, CoreMedia, Architecture, Backend/API, Frontend, Engineering, Security und Operations. Neue Rollen werden als Markdown-Datei unter `agents/` gepflegt und automatisch in den Lauf aufgenommen.

1. Executive Summary
2. Expertenbewertungen
3. Zielkonflikte
4. Loesungsoptionen
5. MVP
6. Roadmap
7. CoreMedia-Anforderungen
8. SEO-/GEO-Anforderungen
9. Leadmanagement-Auswirkungen
10. Analytics Gate
11. Risiken
12. Entscheidungsempfehlung

Technische Empfehlungen muessen zusaetzlich Architecture Gate, Engineering Gate, Security Gate und Operations Gate beruecksichtigen. Oeffentliche, vertriebs- oder kampagnennahe Empfehlungen muessen das Marketing Gate mit Markenfit, Zielgruppenbotschaft, Kampagnenverwertung, CTA-Logik und messbarer Marketingwirkung beruecksichtigen. Managementvorlagen muessen Financial Gate, Evidence Gate und Executive Communication Gate fuer Business Case, belastbare Quellen und entscheidungsreife Storyline einbeziehen.

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
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
python main.py --task tasks/001_architektenbereich.md
```

So startest du es aus dem Projektordner:

```powershell
.\.venv\Scripts\python.exe main.py --task tasks/001_architektenbereich.md
```

Die Ergebnisse landen danach taskbezogen unter:

```text
outputs/<task-name>/reviews/
outputs/<task-name>/recommendation/
```

Beispiel:

```text
outputs/001-architektenbereich/reviews/
outputs/001-architektenbereich/recommendation/
```

## Governance

Die verbindlichen Regeln liegen in:

- `board/charter.md`
- `board/roles.md`
- `board/governance.md`
- `board/decision-framework.md`
- `board/escalation-framework.md`
- `board/definition-of-done.md`
- `standards/task-context.md`

Secrets duerfen nicht in Markdown-Dateien geschrieben werden. `.env` wird lokal genutzt, aber nicht versioniert.
