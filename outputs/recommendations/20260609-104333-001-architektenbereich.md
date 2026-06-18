## 1. Management Summary

Der Architektenbereich von schueco.com soll zu einem klar abgegrenzten, international skalierbaren „Architect Hub“ weiterentwickelt werden. Dieser bündelt alle für Architekten relevanten Inhalte – Systeme/Technik, BIM/CAD, technische Dokumente, Referenzen, Services & Ansprechpartner – entlang typischer Planungs‑Use‑Cases und macht sie AI‑Search‑, SEO‑, GEO‑ und Lead-fähig.

Die Experten sind sich inhaltlich einig:  
- **Architekten-Hub als eigenständiger Bereich** mit eigener IA, URL‑Struktur, Content-Modell und KPI‑Set.  
- **Strukturiertes CoreMedia-Modell** (Content Types, Taxonomien, Workflows, Internationalisierung, DAM‑Anbindung).  
- **Lead- und Vertriebsunterstützung über HubSpot/CRM** mit klar definierten Formularzwecken, Routing und Nurturing.  
- **AI-/SEO-/GEO‑Fähigkeit** durch Grounding Pages, FAQ/Answer-Blöcke und JSON‑LD.  
- **Verbindliches Analytics‑Setup** mit eindeutiger primärer KPI, Event-Design, Dashboards und Alerting.

Das Analytics‑Review bewertet den Ansatz jedoch als „PASSED WITH RISKS“. Eine Umsetzung ist nur verantwortbar, wenn ein explizites **Analytics Gate** in das Projekt integriert wird (siehe Abschnitt 6).

---

## 2. Zielbild: „Schüco Architect Hub“

### 2.1 Positionierung & Ziele

Der neue Architektenbereich wird als **„Schüco Architect Hub“** positioniert:

- **Für wen?** Architekten und Planer in allen relevanten Märkten.  
- **Nutzenversprechen:** „Alle relevanten Planungsinformationen – Systeme, BIM, Details, Referenzen und Beratung – an einem Ort, in maximal 3 Klicks erreichbar.“  
- **Business-Ziele:**
  - Mehr und qualitativ bessere Architekten‑Leads (Projektanbahnung).
  - Höhere Nutzung von BIM/CAD und technischen Unterlagen.
  - Bessere Sichtbarkeit für architektenrelevante Suchanfragen (SEO/GEO).
  - Stärkere Unterstützung von Vertrieb und Objektmanagement durch digitale Signale.

### 2.2 Grundprinzipien

1. **Task-orientiert statt systemzentriert:** Einstiege nach Aufgaben (Planen, Detaillieren, Ausschreiben, Referenzen, Beratung), nicht nach interner Produktlogik.  
2. **Ein Ort, viele Perspektiven:** Systeme, BIM/CAD, Doku, Referenzen und Services werden pro Use Case verknüpft, nicht isoliert nebeneinander gehalten.  
3. **Ein Content – viele Sichten:** Kernentitäten (System, Referenz, BIM‑Asset, Doku, Ansprechpartner) werden in CoreMedia einmalig gepflegt und in Architekten‑Journeys wiederverwendet.  
4. **„Open first, gate where it matters“:** Basisinformationen frei zugänglich; Gating nur bei klar hohem Intent (Projektpakete, Beratung, Bundles).  
5. **Messbar ab Tag 1:** KPI‑Gerüst, Tracking, Dashboards, Alerting und Verantwortlichkeiten werden vor der Umsetzung fixiert (Analytics Gate).

---

## 3. Struktur & Informationsarchitektur

### 3.1 Top-Level-Struktur

Ein klarer Navigationspunkt, z. B. **„Für Architekten“** (lokalisiert), führt in den Architect Hub:

**/architekten/** (bzw. /architects/ je Sprache) – zentrale Landingpage mit 4–5 Einstiegsclustern:

1. **Planung & Systeme**  
   - Systemlösungen aus Architektenperspektive (Use Case, Gebäudetyp, Leistungsanforderung).  

2. **BIM & CAD**  
   - Zentrale Bibliothek für Revit/IFC/DWG etc. mit Filtern nach System, Format, Region/Norm, Phase.  

3. **Technische Dokumente & Ausschreibung**  
   - Datenblätter, Detailzeichnungen, Prüfberichte, Ausschreibungstexte, Planerpakete.  

4. **Referenzen & Inspiration**  
   - Filterbare Referenzdatenbank (Gebäudetyp, Region, System, Nachhaltigkeit, Architekturbüro).  

5. **Beratung, Services & Weiterbildung**  
   - Ansprechpartner, Projektberatung, Ausschreibungsservice, Architektenprogramme, Schulungen/Webinare.

Zu jedem Cluster gibt es eine eigene Landingpage als **Grounding Page** (SEO/GEO‑Kern):

- /architekten/planung/  
- /architekten/bim-cad/  
- /architekten/dokumente-ausschreibung/  
- /architekten/referenzen/  
- /architekten/beratung-services/

### 3.2 Schlüssel-Journeys

Beispiele für geführte Journeys:

- **Inspiration → Projektanbahnung**  
  /architekten/referenzen/ → Filter (z. B. Bürohochhaus, Region, Fassade) → Referenzdetail → verwendete Systeme → CTA „Projekt mit Architektenberater besprechen“.

- **Planung → BIM → Beratung**  
  /architekten/planung/ → Systemdetailseite → BIM/CAD-Block → Download oder Projektpaket → CTA „Technische Beratung zu diesem System“.

- **Ausschreibung → Dokumentpaket → Lead**  
  /architekten/dokumente-ausschreibung/ → Filtern nach System/Gebäudetyp → Download-Bundle „Ausschreibungspaket“ → kurzes Formular (Projektkontext) → Übergabe an Vertrieb.

---

## 4. CoreMedia-Umsetzung: Content-Modell & Governance

### 4.1 Zentrale Content Types

Mindestens folgende (teilweise existierende) Typen sind klar zu modellieren/schärfen:

1. **ArchitectLandingPage**  
   - Slots: Hero, Intents (Kacheln), Highlight-Referenzen, Top-Systeme, BIM/CAD-Teaser, Service-Teaser, FAQ.

2. **System / SystemForArchitects**  
   - Felder: Architekten‑Kurzbeschreibung, Anwendungsbereiche, Gebäudetypen, Leistungsmerkmale, Normen/Zulassungen.  
   - Relationen: BIM/CAD‑Assets, technische Dokumente, Referenzen, Ansprechpartner, Services, FAQs.

3. **BIMCadAsset**  
   - Felder: System-ID, Format (Revit, IFC, DWG, etc.), Software, LOD, Version, Norm/Region, Sprache, Gültigkeit.  
   - Relationen: verknüpfte Systeme, ggf. Referenzen.  

4. **TechnicalDocument**  
   - Typ: Datenblatt, Prüfbericht, Zulassung, Detailzeichnung, Ausschreibungstext, Planungsleitfaden.  
   - Attribute: Version, Gültigkeit, Region/Norm, Sprache.  
   - Relationen: Systeme, ggf. Referenzen.

5. **ReferenceProject**  
   - Attribute: Gebäudetyp, Nutzung, Standort, Land/Region, Architekturbüro, Zertifizierungen (DGNB, LEED, etc.), Projektphase.  
   - Relationen: verwendete Schüco-Systeme, Downloads, Ansprechpartner.

6. **ExpertProfile / ContactPerson**  
   - Attribute: Rolle (Architektenberater, technischer Support), Region/Land, Systemschwerpunkte, Sprachen, Kontaktkanäle.  

7. **ServiceOffer / Tool**  
   - z. B. Ausschreibungsservice, statische Vorbemessung, Bemusterung, Webinare.  
   - Relationen: Zielgruppe Architekt, Regionen, Systeme.

8. **FAQEntry / AnswerBlock**  
   - Felder: Frage, Kurzantwort (max. 2–3 Absätze, zitierfähig), optionale Langantwort, Thema, Zielgruppe.  
   - Einsatz: auf Grounding Pages und System-/BIM-Seiten.

9. **LeadMagnet / DownloadBundle**  
   - z. B. „Planerpaket Fassade X“, „Ausschreibungspaket Fenster Y“.  
   - Relationen: HubSpot-Formular, TechnicalDocuments, BIMCadAssets.

### 4.2 Taxonomien

Verbindliche Taxonomien (global definieren, lokal anwendbar):

- Zielgruppe: Architekt/Planer (für Segmentierung & Personalisierung).  
- Systemfamilie: Fassade, Fenster, Tür, Schiebeelemente, Sonnenschutz, Automation.  
- Gebäudetyp: Büro, Wohnen, Bildung, Healthcare, Hotel, Industrie, Hochhaus, Sonderbau.  
- Planungsphase: Konzept, Entwurf, Ausführungsplanung, Ausschreibung, Ausführung.  
- Thema: Nachhaltigkeit, Energieeffizienz, Brandschutz, Schallschutz, Sicherheit, Barrierefreiheit, BIM.  
- Region/Land & Normraum.  

### 4.3 Workflows, Wiederverwendung, Internationalisierung, DAM

- **Workflows:**  
  - Technische Inhalte (System, BIM, Doku) mit Fachfreigabe (Engineering/Produktmanagement) + redaktioneller Freigabe (Marketing) + ggf. Legal.  
  - Ländervarianten über CoreMedia‑Lokalisierungsmechanismen mit klarer Regel: was global, was lokal (z. B. global: Systembeschreibung; lokal: Norm, Zulassung, Ansprechpartner).

- **Wiederverwendung:**  
  - Systeme, Referenzen, BIM, Doku nur 1x anlegen; via Teaser-Module in Architekten‑Hub, Produktbereich, Kampagnenseiten einbinden.  

- **DAM-Anbindung:**  
  - BIM/CAD, PDFs, Bilder, Videos im DAM; CoreMedia referenziert sie (keine Duplikate).  
  - Einheitliche Metadaten‑Felder (System-ID, Gebäudetyp, Region) im DAM für saubere Filterbarkeit.

---

## 5. SEO‑, GEO‑ & Lead-Konzept

### 5.1 SEO & GEO (AI-Search-Fähigkeit)

- **Suchintentionen abdecken:**  
  - „Schüco Architektenportal / Architektenservice“.  
  - „Schüco BIM Daten“, „Schüco Revit/IFC“, „Schüco Ausschreibungstexte“.  
  - „[Gebäudetyp] Referenzen Schüco“.  
  - „[System] technische Daten / Detailzeichnungen / U‑Wert“.

- **Grounding Pages & FAQ-Strukturen:**  
  - Jede der fünf Cluster-Landingpages enthält:
    - kurze Executive Summary (für AI‑Zitation),  
    - modulare Abschnitte (H2/H3) zu Unterthemen,  
    - 5–15 FAQs mit FAQPage‑JSON‑LD (Schema.org),  
    - automatische Teaser auf Systeme, Referenzen, Downloads, Services.

- **JSON-LD-Strukturierte Daten:**  
  - Organization, BreadcrumbList site‑weit.  
  - Product/ProductModel für Systemseiten.  
  - FAQPage für FAQ‑Blöcke.  
  - CreativeWork/Dataset für BIM/CAD und Technische Dokumente.  
  - Event für Architekten-Webinare/Schulungen.  
  - Person/ContactPoint für Ansprechpartner (wo sinnvoll).

### 5.2 HubSpot & Leadprozesse

- **Formularzwecke (konkret getrennt):**  
  1. Projektberatung anfragen (High‑Intent, MQL/SQL).  
  2. Technische Rückfrage an Architektenberater.  
  3. BIM-/Ausschreibungs-Paket für konkretes Projekt anfordern.  
  4. Newsletter/Updates für Architekten (Nurturing).  
  5. Schulung/Webinar-Anmeldung.

- **Leadqualifikation (Pflichtfelder):**  
  - Rolle (Architekt/Planer/Student/sonstige).  
  - Projektstatus / Planungsphase.  
  - Projekttyp (Gebäudeart).  
  - Projektland/Region.  
  - Grobe Größenklasse/Volumen (Bandbreiten).  

- **Routing & Nurturing (HubSpot-Prinzipien):**  
  - Regelbasiertes Routing nach Region, Projekttyp, Systemfokus; Übergabe an Architektenberater/Objektmanagement.  
  - Nurturing-Strecken je Phase:
    - Early: Referenzen, Inspiration, Systemübersichten.  
    - Mid: BIM/CAD, technische Guides, Detaildokus.  
    - Late: Ausschreibungshilfen, Projektberatung, Bemusterung.

- **Sales Enablement:**  
  - Vordefinierte E‑Mail‑Templates und Content-Pakete (Referenzen, Systeminfo, BIM‑Links), direkt aus HubSpot/CRM nutzbar.  

---

## 6. Analytics Gate (verpflichtend)

Das Analytics‑Review stuft den Ansatz als **„PASSED WITH RISKS“** ein. Deshalb wird ein **Analytics Gate** als verbindliche Projektphase definiert. Ohne dessen Erfüllung keine Freigabe für Implementierung/Go‑Live.

### 6.1 Ziel des Analytics Gate

- Sicherstellen, dass der Architect Hub **strategisch messbar** ist und auf klare Business‑Ziele einzahlt.  
- Vermeiden von „Vanity Metrics only“ (Traffic, Downloads ohne Kontext).  
- Basis schaffen für kontinuierliche Optimierung (CRO, Content‑Optimierung, SEO‑Feintuning).

### 6.2 Inhalte des Analytics Gate

**A. KPI-Framework (muss vor Umsetzung fixiert sein)**

1. **Primäre KPI (eine „North Star“ auswählen und dokumentieren):**  
   - Empfohlene Option: **Anzahl qualifizierter Architekten‑Leads pro Monat** aus dem Architect Hub  
     (Kriterien: Rolle = Architekt/Planer, projektbezogene Angaben vorhanden, definiertes MQL‑Level erreicht).  

2. **Sekundäre KPIs (u. a.):**  
   - Nutzung technischer Inhalte: Anzahl Sessions mit BIM/CAD‑Downloads, Technische-Doku‑Downloads.  
   - Nutzung Referenzen: Views, Filterinteraktionen, Klicks zu Systemseiten und Ansprechpartnern.  
   - Nutzung Kontaktmöglichkeiten: Klicks auf Ansprechpartner, Formularstarts/-abschlüsse.  
   - Engagement: Verweildauer und Seitentiefe im Architektenbereich, Wiederkehrer‑Rate.  
   - SEO: Organischer Traffic auf Architekten‑Cluster und Grounding Pages.

3. **Frühindikatoren:**  
   - Sessions mit intensiver technischer Interaktion, aber ohne Lead (Optimierungsbedarf für CTAs).  
   - Abbruchraten in Formularen (Start vs. Submit).  
   - Häufigkeit und Zero‑Result‑Rate bei interner Suche im Architektenbereich (z. B. Suchbegriffe „BIM“, „Ausschreibung“).

**B. Tracking-Konzept & Data Layer-Spezifikation**

- **Data Layer (Beispiele für Felder):**  
  - `page_type` (e.g. "architect_hub", "architect_system_detail", "architect_bim_library", "architect_reference_detail").  
  - `target_audience` (z. B. "architect").  
  - `content_type` (System, Reference, BIM, TechDoc, FAQ, Service).  
  - `taxonomy` (Gebäudetyp, Systemfamilie, Planungsphase, Region).  
  - `entity_id`, `entity_name` (System‑ID, Referenz‑ID, BIM‑Asset‑ID).  
  - `geo_region`, `country`, `language`.  

- **Event-Design (mindestens):**  
  - `architect_hub_view` (mit Land, Sprache).  
  - `architect_bim_download` (System-ID, Format, Region, Projektphase).  
  - `architect_techdoc_download` (Dokumenttyp, System-ID, Region).  
  - `architect_reference_interaction` (Filter-Nutzung, Referenzklick).  
  - `architect_contact_click` (Kontext: System/Referenz/BIM/Doku).  
  - `architect_form_view` / `architect_form_submit` (Formularzweck, Leadtyp, Markt).  
  - `architect_search_used` (Suchbegriff, Trefferanzahl, Weiterklick).

**C. HubSpot-/CRM-Attribution**

- Jedes Formular erhält technische IDs plus semantische Attribute:  
  - `form_purpose`, `lead_segment` (Architekt), `source_section` (Architect Hub + Seiten-ID).  
- Standardisierte UTM‑Konventionen für Architektenkampagnen.  
- DSGVO‑konformes Konzept zur Pseudonymisierung und ggf. Verknüpfung von Web-Analytics‑Daten mit CRM‑Leads.

**D. Dashboards & Alerting (müssen vor Go-Live konzipiert und min. als V1 aufgebaut sein)**

1. **Dashboard „Architect Hub – Web“**  
   - Traffic & Engagement nach Markt/Sprache.  
   - Nutzung BIM/CAD, TechDocs, Referenzen.  
   - Funnels: Hub → System/BIM/Referenz → Kontakt/Lead.  

2. **Dashboard „Architect Leads – CRM/HubSpot“**  
   - Anzahl/Qualität Architekten‑Leads.  
   - Quelle (Seiten, Kampagnen, Content-Typen).  
   - Übergabe-Status & Bearbeitungszeiten.

3. **Alerting (mindestens):**  
   - Starker Rückgang von:
     - BIM/CAD-Downloads,  
     - Form Submits im Architektenbereich,  
     - Traffic auf Architekten-Hub.  
   - Tracking-Anomalien: keine Events eines Typs über definierte Zeiträume.

**E. Datenqualitätsmanagement**

- Automatisierte Checks (z. B. via Tag-Manager-/BI-Skripte):  
  - Vollständigkeit von Pflicht‑Parametern (`entity_id`, `content_type`, `target_audience`).  
  - Event-Abdeckung pro Seitentyp.  

- Manuelle, regelmäßige Stichproben (monatlich/vierteljährlich):  
  - Test definierter Journeys (z. B. Referenz → System → BIM → Lead-Formular) inkl. Trackingprüfung.

### 6.3 Governance des Analytics Gate

- **Rollen:**  
  - *Analytics Owner Architect Hub* (z. B. im Digital‑/Marketingteam) – verantwortlich für KPI‑Definition, Tracking‑Plan, Dashboards, Datenqualität.  
  - *Product Owner Architect Hub* – stellt sicher, dass Analytics parallel zu UX/Tech geplant und umgesetzt wird.  
  - *IT/Tagging-Verantwortlicher* – technische Umsetzung Data Layer & Events.

- **Gating-Mechanismus:**  
  - Projektphase „Konzeption“ wird erst abgeschlossen, wenn:
    - KPI‑Framework schriftlich freigegeben,  
    - Tracking‑Plan (Events & Data Layer) spezifiziert,  
    - Dashboard‑Konzept dokumentiert.  
  - Go‑Live wird erst freigegeben, wenn:
    - Kern‑Events technisch implementiert und erfolgreich getestet,  
    - V1 der Dashboards live,  
    - Alerting eingerichtet und getestet ist.

---

## 7. Roadmap & Prioritäten

### Phase 1 – Fundament (0–3 Monate)

- Zielbild & Scope finalisieren (Zielmärkte, Sprachen, Personas).  
- IA für Architect Hub definieren (Hub + 4–5 Grounding Pages).  
- CoreMedia‑Content‑Modell (Content Types & Taxonomien) spezifizieren.  
- DAM‑Anbindung und Systemlandschaft (BIM/CAD, Doku, CRM/HubSpot) klären.  
- **Analytics Gate – Teil 1:** KPI‑Framework & Tracking‑Konzept fixieren.

### Phase 2 – MVP Architect Hub (3–8 Monate)

- Implementierung ArchitectLandingPage + Kerncluster  
  (Planung & Systeme, BIM & CAD, Referenzen, Beratung/Services).  
- Integration vorhandener System-, BIM‑ und Referenzinhalte in neues Modell.  
- Basis-SEO (URL‑Struktur, Title/H‑Struktur, interne Verlinkung) & erste JSON‑LD‑Blöcke.  
- Einführung der wichtigsten Architekten-Formulare (Projektberatung, BIM‑Paket).  
- **Analytics Gate – Teil 2:** Events, Data Layer, Dashboards & Alerts implementieren, Test & Abnahme.

### Phase 3 – Ausbau & Optimierung (9–18 Monate, laufend)

- Ausbau Dokumenten-/Ausschreibungsbereich & Download‑Bundles.  
- Verfeinerung Taxonomien, Personalisierung (z. B. nach Region/Interessen).  
- Ausbau FAQ-/Knowledge‑Base für AI‑Search.  
- A/B‑Tests (Einstiegsnavigation, CTA‑Platzierungen, Gating‑Strategie).  
- Enge Zusammenarbeit mit Vertrieb (Sales Enablement, Schulungen).  
- Kontinuierliche, datenbasierte Optimierung anhand definierter KPIs & Dashboards.

---

## 8. Abschließende Empfehlung des Digital Advisory Boards

Das Schüco Digital Advisory Board empfiehlt:

1. **Aufbau eines international skalierbaren „Architect Hub“** als eigenständigen, klar strukturierten Bereich auf schueco.com – mit Use‑Case‑basierter Navigation, sauberem CoreMedia‑Content‑Modell und starker Verknüpfung von Systemen, BIM/CAD, technischer Doku, Referenzen und Ansprechpartnern.

2. **Konsequente Umsetzung der SEO‑, GEO‑ und AI‑Search‑Prinzipien**: Grounding Pages, strukturierte FAQ‑Blöcke, JSON‑LD und eindeutige Entitäten bilden das Fundament für organische Sichtbarkeit und zukünftige KI‑Use‑Cases.

3. **Integration robuster Lead- und Vertriebsprozesse über HubSpot/CRM**: klar getrennte Formularzwecke, Leadqualifikation, Routing und Nurturing sichern die wirtschaftliche Relevanz des Hubs.

4. **Verankerung eines verbindlichen Analytics Gate** als projektkritisches Element: ohne genehmigtes KPI‑Framework, Tracking‑Plan, implementierte Events, Dashboards und Alerting erfolgt weder Implementierungsfreigabe noch Go‑Live.

Mit dieser Ausgestaltung erfüllt der weiterentwickelte Architektenbereich die Anforderungen der Zielgruppe, stärkt Marke und Sichtbarkeit von Schüco und liefert gleichzeitig messbaren Wert für Leads, Vertrieb und internationale Märkte.

---

# Analytics Gate Ergebnis

Status: **PASSED**

Fehlende Bestandteile:
- Keine
