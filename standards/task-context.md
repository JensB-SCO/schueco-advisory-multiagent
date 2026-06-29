# TaskContext Standard

Der `TaskContext` ist die maschinenlesbare Zusammenfassung einer Task-Datei. Er sorgt dafuer, dass das Advisory Board aus dem Task erkennt, **was genau bewertet oder erzeugt werden soll**, bevor Agentenreviews und finale Empfehlung erstellt werden.

Ziel: Der Anwender schreibt nur eine Markdown-Datei unter `tasks/`. Der Runner extrahiert daraus Kontext, Task-Typ, Managementfrage, Deliverables, Rollen und Bewertungslogik.

## Was der Parser erkennt

| Feld | Bedeutung | Quelle im Task |
|---|---|---|
| `title` | Kurzname oder Titel der Aufgabe | erste `#`/`##` Ueberschrift, alternativ `PROJEKTNAME:` |
| `task_type` | erkannter Aufgabentyp | Heuristik aus Projektauftrag, Ausgangsfrage, Review-, Praesentations- oder Deliverable-Hinweisen |
| `mission` | Auftrag des Boards | Abschnitt `# Mission` |
| `management_question` | konkrete Management- oder Bewertungsfrage | Abschnitt `# Ausgangsfrage`, bevorzugt fett zitierte Frage |
| `thesis` | zu pruefende These | Text nach `These lautet` oder Abschnitt `# These` |
| `goal` | Ziel der Bewertung | Abschnitt `# Ziel` |
| `project_brief_path` | referenzierter Projektauftrag | Zeile `PROJEKTAUFTRAG: <pfad>` |
| `process_gates` | vom Task gewuenschte Prozess-Gates | Ueberschriften `# Gate 1 - ...` |
| `requested_roles` | Rollen, die der Task explizit nennt | Unterueberschriften im Abschnitt `# Rollen des Advisory Boards` |
| `scoring_dimensions` | Bewertungsdimensionen | Unterueberschriften im Abschnitt `# Bewertungsrahmen` |
| `evaluation_criteria` | fachliche Bewertungskriterien | Unterueberschriften im Abschnitt `# Bewertungskriterien` |
| `deliverables` | erwartete Ergebnisartefakte | Unterueberschriften im Abschnitt `# Deliverables` |
| `final_output` | gewuenschtes finales Format | Abschnitt `# Finale Praesentation` oder `# Finale Präsentation` |

## Unterstuetzte Task-Typen

| Task-Typ | Wann er erkannt wird | Erwartete Board-Logik |
|---|---|---|
| `project_brief_review` | `PROJEKTAUFTRAG:` ist gesetzt | Projektauftrag laden und gegen Board-Gates bewerten |
| `strategic_assessment` | `# Ausgangsfrage` plus strategische Bewertung oder Managemententscheidung | Managementfrage bewerten, These pruefen, Optionen und Entscheidung vorbereiten |
| `management_assessment` | `# Ausgangsfrage` vorhanden | konkrete Frage oder Anforderung bewerten |
| `board_review` | Review-/Gremienreview-Hinweise | vorhandene Inhalte oder Anforderungen kritisch pruefen |
| `presentation_request` | Praesentation/PowerPoint als Hauptsignal | Storyline und Praesentationslogik erzeugen |
| `deliverable_request` | `# Deliverables` vorhanden | geforderte Artefakte strukturiert liefern |
| `general_task` | keine klaren Signale | allgemeine Board-Empfehlung erzeugen |

## Empfohlenes Task-Template

```markdown
# Schueco Digital Advisory Board
## Task vX.Y - Kurzer Titel

# Mission

Beschreibe, welche Rolle das Board einnehmen soll und was entschieden oder bewertet werden muss.

# Ausgangsfrage

> **Formuliere die konkrete Managementfrage oder Anforderung als eine klare Frage.**

# These

> **Optional: Formuliere eine These, die das Board kritisch pruefen soll.**

# Ziel

Beschreibe, was am Ende entscheidungsreif vorliegen muss.

# Arbeitsprinzip

Optional: Beschreibe, wie das Board arbeiten soll.

# Gate 1 - Name

Optional: Beschreibe Prozess-Gates, die der Board Chair beruecksichtigen soll.

# Rollen des Advisory Boards

## Board Chair
## Strategy Director
## CFO Agent
## Marketing Lead
## Information Security

# Bewertungsrahmen

## Strategischer Nutzen
## Wirtschaftlicher Nutzen
## Risiken
## Umsetzbarkeit
## Prioritaet

# Bewertungskriterien

## Business
## Marketing
## Technologie
## Organisation
## Wirtschaftlichkeit

# Deliverables

## Executive Summary
## Management Decision
## SWOT
## Business Case
## Roadmap
## Governance

# Finale Praesentation

Optional: Beschreibe, ob eine Folienstruktur, Storyline oder Praesentationslogik erwartet wird.
```

## Minimalformat

Fuer viele Aufgaben reichen drei Abschnitte:

```markdown
## Task v1.0 - Titel

# Ausgangsfrage

> **Welche konkrete Frage soll das Board beantworten?**

# Deliverables

## Executive Summary
## Entscheidungsempfehlung
## Risiken
```

## Regeln fuer gute Tasks

- Die konkrete Frage gehoert in `# Ausgangsfrage`.
- Eine These gehoert in `# These` oder in einen klaren Satz mit `These lautet`.
- Gewuenschte Ergebnisse gehoeren unter `# Deliverables`.
- Wenn ein Projektauftrag geladen werden soll, nutze `PROJEKTAUFTRAG: <pfad>`.
- Wenn kein Projektauftrag gemeint ist, verwende keine `PROJEKTAUFTRAG:`-Zeile.
- Schreibe keine Secrets, Tokens oder vertraulichen Zugangsdaten in Task-Dateien.
