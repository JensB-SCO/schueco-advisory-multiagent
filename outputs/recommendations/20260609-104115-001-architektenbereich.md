**1. Management-Zusammenfassung**

Der Architektenbereich von schueco.com sollte als klar abgegrenzter, international skalierbarer „Architect Hub“ neu aufgesetzt werden. Kernprinzip: Alles, was Architekten für Planung, Ausschreibung und Projektentscheidung brauchen, ist in einem durchgängigen Flow auffindbar – von Referenz und Systemlösung über BIM/CAD und technische Dokumente bis zum zuständigen Ansprechpartner und Leadstrecke ins CRM.

Das Zielbild ist fachlich, technisch (CoreMedia), SEO-/GEO- und leadseitig konsistent; Analytics bewertet es als „PASSED WITH RISKS“, die sich durch ein verbindliches Analytics Gate im Projekt beheben lassen. Diese Empfehlung beschreibt:

- das Zielbild „Architect Hub“ (Struktur, Content, UX),
- CoreMedia-/SEO-/GEO-/Lead-Grundlagen,
- das **Analytics Gate** (KPI-Framework, Tracking, Dashboards, Verantwortlichkeiten),
- eine pragmatische Roadmap (MVP → Ausbau).

---

## 2. Zielbild: „Schüco Architect Hub“

### 2.1 Positionierung & Nutzen

- Eigenständiger Bereich „Für Architekten & Planer“ mit klarer URL-Struktur (z. B. `/architekten/`, `/en/architects/`).
- Versprechen: „Schüco für Architekten – Systemlösungen, BIM-Daten, technische Dokumente und Beratung für Ihre Gebäudeplanung.“
- Fokus-Ziele:
  - **Nutzer**: „Time-to-Information“ massiv reduzieren.
  - **Business**: Qualifizierte Architekten-Leads früh im Projekt, besser vorqualifiziert, sauber ins CRM übergeben.
  - **SEO/GEO**: Starke Landingpages für Architekten-Intents, AI-Search-fähige Wissensbasis.
  - **Tech**: Wiederverwendbares, internationales CoreMedia-Modell.

### 2.2 Informationsarchitektur (High Level)

**Top-Level „Architect Hub“ mit 4–5 klaren Einstiegen:**

1. **Planung & Systeme**  
   - Systemlösungen für Fassade/Fenster/Türen/Sonnenschutz aus Architektensicht  
   - Normen, Leistungsdaten, Planungsleitfäden

2. **BIM & CAD**  
   - Zentrales BIM/CAD-Center mit Filtern nach Systemfamilie, Format (Revit, IFC, DWG …), Region/Norm, Projektphase

3. **Technische Dokumente & Ausschreibung**  
   - Datenblätter, Prüfzeugnisse, Zulassungen, Ausschreibungstexte, Planerpakete

4. **Referenzen & Inspiration**  
   - Filterbare Referenzdatenbank (Gebäudetyp, Region, System, Nachhaltigkeit, Architekturbüro)

5. **Beratung & Services / Ansprechpartner**  
   - Regionale Architektenberater, Objektmanagement, Schulungen/Webinare, Architektenservices (z. B. Ausschreibungsservice, Bemusterung)

**Prinzipien:**

- Einstiege orientieren sich an **Jobs-to-be-done** (Planen, Detaillieren, Ausschreiben, Inspiration, Beratung) nicht an interner Organisation.
- Konsistente „Next Steps“:  
  - Systemseite → BIM/CAD → technische Doku → Referenzen → Ansprechpartner → Kontakt/Lead.
  - Referenz → verwendete Systeme → BIM/Doku → Kontakt.

---

## 3. CoreMedia-Grundlage: Content Types, Taxonomien, Workflows

### 3.1 Zentrale Content Types (vereinheitlicht über die Reviews)

Mindestens folgende Content Types sollten modelliert oder geschärft werden:

1. **Architect Hub / Landing Page**
   - Slots für: Hero, Use-Case-Kacheln, Teaser „BIM & CAD“, „Technische Dokumente“, „Referenzen“, „Beratung“, FAQ.

2. **Systemlösung (Produkt/System für Architekten)**
   - Felder: Kurzbeschreibung (Architektensicht), Anwendungsbereiche, technische Kennwerte, Normen/Zertifikate, Vorteile, Download-Referenzen.
   - Relationen: BIM/CAD-Pakete, technische Dokumente, Referenzen, Ansprechpartner, FAQs.

3. **BIM/CAD-Asset**
   - Felder: System-ID, Systemfamilie, Format (Revit/IFC/DWG…), Version, Gültigkeitsdatum, Region/Normraum, Sprache.
   - Relationen: Systemlösung(en), ggf. Referenzprojekte.

4. **Technische Dokumentation**
   - Typ: Datenblatt, Prüfzeugnis, Zulassung, Ausschreibungstext, Detailzeichnung, Montageanleitung.
   - Metadaten: System, Region/Norm, Sprache, Version/Gültigkeit.

5. **Referenzprojekt**
   - Felder: Gebäudetyp, Nutzung, Standort/Region, Architekturbüro, Projektbeschreibung, Leistungsmerkmale (z. B. Nachhaltigkeit), Bilder.
   - Relationen: eingesetzte Systeme, BIM/Dokumente (falls freigegeben), Ansprechpartner.

6. **Ansprechpartner / Expert Profile**
   - Felder: Rolle (Architektenberater, technischer Support), Region/Land, Produktschwerpunkte, Kontaktoptionen.
   - Nutzung: modulare Einbindung auf System-, BIM-, Grounding- und Referenzseiten.

7. **FAQ / Answer Block**
   - Felder: Frage, **Kurzantwort** (1–3 Sätze, zitierfähig für AI), Langantwort (optional), Thema, Zielgruppe.
   - Nutzung: auf Hub-, BIM-, Doku-, System- und Service-Seiten.

8. **Service / Tool / Event**
   - z. B. Architektenschulungen, Webinare, Planungstools, Konfiguratoren.
   - Mit Event-/Tool-Metadaten und Verknüpfung zu Architektenzielen.

9. **Lead Magnet / Download-Bundle**
   - z. B. „Planerpaket System XY“ (BIM + Doku + Ausschreibung).
   - Verknüpft mit HubSpot-Formular für qualifizierte Leads.

### 3.2 Taxonomien (vereinheitlicht)

- Zielgruppe: Architekt/Planer (wichtig für Filter, Personalisierung, Analytics).
- Systemfamilie: Fassade, Fenster, Tür, Schiebesysteme, Sonnenschutz, Automation.
- Anwendungsbereich: Neubau/Sanierung, Hochhaus/Büro/Wohnbau/Bildung/Healthcare/Sonderbau.
- Projektphase: Konzept, Entwurf, Ausführungsplanung, Ausschreibung, Ausführung.
- Region/Land/Normraum: DACH, UK, Nordics, MEA, APAC etc.
- Themencluster: BIM, Brandschutz, Schallschutz, Energieeffizienz, Nachhaltigkeit/Zertifizierung, Barrierefreiheit, Sicherheit.

### 3.3 Workflows & Governance

- **Owner „Architect Hub“ (Product Owner)**:  
  - Verantwortlich für Zielbild, Priorisierung, KPIs und kontinuierliche Optimierung.
- **Content Owner je Bereich**:
  - Systeme/Technik (Produktmanagement/Engineering),
  - BIM/CAD (BIM-Teams),
  - Technische Dokumente (Engineering, Legal, Qualität),
  - Referenzen (Marketing/Regionen),
  - FAQs/Wissensblöcke (Tech Support + Marketing),
  - Ansprechpartner (Sales/HR/Regionen).
- **Freigabe-Workflows**:
  - Erstellung → technische Freigabe → juristische/Compliance-Freigabe (falls nötig) → Brand/UX-Freigabe → Publikation.
  - Pflicht: Versionierung und Gültigkeit bei BIM/CAD und technischen Dokus.

---

## 4. SEO- und GEO-/AI-Search-Fähigkeit

### 4.1 Suchintentionen & Grounding Pages

Auf Basis der Reviews ergeben sich stabile Intents; pro Intent eine Grounding Page:

1. **„Schüco für Architekten“** (`/architekten/`)
   - Überblick, Nutzen, Einstiege in alle Cluster, FAQs „Allgemeine Zusammenarbeit, Services“.

2. **„BIM & CAD für Architekten“** (`/architekten/bim-cad/`)
   - Erklärungen (Formate, Tools), zentraler Filterzugriff, FAQs zur Nutzung/Aktualität.

3. **„Technische Dokumente & Ausschreibung“** (`/architekten/ausschreibung/`)
   - Datenblätter, Ausschreibungstexte, Nachweise, Bundles; FAQs zu Normen, Haftung, Stand.

4. **„Referenzen für Architekten“** (`/architekten/referenzen/`)
   - Filterbare Projektübersicht, erklärende Intro-Texte; FAQ „Wie nutze ich Referenzen in Ausschreibungen?“.

5. **„Services & Beratung für Architekten“** (`/architekten/beratung/`)
   - Übersicht Architekturservices, Ansprechpartner, Events/Webinare; FAQ „Wie läuft Projektberatung ab?“.

Optional weitere Grounding Pages z. B. zu „Nachhaltigkeit & Zertifizierungen“, „Fassadensysteme für Hochhäuser“.

### 4.2 Strukturierte Daten & Entitäten (GEO-Prinzipien)

- Global:
  - `Organization` (Schüco), `BreadcrumbList`.
- Pro Content Type:
  - Systeme: `Product` / `ProductModel`.
  - Referenzen: `Project`/`Place` + `ImageObject`.
  - BIM/CAD & Doku: `CreativeWork` / `Dataset`.
  - FAQs: `FAQPage`.
  - Ansprechpartner: `Person` / `ContactPoint`.
  - Events/Schulungen: `Event`.

**Entitäten & IDs**:

- Eindeutige IDs für:
  - Systeme, Referenzprojekte, BIM/CAD-Pakete, Dokumente, FAQ-Einträge, Ansprechpartner.
- Diese IDs werden:
  - im Markup (Data-Attribute, JSON-LD),
  - im Data Layer für Analytics
  - und in internen APIs verwendet → Basis für AI-Suche und Auswertungen.

### 4.3 Interne Verlinkung

- Produkt/Systemseiten:
  - Blöcke „Für Architekten“ mit Links auf BIM, Doku, Ausschreibung, Referenzen, Beratung.
- Architekten-Hub:
  - verlinkt systematisch in Systemfamilien, Referenzcluster, BIM-Center.
- Referenzen:
  - verlinken zurück auf verwendete Systeme, ggf. direkt auf BIM/Doku und Ansprechpartner.

---

## 5. Lead & Vertrieb: HubSpot-/CRM-Integration

### 5.1 Lead-Touchpoints & Formularzwecke

Kernformulare (alle mit klar definiertem Zweck, Routing und Feldset):

1. **Projektberatung anfragen**
   - High-Intent, primary Sales-Lead (SQL/MQL).
2. **Kontakt Architektenberater / Rückruf**
   - Für frühere Phasen oder technische Fragen.
3. **BIM-/Ausschreibungs-Paket für Projekt anfordern**
   - Starker Intent, kombiniert mit Projektkontext.
4. **Architekten-Newsletter / Event-/Webinar-Anmeldung**
   - Nurturing-Einstieg.

**Pflichtfelder zur Qualifizierung:**

- Rolle: Architekt, Fachplaner, Student, Investor etc.
- Projekttyp / Gebäudetyp.
- Projektphase (Konzept, Entwurf, Ausführungsplanung, Ausschreibung, Ausführung).
- Land/Region.
- Grobe Projektgröße (Bandbreiten).

### 5.2 Routing, Scoring, Nurturing

- **Routing**:
  - nach Region/Land,
  - ggf. nach Projektgröße/Segment (z. B. Großprojekte),
  - nach Systemsparte (Fassade/Fenster/Tür…).
- **Lead Scoring**:
  - Profil: Rolle, Bürogröße, Region.
  - Verhalten: BIM-/CAD-Downloads, Doku-Downloads, Nutzung Tools, wiederkehrende Besuche, Referenz-Interaktionen.
- **Nurturing**:
  - Frühe Phasen: Inspiration & Systemübersichten, Referenzen.
  - Späte Phasen/Ausschreibung: Detaillösungen, Ausschreibungstexte, normative Updates, persönliche Beratung.

---

## 6. **Analytics Gate** (verbindlich)

Die Expertenbewertung ist „PASSED WITH RISKS“. Diese Empfehlung ist nur tragfähig, wenn ein **Analytics Gate** als expliziter Projektbaustein definiert, beauftragt und vor Umsetzung abgeschlossen wird.

### 6.1 KPI-Framework (muss vor UX/Implementierung stehen)

**Primäre KPI (eine verbindlich wählen, Empfehlung):**

- **Anzahl qualifizierter Architekten-Leads pro Monat** aus dem Architektenbereich  
  (definiert als: Rolle = Architekt/Planer + projektbezogene Angaben + akzeptiertes Routing an Vertrieb).

Optional ergänzend, falls CRM-fähig:

- Anzahl architekturbasierter Projektanbahnungen/Opportunities pro Quartal, die ihren Erstkontakt im Architektenbereich hatten.

**Sekundäre KPIs:**

- Nutzung technischer Inhalte:
  - BIM/CAD-Downloads (Unique User, Downloads nach System/Land).
  - Downloads technischer Dokumente und Ausschreibungstexte.
- Nutzung Referenzen:
  - Referenzdetailansichten, Filterverwendung, Klicks auf Projektkontakte.
- Nutzung Kontakt/Service:
  - Klicks auf Ansprechpartner, Projektberatung, Schulungsanmeldungen.
- Engagement:
  - Sessions & Verweildauer im Architektenbereich, Seiten/Tiefe pro Session, Wiederkehrerrate.

**Frühindikatoren:**

- Sessions von Architekten mit mehrfachen BIM/CAD-/Doku-Interaktionen ohne Lead.
- Abbruchraten in Formularen (Form Start vs. Submit).
- Nutzung der internen Suche im Architektenbereich (Häufigkeit und Zero-Result-Rate für Begriffe wie „BIM“, „Ausschreibungstext“, „Brandschutz“).

**Verbindlich zu klären (Gate-Kriterium):**

1. Offizielle „North Star“-KPI für den Architektenbereich (oben vorgeschlagene primäre KPI).
2. Definition „qualifizierter Architekten-Lead“ inkl. obligatorischer CRM-Felder.

### 6.2 Tracking-Konzept & Data Layer (vor Design/Dev)

**Data Layer – zentrale Felder (mindestens):**

- `page_type`: `architect_landing`, `architect_system_detail`, `architect_bim_center`, `architect_reference_detail`, `architect_faq`, etc.
- `target_audience`: `"architect"` / `"fabricator"` / …
- `content_type`: `system`, `reference`, `bim_asset`, `technical_document`, `faq`, `contact_person`, `service`, `event`.
- `entity_id`, `entity_name`: eindeutige IDs für Systeme, Projekte, BIM-Assets, Dokumente, FAQs, Personen.
- `taxonomy`: Gebäudetyp, Planungsphase, Systemfamilie, Thema.
- `geo_region`, `country`, `language`.

**Kern-Events (vereinheitlicht über die Reviews):**

- `architect_hub_view`
- `architect_filter_use` (Parameter: Filtertyp, Werte)
- `architect_bim_download` (System, Format, Region, Projektphase)
- `architect_document_download` (Dokumenttyp, System, Region)
- `architect_reference_view` / `architect_reference_interaction` (Filter, Klicks)
- `architect_contact_click` (Kontext: System, BIM, Referenz, Hub)
- `architect_form_view` / `architect_form_start` / `architect_form_submit`  
  (Form Purpose, Lead Segment, Projektphase, Region)
- `architect_internal_search_use` (Suchbegriff, Trefferanzahl, Folgeklick ja/nein)

**Gate-Kriterium:**

- Ein **abgestimmter, dokumentierter Tracking-Plan** existiert, der:
  - pro Seitentyp Use-Case, KPIs, Events, Parameter, Trigger beschreibt,
  - mit CoreMedia-Content Types & Taxonomien abgeglichen ist,
  - von IT/Analytics/Marketing freigegeben wurde.

Ohne diesen Plan kein Development-Start für den Architektenbereich.

### 6.3 Dashboards, Monitoring & Alerting

**Pflicht-Dashboards (Go-Live-Ready):**

1. **„Architect Web Performance“-Dashboard**
   - Traffic & Engagement im Architektenbereich (Segmentierung nach Markt, Sprache).
   - BIM/CAD- und Doku-Nutzung.
   - Funnel „Einstieg → System/BIM/Doku/Referenz → Kontakt/Lead“.

2. **„Architect Leads & CRM“-Dashboard (HubSpot/CRM)**
   - Anzahl & Qualität der Architekten-Leads (MQL/SQL).
   - Leadquellen (Seiten, Content-Typen, Kampagnen).
   - Durchlaufzeiten im Vertrieb (SLA-Einhaltung).

**Alerting (Mindest-Set):**

- Einbruch > X % (z. B. 30 %) in:
  - Form Submits im Architektenbereich,
  - BIM/CAD-Downloads,
  - Traffic auf `/architekten/`.
- Tracking-Anomalien:
  - Keine Events eines bestimmten Typs für > X Stunden.
  - Auffällige Sprünge bei 404 im Architektenpfad.

**Verantwortlichkeiten:**

- **Analytics-Owner Architektenbereich** (im Digital-/Marketingteam):
  - Verantwortlich für KPIs, Dashboards, Data Quality, Quartalsreviews.
- Definierte Eskalationswege bei Alerts (technisch vs. fachlich).

### 6.4 Datenqualität & Governance (laufender Betrieb)

- Automatisierte Checks:
  - Event-Abdeckung auf definierten Templates.
  - Pflicht-Parameter (`entity_id`, `content_type`, `country`) befüllt.
- Regelmäßige Stichproben:
  - z. B. monatlich kritische Journeys (BIM-Download → Formular).

---

## 7. Roadmap & Umsetzungsvorgehen

### Phase 0 – Alignment & Analytics Gate (4–6 Wochen)

- Cross-funktionaler Workshop (Marketing Architektur, Vertrieb, Produktmanagement, IT/CoreMedia, Analytics, HubSpot).
- Festlegen:
  - North-Star-KPI, Definition „qualifizierter Architekten-Lead“,
  - Zielmärkte/Sprachen für MVP,
  - Rollen (PO Architektenhub, Content Owner, Analytics-Owner).
- Erstellen und Abnahme:
  - KPI-Framework,
  - Tracking-Plan/Data Layer-Spezifikation,
  - grobes Content-Modell & Taxonomien in CoreMedia,
  - HubSpot-Formular- und Routing-Konzept.
- **Freigabe Analytics Gate** als formaler Meilenstein.

### Phase 1 – MVP „Architect Hub“ (3–4 Monate)

Scope MVP:

- Architekten-Landing `/architekten/`.
- Mindestens:
  - Basis-Systemseiten mit Architektenabschnitt,
  - einfaches BIM/CAD-Listing (Top-Systeme, Kernformate),
  - Referenzen-Listing + 3–5 zentrale Referenzdetailseiten,
  - Seite „Beratung & Ansprechpartner“ mit regionalen Kontakten,
  - 1–2 Grounding Pages (z. B. „BIM & CAD“ + „Ausschreibung & technische Dokumente“),
  - 2–3 typische Architekten-Formulare (Projektberatung, allgemeine Anfrage, Event/Newsletter),
  - Basistracking & 2 Dashboards.

Ziel: Schnell nutzbarer Mehrwert + Datenbasis für Optimierung.

### Phase 2 – Ausbau & Internationalisierung (6–12 Monate)

- Erweiterte Filter / Suche (Semantik für Produkttypen, Normen).
- Vollständige BIM/CAD-Bibliothek mit Integration DAM/BIM-System.
- Ausbau der technischen Doku-/Ausschreibungsbibliothek.
- Vollständige Referenzdatenbank (inkl. globaler Leuchtturmprojekte).
- Lokalisierte Varianten (wichtige Kernmärkte) mit landesspezifischen Normen/Dokumenten/Ansprechpartnern.
- JSON-LD-Rollout für alle relevanten Content-Typen.
- Ausbau HubSpot-Nurturing & Lead-Scoring.

### Phase 3 – AI-Search & kontinuierliche Optimierung (laufend)

- Nutzung der FAQ- und Answer-Blöcke für AI-gestützte Suche/Q&A auf der Website.
- Auswertung der Onsite-Suche und FAQ-Nutzung zur Content-Optimierung.
- Regelmäßige Quartalsreviews:
  - KPI-Entwicklung,
  - Content-Gaps (z. B. häufige, unbeantwortete Suchbegriffe),
  - Anpassungen in IA, Content, Leadprozessen.

---

## 8. Entscheidungsvorlage fürs Management

**Zu entscheiden / freizugeben:**

1. **Zielbild**: Aufbau eines internationalen „Architect Hub“ als eigenständigen, strukturierten Bereich mit klaren Use-Case-Einstiegen, statt punktueller Verbesserungen im bestehenden Auftritt.
2. **North-Star-KPI**: Offizielle Festlegung auf „qualifizierte Architekten-Leads pro Monat“ (inkl. Definition „qualifiziert“).
3. **Analytics Gate**:  
   - formale Verankerung eines verpflichtenden Analytics-Gates vor Start der Implementierung,
   - Ressourcen für einen dedizierten Analytics-Workstream (Tracking-Plan, Dashboards, QA).
4. **Rollen**:
   - Benennung eines **Product Owner Architektenhub**,
   - klar definierte Content Owner für Systeme, BIM/CAD, technische Doku, Referenzen, FAQs, Ansprechpartner,
   - Analytics-Owner.
5. **Budget & Scope** für Phase 0 + MVP (Phase 1) inkl. UX/Content/IT/Analytics/HubSpot-Anpassungen.

Mit dieser Entscheidung und einem sauber durchgeführten Analytics Gate lässt sich der Architektenbereich gezielt so weiterentwickeln, dass er:

- Architekten schnell und international konsistent zu relevanten Informationen führt,
- technische Inhalte, BIM/CAD, Referenzen und Ansprechpartner durchgängig verknüpft,
- SEO- und GEO-/AI-Search-Fähigkeit sicherstellt,
- qualitativ hochwertige Leads generiert und vertrieblich nutzbar macht,
- in CoreMedia, DAM und HubSpot sauber integrierbar und messbar betrieben werden kann.

---

# Analytics Gate Ergebnis

Status: **PASSED**

Fehlende Bestandteile:
- Keine
