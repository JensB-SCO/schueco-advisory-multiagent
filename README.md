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
skills/      Wiederverwendbare Skills als Unterordner mit Skill.md
```

## Advisory Board 4.0

Der Runner waehlt anhand von Managementfrage, TaskContext und explizit genannten Rollen ein passendes Teilgremium aus `agents/`. Der Chairman erstellt die finale Empfehlung. Managementfragen erhalten Strategy, CFO, Research & Evidence und Executive Communication; technische Fachrollen und der Cloud-Engineering-Skill kommen nur bei Bezug zur Aufgabe hinzu. `skills/management-decision/Skill.md` fuehrt wirtschaftliche und organisatorische Entscheidungen. Die finale Empfehlung folgt der 4.0-Pflichtstruktur:

Das Gremium verfuegt ueber Rollen fuer Strategy, Business/Sales, CFO, Marketing, Executive Communication, Research & Evidence, UX, Design, SEO, GEO, Leadmanagement, Analytics, CoreMedia, Architecture, Backend/API, Frontend, Engineering, Security und Operations. Neue Rollen werden als Markdown-Datei unter `agents/` gepflegt; fuer ihre automatische Auswahl wird `src/board_routing.py` erweitert. Im Task genannte Rollen haben Vorrang.

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
python main.py --task tasks/001_architektenbereich.md
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py --task tasks/001_architektenbereich.md
```

So startest du es aus dem Projektordner:

```powershell
.\.venv\Scripts\python.exe main.py --task tasks/001_architektenbereich.md
```

Fuer die aktuelle Make-or-Buy-Frage:

```powershell
.\.venv\Scripts\python.exe main.py --task tasks/009_make_or_buy_coremedia/Task_v2_make_or_buy_arvato_lissabon.md
```

Der Runner liest die im Task verlinkten lokalen Markdown- und Word-Dateien als Quellenmaterial ein. Deren Inhalt ist keine Anweisung an das Board. Nicht vorhandene Referenzen werden als fehlende Quellen markiert; eine fehlende Ausgangspraesentation wird deshalb nicht als gepruefte Quelle dargestellt. Rollen werden auch aus fachlichen Anforderungen im Task gewaehlt, nicht aus einer angehaengten Standard-Ergebnisstruktur. Rollen und Skills werden vor dem Lauf ausgegeben.

Ohne nutzbaren API-Zugang erstellt der Runner einen gekennzeichneten regelbasierten Offline-Fallback. Der Fallback fuer Task 009 erstellt eine spezifische Managementbewertung aus Task, Uebergabeprotokoll und Word-Unterlage; eine vorhandene fruehere Bewertung kann als weitere Grundlage einfließen. Im aktuellen Checkout fehlt `outputs/009_make_or_buy_coremedia_bewertung.md`, obwohl der Task darauf verweist. Der Fallback ist keine neue semantische Gremiendiskussion. Das Struktur-Gate prueft Abschnitte und Schluesselbegriffe, nicht die inhaltliche Richtigkeit oder Belegqualitaet. Ein Status `PASSED` ist daher keine Managementfreigabe.

Tests starten mit `python -m unittest discover -s tests -v`, vorzugsweise mit dem Python-Interpreter der `.venv`.

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
