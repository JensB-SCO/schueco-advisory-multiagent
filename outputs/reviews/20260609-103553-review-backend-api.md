# Expertenreview: backend_api

1. Kernaussage  
Die Weiterentwicklung des Architektenbereichs sollte als eigenständiger, AI-Search- und SEO-optimierter „Architect Hub“ umgesetzt werden: ein strukturierter, API-gestützter Bereich in CoreMedia, der Produkt-/Systeminfos, technische Dokumentation, BIM/CAD, Referenzen und Ansprechpartner über klar definierte Content-Typen, Taxonomien und Such-/Filterfunktionen zusammenführt, messbar macht und über Leads/CRM (z.B. HubSpot) mit Vertrieb verknüpft.

---

2. Chancen  

- **Bessere Informationsauffindbarkeit für Architekten**  
  - Fachlogische Struktur (Phasen des Planungsprozesses: Entwurf, Ausschreibung, Ausführung).  
  - Facettensuche nach System, Anwendung (Fassade, Fenster, Tür), Land/Norm, Leistungsmerkmalen.  
  - Schneller Zugriff auf CAD/BIM, Detailzeichnungen, Ausschreibungstexte, Zulassungen.

- **Stärkere Positionierung von Schüco als Partner für Architekten**  
  - Kuratierte „Architect Journeys“ (Guides, How-tos, Best Practices).  
  - Referenzprojekte als Inspiration + Nachweis technischer Kompetenz.  
  - Fachartikel, Whitepaper, Webinare, CPD/Weiterbildung.

- **SEO & GEO-Synergien**  
  - Klar getrennte und indexierbare Seitentypen: „BIM/CAD Download“, „Referenzprojekt“, „Systemdetail“, „FAQ für Architekten“.  
  - Strukturierte Daten (JSON-LD) für Produkte, Projekte, FAQs und Ansprechpartner.  
  - Bessere interne Verlinkung von Produkt- zu Architekteninhalten und umgekehrt.  
  - Vorbereitung für AI-Search: eindeutige Entitäten (Systemnamen, Projekttypen, Regionen).

- **Leadgenerierung & Sales Enablement**  
  - Lead-Kapitur an den „wertvollsten“ Stellen: Download-Pakete, Projektberatung, Objekt-Support.  
  - Qualifizierte Leads dank spezifischer Formulare (z.B. „Projektanfrage Fassade > 1.000 m²“).  
  - Übergabe an CRM (z.B. HubSpot) mit Projektkontext (Typ, Region, Ausführungszeitraum).  
  - Besseres Vertriebs-Enablement: standardisierte Dokumente, Checklisten, Argumentationshilfen.

- **Skalierbarkeit & Governance in CoreMedia**  
  - Wiederverwendbare Content-Typen für internationale Märkte.  
  - Lokalisierung von Normen, Ansprechpartnern, Sprachen über Taxonomien.  
  - Zentrale Pflege technischer Dokumente mit Wiederverwendung in mehreren Kontexten.

---

3. Risiken  

- **Komplexität der Informationsarchitektur**  
  - Zu viele Filter, Content-Typen und Navigationspfade können Nutzer überfordern.  
  - Inkonsistente Verwendung von Systembezeichnungen, Normen, Regionen schwächt AI-Search-Fähigkeit.

- **Daten- und Schnittstellenabhängigkeiten**  
  - BIM/CAD-Daten, technische Dokumente und Referenzen liegen möglicherweise in separaten Systemen (DAM, PIM, externen Portalen).  
  - Fehlende oder instabile APIs können zu Inkonsistenzen/fehlenden Daten führen.

- **Unklare Verantwortlichkeiten**  
  - Wer pflegt welche Inhalte (Marketing vs. Technik vs. Landesgesellschaft)?  
  - Gefahr veralteter Dokumente (Normen, Zulassungen) ohne klaren Governance-Prozess.

- **SEO-/Tracking-Fehlkonfiguration**  
  - Duplicate Content durch parallele Produkt- und Architekten-Strukturen.  
  - Fehlende Events/KPIs führen zu „Blindflug“ bei Optimierung.

- **Überfrachtete Leadprozesse**  
  - Zu aggressive Gating-Strategien (alles nur nach Login/Leadformular) schrecken Architekten ab.  
  - Unzureichende Qualifizierung und Routing führen zu Frustration im Vertrieb.

---

4. Anforderungen  

4.1 Fachlich / UX  
- **Zielgruppen-Fokus „Architekten“**  
  - Klare Einstiegs-Seite „Für Architekten“ mit:  
    - Einstieg nach „Aufgabe“ (Planen, Ausschreiben, Ausführen, Sanieren).  
    - Einstieg nach „Gebäudetyp“ (Wohnbau, Büro, Öffentliche Gebäude, Sonderbauten).  
    - Einstieg nach „System/Werkstoff“ (Aluminium, Kunststoff, Fassade, Fenster, Tür, Sonnenschutz).  

- **Inhaltsbereiche**  
  1. **Technische Informationen**  
     - Systemseiten mit: Leistungsmerkmalen, Normen/Zulassungen, Detaillösungen, Anschlussdetails.  
     - Ausschreibungstexte, Detailzeichnungen, Prüfberichte.  
  2. **BIM/CAD-Daten**  
     - Downloadbereich mit Filtern nach System, CAD-Format, BIM-Standard, Region.  
     - Option „Projekt-Paket anfordern“ (Sammel-Download + Beratung).  
  3. **Referenzprojekte**  
     - Filter nach Gebäudetyp, Region, System, Architekturbüro, Nachhaltigkeitslabels.  
     - Verknüpfung zu relevanten Systemseiten und Downloads.  
  4. **Ansprechpartner & Services**  
     - Regionale/landesspezifische Architektenberater und technische Berater.  
     - Services: statische Vorbemessung, Pflichtenhefte, Workshops, Schulungen.  
  5. **Wissen & Inspiration**  
     - Fachartikel, Whitepaper, Webinare, Tutorials, CPD/Weiterbildung.  
     - FAQs für typische Architektenfragen (z.B. „Wie integriere ich Schüco in Revit?“).

- **Such- und Filterfunktionen**  
  - Globale „Profi-Suche“ mit Filtern für Content-Typ (Systeminfo, BIM/CAD, Referenz, FAQ).  
  - Semantische Suche mit Synonymen (z.B. „Pfosten-Riegel“, „Curtain Wall“).

4.2 Content / CoreMedia-spezifisch  
- **Content-Typen** (mindestens)  
  - `Architect-Landing`  
  - `System-Technical-Page` (verknüpft mit Produkt/Systementität)  
  - `BIM-CAD-Asset` (Metadaten: System, Format, Version, Norm, Land)  
  - `Reference-Project` (Metadaten: Typ, Region, Architekt, Produkte, Zertifizierungen)  
  - `Expert-Profile` (Ansprechpartner)  
  - `Service-Offer` (Beratung, Schulungen etc.)  
  - `FAQ`  
  - `Download-Bundle` (z.B. „Planerpaket“ je System oder Projektphase)

- **Taxonomien**  
  - Gebäudetyp, Region/Land, Planungsphase, Systemfamilie, Norm/Standard, Leistungsmerkmal, Sprachversion.  
  - Einheitliche IDs für Systeme/Produkte (Entitäten), um AI-Search und Wiederverwendung zu ermöglichen.

- **Workflows & Governance**  
  - Prüf- und Freigabe-Workflows insbesondere für technische Inhalte und Normangaben.  
  - Verantwortlichkeiten:  
    - Technik: Inhaltliche Korrektheit.  
    - Marketing/Brand: Darstellung, Storytelling, Bildwelt.  
    - Lokale Einheiten: Lokale Normen, Ansprechpartner, Sprache.

- **DAM-Anbindung**  
  - Zentrale Ablage von BIM/CAD, Zeichnungen, Referenzbildern im DAM, mit sauberer Metadatenstruktur.  
  - Nutzung von DAM-Referenzen in Content-Typen (keine Duplikate in CoreMedia).

4.3 SEO & GEO  
- **SEO-Prinzipien**  
  - Klare URL-Struktur:  
    - `/architekten/` (Landing)  
    - `/architekten/systeme/<system-name>/`  
    - `/architekten/bim-cad/<system-name>/`  
    - `/architekten/referenzen/<projekt-name>/`  
  - Meta-Titel/Description pro Seitentyp, H1-Struktur und interne Verlinkung (z.B. von Referenz zu Systemseite zu Download).  
  - Indexierbare Listing-Seiten mit SEO-Texten, aber facettierte Filter per Parameter, die Suchmaschinen-gerecht gehandhabt werden (Canonical, Noindex für irrelevante Kombis).

- **GEO-/AI-Search-Fähigkeit**  
  - Eindeutige Entitäten:  
    - System-ID, Projekt-ID, Architektenbüro-ID, Ansprechpartner-ID.  
  - JSON-LD:  
    - `Product`/`ProductModel` für Systeme.  
    - `Project`/`Place` für Referenzen (inkl. Geo-Koordinaten).  
    - `FAQPage` für FAQ-Bereiche.  
    - `Person`/`Organization` für Ansprechpartner/Büros.  
  - FAQ-Strukturen: klare Q&A-Blöcke für typische Architektenfragen, maschinenlesbar.

4.4 Analytics & Leadprozesse  
- **KPIs gemäß Analytics-Prinzipien**  
  - Primäre KPIs:  
    - Lead-Anfragen aus Architektenbereich (qualifizierte Projekt-Leads).  
    - Nutzung BIM/CAD-Downloads.  
  - Sekundäre KPIs:  
    - Verweildauer, Tiefe des Seitenpfads, Rückkehrquote.  
    - Nutzung Such-/Filterfunktionen.  
  - Frühindikatoren:  
    - Klicks auf „Projektberatung anfragen“, „Kontakt Architektenberater“, „Planerpaket downloaden“.  
    - Interaktionen mit Referenzprojekten (Sharing, Merklisten).

- **Tracking Events**  
  - Suchanfragen (Suchbegriffe, Filterkombinationen).  
  - Downloads (Typ, Format, System, Land).  
  - Formularabschlüsse (Formulartyp, Projektparameter).  
  - Klicks von Produktseiten in den Architektenbereich und zurück (Cross-Navigation).

- **Dashboard & Alerting**  
  - BI-/Analytics-Dashboard für Architektenbereich (Traffic, Funnels, Downloads, Leads).  
  - Alerts bei:  
    - Signifikantem Rückgang von BIM/CAD-Downloads.  
    - Ausfall bestimmter Formulare/Schnittstellen (Lead-Übernahme).  
    - Starke Zunahme bestimmter Suchen ohne Treffer („No Result“-Monitoring).

- **HubSpot-/CRM-Integration**  
  - Formulare mit klar definiertem Zweck:  
    - Projektanfrage, Beratungstermin, Download-Paket-Anforderung, Newsletter/Updates.  
  - Leadqualität: Pflichtfelder zu Projekttyp, Projektgröße, Zeithorizont, Land.  
  - Routing:  
    - Übergabe an zuständigen Architektenberater nach Region/Land/System.  
  - Nurturing:  
    - Automatisierte Workflows (z.B. nach BIM/CAD-Download Einladung zu Webinar/Guide).  
  - Sales Enablement:  
    - Templates und Inhalte zum Nachfassen (Mail-Vorlagen, Präsentationen, Case-Studies).

4.5 Technik, API & Betrieb  
- **APIs & Datenquellen**  
  - Schnittstelle zu:  
    - PIM/Systemdaten (technische Parameter, Normen).  
    - BIM/CAD-Repositorium / DAM.  
    - CRM/HubSpot (Formular- & Lead-Daten).  
  - Möglichst einheitliche, dokumentierte REST/GraphQL-APIs mit Versionierung.  
  - Caching-Layer für häufig genutzte technische Daten und BIM/CAD-Listings.

- **Skalierung & Performance**  
  - Serverseitiges Rendering und Caching für high-traffic Listing-/Detailseiten.  
  - CDN-Auslieferung für BIM/CAD-Assets, Bilder, Downloads.  
  - Performance-Monitoring (LCP, FID, CLS), da Architekten oft große Medien/Assets anfragen.

- **Security & Zugriff**  
  - Kein unnötiges Gating von Basismaterial (SEO-relevante Inhalte müssen frei zugänglich sein).  
  - Gated nur für: Bundles, spezialisierte Tools, Projektberatung.  
  - DSGVO-konforme Formulare, Consent Management, sichere Übertragung (TLS), Bot-Protection für Formulare.

---

5. Konkrete Empfehlungen  

- **1. Architekten-Hub als klar abgegrenzten Bereich aufbauen**  
  - Eigene Hauptnavigation „Für Architekten“ mit fokussierter IA und Landingpage.  
  - Unterstruktur nach: „Systeme & Technik“, „BIM/CAD“, „Referenzen“, „Services & Ansprechpartner“, „Wissen & FAQs“.

- **2. Content-Typen & Taxonomien in CoreMedia definieren und global ausrollen**  
  - Zuerst ein CoreMedia-Content-Modell für Architektenbereich erstellen.  
  - Taxonomie-Workshop mit Produktmanagement, Marketing, IT zur Definition von Systemfamilien, Normklassen, Gebäudetypen, Planungsphasen.  
  - Governance-Board etablieren, das Benennungen und Entitäten freigibt.

- **3. BIM/CAD- und Systemdaten professionell integrieren**  
  - API- oder Connector-Lösung zum bestehenden BIM/CAD-Portal/DAM aufsetzen.  
  - Im Architektenbereich nicht duplizieren, sondern referenzieren – mit sauberem Metadaten-Mapping.  
  - „Sammel-Download“ und „Projekt-Pakete“ anbieten, mit leichtgewichtiger Lead-Erfassung.

- **4. Such- & Filtererlebnis optimieren**  
  - Eine dedizierte „Planer-Suche“ implementieren, die Systeminfos, BIM/CAD, Referenzen und FAQs durchsucht.  
  - Log-Analyse und fortlaufende Optimierung der Suchsynonyme und Facetten.  

- **5. SEO- und GEO-Optimierung von Anfang an mitplanen**  
  - Für jeden Content-Typ SEO-Templates definieren (Meta, H-Struktur, Structured Data).  
  - FAQ-Blöcke standardisiert als FAQPage/FAQ-Schema ausspielen.  
  - Projekt- und Systemseiten mit JSON-LD (Product/Project/Place) anreichern.

- **6. Leadprozesse konkret ausarbeiten und mit Vertrieb abstimmen**  
  - Pro Kontaktpunkt definieren: Zweck, Pflichtfelder, Lead-Scoring-Logik.  
  - Routing-Regeln nach Region/System im CRM abbilden.  
  - Gemeinsame Service-Level-Agreements (SLA) zur Bearbeitung von Architekten-Leads.

- **7. Analytics-Setup als Projektbestandteil verankern**  
  - Noch vor dem Go-Live KPIs, Events, Dashboards und Alerts nach Analytics-Prinzipien definieren.  
  - Regelmäßige Reviews (z.B. quartalsweise) mit Fachbereichen, um Inhalte und Features datenbasiert zu optimieren.

- **8. Schrittweise, MVP-orientierte Umsetzung**  
  - MVP:  
    - Architekten-Landing, Basis-Systemseiten, BIM/CAD-Zugriff, Referenzen-Listing, ein einfaches Kontakt/Projekt-Formular, Basistracking.  
  - Phase 2:  
    - Erweiterte Filter/Suche, Download-Bundles, FAQs, JSON-LD, erweiterte Analytics & Nurturing.  
  - Phase 3:  
    - Personalisierte Empfehlungen (z.B. basierend auf Region/Interesse), Integration weiterer Tools (Konfiguratoren, Berechnungstools).

---

6. Offene Fragen  

- **Zielbild & Scope**  
  - Welche Märkte/Sprachen sollen in der ersten Ausbaustufe des Architektenbereichs enthalten sein?  
  - Gibt es bestehende Portale/Tools speziell für Architekten, die integriert oder abgelöst werden sollen?

- **Systemlandschaft & Datenquellen**  
  - Wo liegen heute die „Single Sources of Truth“ für: System-/Produktdaten, BIM/CAD, Referenzprojekte, Ansprechpartner?  
  - Welche APIs/Integrationsmöglichkeiten bestehen bereits (PIM, DAM, CRM, ggf. BIM-Portal)?

- **Rollen & Governance**  
  - Welche Fachbereiche übernehmen Eigentümerschaft für:  
    - Technische Inhalte.  
    - Architekten-spezifisches Marketing/Wissen.  
    - Referenzprojekte.  
    - BIM/CAD-Content.  
  - Gibt es bereits etablierte Freigabeprozesse, die in CoreMedia-Workflows gespiegelt werden sollen?

- **Leadstrategie & Vertrieb**  
  - Welche Leaddefinitionen und -qualitätskriterien gelten unternehmensweit, und müssen angepasst werden (z.B. für Projekt-Leads von Architekten)?  
  - Wie ist die aktuelle Anbindung zu HubSpot/CRM, und in welchen Märkten wird welches System genutzt?

- **Technische Rahmenbedingungen**  
  - Welche CoreMedia-Version und welche bestehenden Module/Erweiterungen sind im Einsatz (z.B. Search, Personalization)?  
  - Welche Performance- und Verfügbarkeitsanforderungen gibt es (z.B. für internationale Zugriffe auf große BIM/CAD-Dateien)?

- **Compliance & Rechtliches**  
  - Gibt es besondere Anforderungen zu Dokumentationspflicht, Archivierung (z.B. bei Prüfberichten, Normangaben)?  
  - Gibt es länderspezifische Restriktionen bei der Darstellung von Projekten/Kundenreferenzen?

Die Antworten auf diese Fragen sollten in einem kurzen, cross-funktionalen Workshop (IT, Marketing, Technik, Vertrieb) geklärt und in einem Lösungs- und Integrationskonzept für den Architekten-Hub konkretisiert werden.