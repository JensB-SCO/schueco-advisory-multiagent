# Advisory Board Roles 4.0

Diese Datei ist die zentrale Rollen- und Aufgabenuebersicht des Schueco Digital Advisory Boards. Die ausfuehrbaren Agenten-Prompts liegen weiterhin unter `agents/`; diese Uebersicht dient als schnelle Orientierung fuer Auftraggeber, Product Owner, Gremiumsmitglieder und Entwickler.

Der Runner laedt alle Markdown-Dateien aus `agents/` automatisch, mit Ausnahme von `chairman.md`. Neue Rollen werden deshalb durch eine neue Datei unter `agents/` technisch aktiv und muessen hier fachlich dokumentiert werden.

## Rollenmodell

| Rolle | Datei | Kernauftrag | Typische Prueffragen | Gate- oder Entscheidungsbezug |
|---|---|---|---|---|
| Board Orchestrator / Chairman | `agents/chairman.md` | Fuehrt Expertenbewertungen zusammen, loest Zielkonflikte und formuliert die finale Entscheidungsempfehlung. | Sind alle Pflichtabschnitte, Gates, Zielkonflikte, Risiken und Blocker entscheidungsreif zusammengefuehrt? | Finale Empfehlung, Board-Konsens, BLOCKED/READY-Status |
| Strategy Lead | `agents/strategy.md` | Bewertet strategische Passung, Business Impact, Priorisierung, Zielgruppenwert und MVP-Grenze. | Passt die Initiative zur Schueco Strategie? Ist der Nutzen klar? Ist die Roadmap plausibel? | Business Gate, Decision Framework |
| CFO Agent | `agents/cfo.md` | Bewertet Business Case, TCO, ROI, Investitionsszenarien, Budgetrisiken und Sensitivitaeten. | Sind Kosten, Nutzen, Payback, Szenarien und Annahmen belastbar genug fuer Budgetfreigabe? | Financial Gate, Managemententscheidung |
| Executive Communication Agent | `agents/executive_communication.md` | Uebersetzt Fachdetails in eine managementtaugliche Storyline fuer Geschaeftsfuehrung, Vorstand und Steering Committees. | Ist die Kernbotschaft klar? Welche Entscheidung wird verlangt? Sind So-what und Now-what praegnant? | Executive Communication Gate, Vorstandsvorlage |
| Research & Evidence Agent | `agents/research_evidence.md` | Prueft Quellen, Benchmarks, Studien, Praxisbeispiele, Evidenzgrad und Datenluecken. | Welche Aussagen sind belegt? Wie aktuell, glaubwuerdig und uebertragbar sind die Quellen? | Evidence Gate, Quellen- und Annahmenqualitaet |
| Marketing Expert | `agents/marketing.md` | Bewertet Markenfit, Zielgruppenbotschaft, Kampagnenfaehigkeit, Content-Strategie, Positionierung und Conversion-Narrative. | Ist die Botschaft markenkonform? Gibt es Kampagnenanschluss, CTA-Logik und messbare Marketingwirkung? | Marketing Gate |
| Sales Expert | `agents/sales.md` | Bewertet Vertriebsnutzen, Leadqualitaet, Umsatzpotenzial, Beratungsunterstuetzung und Customer Enablement. | Hilft die Initiative Vertrieb und Beratung? Verbessert sie Conversion, Pipeline oder Abschlusswahrscheinlichkeit? | Business Gate, Lead- und Umsatzwirkung |
| Lead Management Expert | `agents/leadmanagement.md` | Bewertet HubSpot, Lead Capture, Lead Scoring, MQL/SQL, Nurturing, Attribution und Sales Routing. | Wie werden Leads erfasst, qualifiziert, attribuiert und an Sales uebergeben? | Leadmanagement-Auswirkungen, HubSpot-Faehigkeit |
| UX & CX Strategist | `agents/ux.md` | Bewertet Nutzerfuehrung, Customer Journey, Informationsarchitektur, Accessibility, Conversion und Verstaendlichkeit. | Versteht die Zielgruppe den Weg? Sind Aufgaben, Zustaende und Conversion-Pfade klar? | UX Gate |
| Design Lead | `agents/design.md` | Bewertet visuelle Fuehrung, Design-System-Kompatibilitaet, Markenwirkung, Content-Hierarchie und responsive Layoutqualitaet. | Ist das Design markenkonform, konsistent, pflegbar und hilfreich fuer Nutzeraufgaben? | UX Gate, Marketing Gate, Design-System-Fit |
| SEO Expert | `agents/seo.md` | Bewertet Crawlbarkeit, Indexierung, Suchintention, interne Verlinkung, strukturierte Daten und Core Web Vitals. | Bedient die Loesung Suchintentionen und technische SEO-Anforderungen? | SEO Gate |
| GEO Expert | `agents/geo.md` | Bewertet AI Search Readiness, Entity-Struktur, Grounding Pages, FAQ-Bloecke, JSON-LD und zitierfaehige Inhalte. | Ist die Initiative fuer Antwortmaschinen, AI Overviews und strukturierte Fakten nutzbar? | GEO Gate |
| Digital Analytics & Monitoring Director | `agents/analytics.md` | Bewertet KPIs, Tracking, Data Layer, Dashboards, Monitoring, Alerting, A/B Testing und Datenqualitaet. | Ist Erfolg messbar? Sind Events, KPIs, Reporting und Datenqualitaet definiert? | Analytics Gate |
| CoreMedia Architect | `agents/coremedia.md` | Bewertet Content Types, Taxonomien, Workflows, Wiederverwendung, Internationalisierung, DAM und Governance. | Ist die Loesung redaktionell pflegbar und CoreMedia-kompatibel? | CoreMedia-Anforderungen, Architecture Gate |
| Architecture Lead | `agents/architecture.md` | Bewertet Systemarchitektur, Komponentenmodell, Integrationen, Datenfluesse, Skalierbarkeit und technische Abhaengigkeiten. | Sind Systemgrenzen, Integrationen, Datenfluesse und Verantwortlichkeiten entscheidungsreif? | Architecture Gate, Engineering Council |
| Backend & API Architect | `agents/backend_api.md` | Bewertet API-Design, Schnittstellen, Security, Datenquellen, Skalierung und Betrieb. | Sind API-Vertraege, Authentifizierung, Datenquellen und Fehlerfaelle klar? | Architecture Gate, Engineering Gate, Security Gate |
| Frontend Lead | `agents/frontend.md` | Bewertet Komponentenarchitektur, Performance, Accessibility, Responsive Verhalten und Design-System-Kompatibilitaet. | Ist die UI robust, performant, barrierearm, responsiv und gekapselt umsetzbar? | Engineering Gate, UX Gate |
| Engineering Lead | `agents/engineering.md` | Bewertet technische Umsetzbarkeit, Testbarkeit, Dokumentationspflichten, Konfiguration, Fehlerbehandlung, Automatisierung und Produktionsreife. | Sind Tests, Dokumentation, Betrieb, Security und Definition of Done ausreichend? | Engineering Gate, Engineering Council |
| Security Architect | `agents/security.md` | Bewertet Security, Datenschutz, Rollen- und Rechtemodelle, Secrets, Prompt-Injection-Risiken, Tool-Misuse, Datenabfluss, Audit Logging und Compliance. | Gibt es kritische Datenschutz-, Security- oder Compliance-Risiken? | Security Gate, Vetorecht |
| SRE / Operations Lead | `agents/operations.md` | Bewertet Betriebsfaehigkeit, Deployment, Rollback, Health Checks, Metrics, Logging, Alerting, Supportprozesse und Kostenrisiken. | Ist die Loesung produktionsfaehig, monitorbar, supportbar und rollback-faehig? | Operations Gate, Vetorecht |

## Agentencluster

### Management Consulting Board

Diese Rollen machen aus der fachlichen Bewertung eine entscheidungsreife Managementvorlage:

- `strategy`: strategische Passung, Priorisierung und Roadmap-Faehigkeit
- `cfo`: Business Case, TCO, ROI und Investitionsszenarien
- `executive_communication`: Management-Storyline, Folienlogik und Entscheidungsklarheit
- `research_evidence`: Quellen, Benchmarks, Evidenzgrad und Annahmenqualitaet

### Go-to-Market, Demand und Customer Journey

Diese Rollen bewerten Markt-, Zielgruppen-, Kampagnen-, Vertriebs- und Leadwirkung:

- `marketing`: Markenfit, Kampagnenfaehigkeit, Content-Strategie und CTA-Logik
- `sales`: Vertriebsnutzen, Umsatzpotenzial und Customer Enablement
- `leadmanagement`: HubSpot, Lead Capture, MQL/SQL, Nurturing und Attribution
- `ux`: Customer Journey, Verstaendlichkeit, Accessibility und Conversion
- `design`: visuelle Fuehrung, Markenwirkung und Design-System-Fit

### Findability, Content und Messbarkeit

Diese Rollen stellen sicher, dass Inhalte auffindbar, zitierfaehig, pflegbar und messbar sind:

- `seo`: Suchintention, Indexierung, interne Verlinkung und strukturierte Daten
- `geo`: AI Search Readiness, Entity-Struktur, Grounding Pages und JSON-LD
- `analytics`: KPIs, Tracking, Dashboards, Monitoring und Datenqualitaet
- `coremedia`: Content Types, Taxonomien, Workflows, DAM und Governance

### Engineering Council

Diese Rollen pruefen technische Umsetzbarkeit, Produktionsreife, Security und Betrieb:

- `architecture`: Systemarchitektur, Integrationsgrenzen und Datenfluesse
- `backend_api`: API-Design, Schnittstellen, Datenquellen und Skalierung
- `frontend`: Komponentenarchitektur, Performance, Accessibility und Responsive Verhalten
- `engineering`: Tests, Dokumentation, Automatisierung und Production Readiness
- `security`: Datenschutz, Rollen, Secrets, Missbrauchsschutz und Compliance
- `operations`: Deployment, Monitoring, Rollback, Support und Betriebsrisiken

## Blocker-Logik

Eine Rolle kann `BLOCK` oder `APPROVE WITH RISKS` empfehlen, wenn ihr Verantwortungsbereich nicht entscheidungsreif ist. Besonders kritisch sind:

- CFO: Business Case, Kostenannahmen oder ROI sind nicht belastbar.
- Research & Evidence: zentrale Managementaussagen sind unbelegt oder nur als Hypothese nutzbar.
- Executive Communication: die Empfehlung ist fachlich richtig, aber nicht managementtauglich entscheidbar.
- Marketing: Markenfit, Zielgruppenbotschaft, Kampagnenanschluss oder Conversion-Narrative fehlen.
- Analytics: Erfolg ist nicht messbar oder Tracking/Reporting ist unklar.
- Engineering: Tests, Dokumentation, Betrieb oder technische Umsetzbarkeit fehlen.
- Security: Datenschutz-, Compliance- oder Sicherheitsrisiken sind kritisch.
- Operations: produktionsrelevante Loesungen haben kein belastbares Betriebskonzept.

## Pflegehinweise

- Jede neue Rolle braucht eine Datei unter `agents/`.
- Jede neue Rolle muss hier in der Rollenmatrix ergaenzt werden.
- Wenn eine Rolle ein neues Pflichtkriterium einfuehrt, muss ein passendes Gate unter `gates/` oder eine Governance-Ergaenzung unter `board/` angelegt werden.
- Rollen muessen klar abgrenzbar bleiben: Sales bewertet Vertriebswirkung, Lead Management bewertet Leadprozesse, Marketing bewertet Botschaft und Kampagnenfaehigkeit, CFO bewertet Investmentlogik.
- Secrets duerfen nie in Rollen-, Gate- oder Governance-Dokumenten stehen.
