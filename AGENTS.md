# Schüco Digital Advisory Board – Codex Instructions

## Ziel
Dieses Repository enthält ein Multi-Agent-System für die Weiterentwicklung der Schüco Website.

## Codex-Regeln
- Agenten liegen als Markdown unter `agents/`.
- Unternehmenswissen liegt als Markdown unter `knowledge/`.
- Aufgaben liegen als Markdown unter `tasks/`.
- Ergebnisse werden unter `outputs/` erzeugt.
- Der TaskContext-Standard liegt unter `standards/task-context.md`; neue Tasks sollen Ausgangsfrage, Ziel und Deliverables klar auszeichnen.
- Marketing ist als eigene Gremiumsrolle unter `agents/marketing.md` zu beruecksichtigen.
- CFO, Executive Communication und Research & Evidence sind fuer Managementvorlagen als spezialisierte Rollen unter `agents/` zu beruecksichtigen.
- `.env` niemals ändern oder committen.
- Keine Secrets in Markdown-Dateien schreiben.

## Qualitätsstruktur
Jede finale Empfehlung braucht:
1. Executive Summary
2. Expertenbewertungen
3. Zielkonflikte
4. Lösungsoptionen
5. MVP
6. Roadmap
7. CoreMedia-Anforderungen
8. SEO-/GEO-Anforderungen
9. Leadmanagement-Auswirkungen
10. Analytics Gate
11. Risiken
12. Entscheidungsempfehlung

Marketing-relevante Empfehlungen muessen zusaetzlich Markenfit, Zielgruppenbotschaft, Kampagnenfaehigkeit, CTA-Logik und messbare Marketingwirkung benennen.

Managementrelevante Empfehlungen muessen zusaetzlich Business Case/TCO/ROI, Evidenzbasis/Quellenqualitaet und eine entscheidungsreife Executive Storyline benennen.
