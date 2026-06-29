# Governance 4.0

## Entscheidungslogik

Eine Empfehlung ist nur entscheidungsreif, wenn alle relevanten Gates bewertet wurden und offene Risiken explizit genannt sind.

## Freigabestatus

- READY: Empfehlung ist entscheidungsreif und alle Pflichtgates sind erfuellt.
- READY WITH RISKS: Empfehlung ist entscheidungsreif, aber Risiken oder Abhaengigkeiten muessen gesteuert werden.
- BLOCKED: Empfehlung verletzt ein Pflichtgate oder enthaelt nicht genug Informationen fuer eine belastbare Entscheidung.

## Pflichtgates

- Business Gate
- Financial Gate
- Marketing Gate
- Evidence Gate
- Executive Communication Gate
- UX Gate
- SEO Gate
- GEO Gate
- Analytics Gate
- Architecture Gate
- Engineering Gate
- Security Gate
- Operations Gate

## Eskalationsregeln

Ein Thema wird eskaliert, wenn:

- Business Nutzen und Umsetzungsaufwand unklar bleiben.
- Business Case, TCO, ROI oder Investitionsszenarien unklar bleiben.
- Markenfit, Zielgruppenbotschaft oder Kampagnenanschluss unklar bleiben.
- Quellenbasis, Benchmark-Qualitaet oder Evidenzgrad entscheidungsrelevanter Aussagen unklar bleiben.
- Die Empfehlung fuer Management oder Vorstand nicht entscheidungsreif formuliert ist.
- Datenschutz, Security oder Compliance betroffen sind.
- CoreMedia-, HubSpot-, Analytics- oder Betriebsgrenzen verletzt werden.
- Die Empfehlung keine messbaren KPIs enthaelt.
- Der Engineering Council die Production Readiness nicht bestaetigt.

## Dokumentationspflicht

Alle neuen Rollen, Gates, Standards und Master-Prompts werden als Markdown im Repository gepflegt. Secrets duerfen nicht in Markdown-Dateien geschrieben werden. `.env` bleibt unveraendert und wird nicht committet.
