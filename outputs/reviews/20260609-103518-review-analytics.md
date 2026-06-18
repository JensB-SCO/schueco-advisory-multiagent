# Expertenreview: analytics

PASSED WITH RISKS

---

## 1. Kernaussage

Das Lösungskonzept adressiert zentrale Business‑ und Nutzerziele (Architekten schneller zu relevanten Inhalten führen, SEO/GEO, Lead‑Support, CoreMedia‑Umsetzbarkeit), ist aber aus Analytics‑Sicht nur dann tragfähig, wenn Messbarkeit, Datenstruktur und Monitoring von Beginn an verbindlich mitgeplant und technisch abgesichert werden. Ohne einen klaren KPI‑Rahmen, sauber definierten Tracking‑Plan und Datenqualitätsprozesse droht ein „Blindflug“ im späteren Betrieb.

---

## 2. Chancen (Analytics‑Perspektive)

**2.1 Bessere Steuerbarkeit des Architektenbereichs**

- Einführung einer klaren primären KPI (z. B. qualifizierte Architekten‑Leads oder Abrufe technischer Unterlagen) ermöglicht die Priorisierung von Content‑ und UX‑Maßnahmen.
- Sekundäre KPIs (z. B. Interaktion mit BIM/CAD‑Downloads, Nutzung von Kontakt‑/Beratungsfunktionen, Tiefeninteraktion im Referenzbereich) machen Optimierungen entlang der Customer Journey messbar.

**2.2 Verbesserte Segmentierung und Zielgruppensteuerung**

- Durch saubere Kennzeichnung des „Architekten“-Segments im Data Layer (z. B. `user_role: "architect"`, `page_segment: "architects"`) können Nutzungs- und Conversion‑Muster dieser Zielgruppe separat analysiert werden.
- GEO‑fähige Strukturen (eindeutige Entitäten wie Projekte, Produkte, Referenzen, BIM‑Objekte) ermöglichen detaillierte Behavioral‑Analysen pro Entität (z. B. „Welche Referenztypen performen bei Architekten am besten?“).

**2.3 Attribution & Lead‑Qualität**

- Sauber eingebundene HubSpot‑Formulare mit konsistenter Tracking‑Logik (Formularzweck, Quelle, Kampagne) ermöglichen
  - Bewertung der Leadqualität aus dem Architektenbereich,
  - Vergleich verschiedener Einstiegsseiten/Funnel‑Varianten (A/B Testing),
  - bessere Zuordnung von Marketing‑ und Content‑Maßnahmen zu Opportunities/Projekten im CRM.

**2.4 Content‑ & SEO‑Performance messbar machen**

- KI‑Search‑ und SEO‑fähige Strukturen (FAQ‑Blöcke, Grounding Pages, strukturierte Daten) lassen sich gut mit Page‑ und Event‑KPIs verknüpfen:
  - KPIs pro Content‑Typ (z. B. FAQ, Referenz, Produktdetail, BIM‑Download),
  - Performance von Landing Pages für Architekten (Trafficqualität, Scroll‑ und Interaktionsraten, Conversion).

**2.5 Monitoring & Frühindikatoren**

- Durch definierte Frühindikatoren (z. B. „Anzahl Sessions von Architekten mit Interaktion mit BIM/CAD‑Modulen, aber ohne Lead“) können Probleme früh erkannt und Gegenmaßnahmen eingeleitet werden (z. B. Optimierung von Kontaktangeboten auf diesen Seiten).

---

## 3. Risiken

**3.1 Unklare oder fehlende KPI‑Definition**

- Wenn das Fachkonzept nicht explizit primäre und sekundäre KPIs benennt, entsteht ein unstrukturierter Messmix (Traffic, Klicks, Downloads), der wenig strategische Aussagekraft hat.
- Gefahr: Fokus auf Vanity‑Metrics (Seitenaufrufe im Architektenbereich) statt Outcome‑KPIs (qualifizierte Leads, Angebotsanfragen, konkrete Projektanbahnung).

**3.2 Unzureichender Tracking‑Plan & Data Layer**

- Ohne frühzeitige Definition eines einheitlichen Data Layer‑Schemas (für Content‑Typen, Taxonomien, Nutzerrolle, Produkt‑/Referenz‑IDs, BIM‑Objekte etc.) wird das Tracking fragmentiert, schwer wartbar und fehleranfällig.
- CoreMedia‑Spezifika (Content Types, Taxonomien, Varianten/Internationalisierung) werden sonst nicht sauber in Events/Parametern abgebildet → eingeschränkte Auswertbarkeit nach Märkten, Sprachen, Zielgruppen.

**3.3 Messlücken bei Leadprozessen**

- Wird HubSpot nur „angestöpselt“, ohne klare Tracking‑ und Attributionslogik (Form IDs, Funnel‑Zuordnung, Kampagnenparameter, UTM‑Standard), erhält der Vertrieb zwar Leads, aber ohne belastbare Informationen zur Journey, Content‑Touchpoints und Effektivität des Architektenbereichs.
- Risiko: Fehlende Trennung zwischen Architekten‑Leads, anderen Zielgruppen und generischen Website‑Leads.

**3.4 Fehlen von Dashboards, Monitoring & Alerting**

- Ohne dedizierte Architekten‑Dashboards (Web + CRM/HubSpot) bleibt unklar:
  - ob die Ziele (schnellerer Informationszugriff, bessere Zugänglichkeit, mehr qualifizierte Leads) tatsächlich erreicht werden,
  - wie sich die KPIs nach Launch und über Releases hinweg entwickeln.
- Kein Alerting ⇒ Störungen (z. B. defekte Formulare, fehlerhafte BIM‑Links, Tracking‑Ausfälle) werden zu spät erkannt.

**3.5 Datenqualität & Konsistenz**

- Hohes Risiko von Inkonsistenzen, wenn Content‑Model (CoreMedia‑Content Types, Taxonomien, Referenz‑Strukturen) und Tracking‑Implementation nicht synchron entwickelt werden.
- Ohne regelmäßige Datenqualitätsprüfungen (z. B. Events‑Abdeckung, korrekte IDs, plausible Werte) drohen Fehlschlüsse aus den Zahlen.

---

## 4. Anforderungen (aus Analytics‑Sicht, zwingend)

**4.1 KPI‑Rahmen**

- Primäre KPI (Beispiele, eine Variante verbindlich wählen):
  - Anzahl qualifizierter Architekten‑Leads pro Zeitraum (z. B. Leads mit Architekten‑Rolle und projektbezogenem Interesse),
  - oder Anzahl der abgeschlossenen „Projektanbahnungen“ aus dem Architektenbereich (wenn im CRM abbildbar).
- Sekundäre KPIs:
  - Nutzung technischer Inhalte: BIM/CAD‑Downloads, Produktdatenblätter, Systemdetails.
  - Nutzung Referenzen: Detailansichten, Filterung, Klicks auf Projektkontakte.
  - Nutzung Kontaktmöglichkeiten: Klicks auf Ansprechpartner, Terminbuchung, Rückrufanfragen.
  - Engagement‑KPIs: Sessions, Verweildauer im Architektenbereich, Tiefe pro Session, Wiederkehrer‑Rate von Architekten.
- Frühindikatoren:
  - Sessions mit intensiver technischer Interaktion, aber ohne Lead.
  - Abbruchraten auf kritischen Schritten (z. B. Form Start vs. Form Submit).
  - Nutzung der internen Suche im Architektenbereich (Häufigkeit bestimmter Suchbegriffe wie „BIM“, „Ausschreibungstext“, „Brandschutz“).

**4.2 Tracking‑Konzept & Data Layer**

- Einheitliches Data‑Layer‑Schema, u. a.:
  - `page_type` (e.g. "architect_landing", "architect_reference_detail", "architect_bim_download"),
  - `user_role` / `target_audience` (z. B. "architect", "fabricator", "investor"),
  - `content_type` (CoreMedia‑Contenttyp, z. B. "reference", "product", "whitepaper", "faq"),
  - `taxonomy` (Fachgebiete, Gebäudeart, Produktlinien, Regionen),
  - `entity_id` und `entity_name` (Projekte, Produkte, BIM‑Objekte),
  - GEO‑relevante Metadaten (z. B. `geo_region`, `country`, `language`).
- Event‑Design (Beispiele):
  - `architect_bim_download` mit Parametern (BIM‑Typ, Produktlinie, Projektphase, Land).
  - `architect_reference_interaction` (Filter, Klick auf Referenz, Kontakt‑Klick aus Referenz).
  - `architect_form_view` / `architect_form_submit` (Formularzweck, Leadtyp, Produktfokus).
  - `internal_search_used` im Architektenbereich (Suchbegriff, Trefferanzahl, weiterführende Aktionen).

**4.3 CoreMedia‑Integration**

- Sicherstellen, dass CoreMedia:
  - alle relevanten Content Types und Taxonomien eindeutig im Markup und Data Layer bereitstellt,
  - Content‑Varianten (z. B. nach Ländern/Sprachen) mit IDs kennzeichnet, die im Tracking genutzt werden,
  - strukturelle Informationen für AI‑Search (FAQ, Entitäten, JSON‑LD‑relevante Daten) consistent ausspielt, sodass Analytics‑Events darauf referenzieren können.

**4.4 HubSpot‑Einbindung & CRM‑Übergabe**

- Klare Formularklassifizierung:
  - `form_purpose` (z. B. "project_consultation", "documentation_request", "event_registration"),
  - `lead_segment` (z. B. Architekt vs. andere Zielgruppen),
  - `source_section` (Architektenbereich + spezifische Seiten-ID).
- Standardisierte UTM‑Konventionen und Speicherung dieser Informationen beim Lead (Kampagne, Medium, Content‑Variante).
- Technische Sicherstellung, dass relevante Analytics‑IDs (z. B. Client ID, Session ID, Site Section) DSGVO‑konform mit dem CRM verknüpft werden können (Pseudonymisierung/Consent beachten).

**4.5 Dashboards, Monitoring & Alerting**

- Mindestens zwei Kern‑Dashboards:
  1. **Architekten‑Performance (Web)**
     - Traffic & Engagement im Architektenbereich (nach Markt, Sprache).
     - Nutzung von Technikinhalten & BIM/CAD.
     - Funnel‑Analysen für Key Journeys (z. B. „Recherche → Referenz → BIM Download → Kontakt“).
  2. **Architekten‑Leads & Vertrieb (HubSpot/CRM)**
     - Anzahl und Qualität der Architekten‑Leads.
     - Lead‑Quellen (Seiten, Kampagnen, Content‑Typen).
     - Übergabe‑Status und Bearbeitungszeiten im Vertrieb.
- Monitoring & Alerting:
  - Alerts bei plötzlichen Einbrüchen in:
    - Form Submits im Architektenbereich,
    - BIM/CAD‑Downloads,
    - Gesamttraffic im Architektenbereich (als Indikator für technische Probleme).
  - Alerts bei Tracking‑Anomalien (z. B. keine Events eines Typs > X Stunden).

**4.6 Datenqualitätsprüfung**

- Automatisierte Plausibilitätschecks:
  - Event‑Abdeckung: Ist auf allen definierten Seiten/Content‑Typen das erwartete Event‑Set vorhanden?
  - Feldvollständigkeit: Fehlen Pflicht‑Parameter (z. B. `entity_id`, `content_type`)?
  - Konsistenz mit CoreMedia‑Datenmodell (IDs, Taxonomien).
- Regelmäßige manuelle Stichproben (z. B. monatlich) auf ausgewählten Journeys.

---

## 5. Konkrete Empfehlungen

1. **Frühzeitig ein dediziertes Analytics‑Workstream etablieren**  
   - Analytics‑Owner definieren (Verantwortlicher für KPIs, Tracking, Dashboards, Data Quality).
   - Analytics‑Anforderungen gleichberechtigt mit UX, Content, Technik in die Projektplanung aufnehmen.

2. **KPI‑Framework gemeinsam mit Fachbereich & Vertrieb definieren**  
   - In einem Workshop mit Architekten‑Marketing, Vertrieb, Digital/IT:
     - primäre KPI fixieren (z. B. qualifizierte Architekten‑Leads pro Monat),
     - sekundäre KPIs & Frühindikatoren festlegen,
     - Zielwerte/Hypothesen formulieren (z. B. „+30 % BIM‑Downloads, +20 % Architekten‑Leads im ersten Jahr“).

3. **Umfassenden Tracking‑Plan erstellen (vor Design/Implementierung abschließen)**  
   - Pro Seitentyp/Use Case im Architektenbereich:  
     - Ziel, relevante KPIs, Events, Parameter, Trigger, Data Layer‑Felder definieren,
     - Zuordnung zu CoreMedia‑Content Types & Taxonomien dokumentieren.
   - Tracking‑Plan als verbindliches Artefakt in JIRA/Confluence o. Ä. pflegen.

4. **Data Layer‑Spezifikation eng mit CoreMedia‑Architektur abstimmen**  
   - Gemeinsames Schema zwischen Analytics, CoreMedia‑Architektur und SEO/GEO‑Verantwortlichen:
     - Entitäten (Projekte, Produkte, BIM‑Objekte),
     - Taxonomien (z. B. Gebäudeart, Region, Nutzungstyp),
     - FAQ‑Strukturen, JSON‑LD‑Datenpunkte.
   - Sicherstellen, dass alle benötigten Daten im Frontend verfügbar und stabil versioniert sind.

5. **HubSpot‑Leadprozesse sauber designen und mit Analytics verheiraten**

   - Pro Formulartyp:
     - Zweck, Leadkriterien, Routing, Nurturing‑Logik definieren (HubSpot‑Prinzipien),
     - Analytics‑Attribute (Formular‑ID, Zweck, Segment) standardisieren.
   - Gemeinsames Reporting‑Set für Marketing & Vertrieb:
     - Welche Architekten‑Seiten/Content‑Typen generieren die besten Leads?
     - Welche Assets (z. B. BIM‑Downloads, Whitepaper) korrelieren mit höheren Abschlusschancen?

6. **SEO/GEO‑Anforderungen analytisch nutzbar machen**

   - AI‑Search‑fähige Entitäten und FAQ‑Blöcke konsequent mit IDs versehen, die im Analytics‑Event mitgeführt werden.
   - Performance pro Entitätstyp und FAQ‑Cluster messbar machen (Traffic, Interaktion, Conversion).

7. **Dashboards & Alerting parallel zum Development aufbauen**

   - Keine nachgelagerten „Reporting‑Projekte“: Erste Version der Dashboards bereits zum Go‑Live bereitstellen.
   - Alerts definieren, testen und im Betrieb verankern (inkl. klarer Verantwortlichkeiten, wer reagiert).

8. **Pilotphase mit A/B‑Tests und klarer Messstrategie**

   - Wo möglich, Architekten‑Landingpages oder Modulvarianten (z. B. Platzierung BIM vs. Referenzen) A/B testen.
   - Erfolgskriterien vorab festlegen (z. B. höhere Lead‑Rate oder mehr qualifizierte Interaktionen).

---

## 6. Offene Fragen (aus Analytics‑Sicht zu klären)

1. **Primäre Business‑KPI**  
   - Was ist offiziell die eine „North Star“-KPI für den Architektenbereich (qualifizierte Leads, BIM‑Nutzung, Projektanbahnungen, …)?

2. **Definition „qualifizierter Architekten‑Lead“**  
   - Welche Felder im Formular/CRM definieren „Architekt“ und „qualifiziert“ (z. B. Projektphase, Budget, Entscheidungsbefugnis)?

3. **Verfügbare Analytics‑Stacks und Governance**  
   - Welche Tools sind aktuell im Einsatz (GA4, Adobe Analytics, Matomo, Tag Manager, HubSpot Analytics, BI‑Tools)?
   - Gibt es bestehende Data‑Layer‑Standards, die wiederverwendet oder erweitert werden müssen?

4. **Rollen & Verantwortlichkeiten**  
   - Wer verantwortet KPIs, Dashboards und laufende Optimierung für den Architektenbereich (Marketing, Digital, eigene Product Owner‑Rolle)?
   - Wer reagiert auf Alerts (technisch vs. fachlich)?

5. **Consent & Datenschutz**  
   - Welche Tracking‑Szenarien sind datenschutz‑rechtlich zulässig (v. a. im Hinblick auf CRM‑Verknüpfung und Pseudonymisierung)?
   - Wie wird Consent in CoreMedia/Frontend umgesetzt und im Data Layer/Tracking reflektiert?

6. **Internationalisierung & Marktunterschiede**  
   - Gibt es markt‑/landspezifische KPIs oder nur globale Zielgrößen?
   - Müssen einzelne Märkte eigene Architektenbereiche und Reporting‑Slices erhalten?

7. **Zeithorizont & Ressourcen für kontinuierliche Optimierung**  
   - Ist ein Budget/Ressourcenrahmen für laufende CRO‑Maßnahmen, A/B‑Tests und Content‑Optimierung vorgesehen oder endet das Projekt mit dem Launch?

Solange diese Punkte nicht geklärt und die genannten Anforderungen nicht explizit im Projekt verankert sind, bleibt das Konzept aus Analytics‑Sicht „PASSED WITH RISKS“.