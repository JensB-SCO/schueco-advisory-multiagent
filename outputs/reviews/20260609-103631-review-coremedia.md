# Expertenreview: coremedia

1. Kernaussage  
Für den Architektenbereich von Schüco sollte ein eigenständiger, klar segmentierter „Architect Experience Hub“ in CoreMedia aufgebaut werden – mit fachlich sauberen Content Types (Produkte, Systeme, Referenzen, BIM/CAD, technische Doku, Events, Personen/Ansprechpartner), einer zielgruppenorientierten Taxonomie (Use Cases, Projektphasen, Gebäudetypen, Regionen), geführten Journeys und AI-Search-fähigen Antwortblöcken. Alles wird SEO-/GEO-optimiert, mit HubSpot-Leadstrecken verknüpft und über definierte KPIs messbar gemacht.

---

2. Chancen  

**2.1 Nutzererlebnis & Conversion**  
- Deutlich schnellere Orientierung für Architekten durch:  
  - klaren Einstieg „Für Architekten“  
  - gefilterte Sichten auf Produkte/Systeme, Referenzen, BIM/CAD, Ausschreibungstexte, Normen, Schulungen  
- Höhere Conversion zu Leads durch:  
  - kontextuelle Formulare (z. B. „Projekt mit Experten besprechen“, „BIM-Paket anfordern“)  
  - personalisierte Empfehlungen („Sie planen … Bürogebäude mit Pfosten-Riegel-Fassade?“ → passende Systeme, BIM-CAD, Referenzen, Ansprechpartner)  

**2.2 Content-Wiederverwendung & Effizienz**  
- Produkt- und Systeminformationen, technische Doku und Referenzen werden einmalig gepflegt und in verschiedenen Architekten-Journeys ausgespielt (CoreMedia-CMS-Stärken).  
- BIM/CAD, Broschüren und Datenblätter über DAM sauber referenziert – keine Dubletten, konsistente Stände.  

**2.3 SEO & GEO**  
- Aufbau eines klaren Themen-Clusters „Architektur & Planung mit Schüco“:  
  - Pillar Pages (z. B. „Schüco Lösungen für Architekten“, „Fassadensysteme für Hochhausprojekte“)  
  - FAQ-Strukturen zu typischen Architektenfragen (Brandschutz, Schallschutz, Nachhaltigkeit, Zertifizierungen, BIM-Workflows).  
- GEO-Fähigkeit durch:  
  - eindeutige Entitäten (Produkte, Systeme, Referenzprojekte, Personen/Ansprechpartner)  
  - zitierfähige Antwortblöcke und FAQ-Abschnitte  
  - JSON-LD für Produkte, FAQs, Organisation, Events/Trainings  
  - Grounding Pages für zentrale Themen (z. B. „BIM mit Schüco“, „Aluminium-Fassadensysteme für Architekten“).  

**2.4 Vertriebs- & Lead-Unterstützung**  
- Qualifizierte Leads durch kontextabhängige Formulare (z. B. „Unterstützung bei technischen Details“, „Projektberatung“).  
- Besseres Routing zu Sales (Region, Projekttyp, Projektphase) über strukturierte Datenerhebung.  
- Segment-spezifische Nurturing-Strecken mit HubSpot (z. B. Early-Stage: Inspiration & Referenzen, Mid-Stage: technische Doku, Late-Stage: direkte Angebots-/Projektanfrage).  

---

3. Risiken  

**3.1 Komplexität & Pflegeaufwand**  
- Gefahr einer zu komplexen Taxonomie (Gebäudetypen, Nutzungstypen, Regionen, Projektphasen etc.), die im Alltag nicht konsequent gepflegt wird.  
- BIM/CAD-Daten, technische Doku und Referenzen sind oft verteilte Datenquellen – ohne klare Ownership droht Veraltung.  

**3.2 Fragmentierte Nutzerführung**  
- Wenn „Architektenbereich“ nur als Marketing-Landingpage aufgebaut wird, aber wesentliche Inhalte noch im restlichen Webauftritt „versteckt“ bleiben, entsteht Bruch in der Journey.  
- Unklare Abgrenzung zu anderen Zielgruppen (Investoren, Verarbeiter) kann zu doppelten Inhaltsstrukturen führen.  

**3.3 Governance & Internationalisierung**  
- Lokale Märkte (Länder-Websites) könnten eigene Architektenstrukturen anlegen, die mit dem globalen Modell kollidieren.  
- Unterschiedliche rechtliche/technische Anforderungen (Normen, Zertifikate) je Land → Risiko von falschen oder unpassenden Dokumenten in bestimmten Märkten.  

**3.4 Analytics & Messbarkeit**  
- Ohne saubere Definitionen von KPIs, Events und Verantwortlichkeiten entsteht zwar „viel Tracking“, aber wenig nutzbare Erkenntnis.  
- Risiko, dass früh definierte KPIs (z. B. „Downloads“) nicht auf echte Business-Ziele (z. B. qualifizierte Projekt-Leads) einzahlen.  

---

4. Anforderungen  

**4.1 Content Types (CoreMedia)**  
Mindestens folgende eigenständige Content Types sollten modelliert bzw. geschärft werden:

1. **Architect Landing / Hub Page**  
   - Zweck: Einstieg für Architekten, Übersicht über alle relevanten Assets.  
   - Felder: Zielgruppen-Fokus, Haupt-Use-Cases, Teaser auf Produktsysteme, Referenzen, BIM/CAD, Ansprechpartner, FAQs, Events.  

2. **Produkt-/System-Content Type** (falls nicht vorhanden: schärfen für Architekten-Sicht)  
   - Technische Kennwerte, Zertifizierungen, Anwendungsbereiche (Fassade, Fenster, Türen, Sonnenschutz, Sicherheit etc.).  
   - Relation zu: BIM/CAD-Paketen, technischen Dokumenten, Referenzen, Ansprechpartnern.  

3. **Referenzprojekt**  
   - Architektonische Beschreibung, Gebäudetyp, Nutzung, Standort, beteiligtes Architekturbüro, Systemlösungen.  
   - Medien: Bilder, Videos, 360°, Pläne (über DAM).  
   - Relationen: verwendete Schüco-Systeme, Ansprechpartner, Downloads.  

4. **BIM/CAD-Paket**  
   - Art: BIM (Revit, ArchiCAD …), 2D/3D-CAD, Detailzeichnungen.  
   - Zuordnung: Produkt/System, Projektphase (Entwurf, Ausführungsplanung), Region (ggf. Norm-Bezug).  
   - Technische Metadaten: Version, Gültigkeit, Sprach-/Ländercode.  

5. **Technische Dokumentation**  
   - Typ: Datenblatt, Prüfzeugnis, Zulassungen, Montageanweisung, Wartungsanleitung.  
   - Verknüpfung zu Produkt/System, Markt/Region, Sprache.  

6. **Person / Ansprechpartner**  
   - Rolle: Architektenberater, Projektmanager, Support.  
   - Zuständigkeiten: Region, Produktschwerpunkte, Zielgruppen.  

7. **Event / Schulung / Webinar**  
   - Fokus: Architektur, Planung, Normen, digitale Planung (BIM).  
   - Structured Data: Event-Schema (Ort, Zeit, Zielgruppe).  

8. **FAQ / Answer Block** (für GEO & AI-Search)  
   - Ein Frage-Antwort-Content Type mit: Frage, kurze zitierfähige Antwort (max. 2–3 Absätze), weiterführende Links.  
   - Kategorisierung nach Themen (BIM, Brandschutz, Nachhaltigkeit, Systemwahl).  

9. **Lead Magnet / Gated Content**  
   - Whitepaper, Planungshandbücher, Detail-Sammlungen, Checklisten.  
   - Verknüpft mit HubSpot-Formularen (Lead-Erfassung).  

**4.2 Taxonomien**  
- **Zielgruppe:** Architekten / Planer (Tag zur Segmentierung).  
- **Gebäudetypen:** Büro, Wohnen, Krankenhaus, Bildung, Hotel, Industrie, Hochhaus, Sonderbau etc.  
- **Projektphase:** Konzept, Vorentwurf, Entwurf, Ausführungsplanung, Ausschreibung, Ausführung.  
- **Anwendungsbereich:** Fassade, Fenster, Türen, Schiebesysteme, Sonnenschutz, Sicherheit, Automation.  
- **Region/Land:** zur Steuerung von Normen, Sprachen, Ansprechpartnern.  
- **Themencluster:** Nachhaltigkeit, Energieeffizienz, Sicherheit, Design, Barrierefreiheit, Brandschutz, Akustik.  

**4.3 Workflows**  
- Redaktions-Workflow pro Content Type mit klaren Rollen:  
  - Erstellung (Fachredaktion / Product Owner),  
  - technische Freigabe (Engineering/Produktmanagement),  
  - juristische/Compliance-Freigabe (wo nötig),  
  - länderspezifische Freigabe (für Normen, Dokumente, Übersetzungen).  
- SLA für Aktualisierung technischer Dokumente, BIM/CAD-Daten und Referenzprojekte.  

**4.4 Wiederverwendung**  
- Referenzen, Produkte, BIM/CAD, technische Doku:  
  - einmalig anlegen, mehrfach ausspielen:  
    - auf Architekten-Hub,  
    - auf Produktdetailseiten,  
    - in Themen-/Grounding-Pages,  
    - in Kampagnen-Landingpages.  
- Konfigurierbare Teaser-Module, die über Taxonomie (z. B. Gebäudetyp: Büro + Thema: Fassadensysteme) automatisch passende Inhalte ziehen.  

**4.5 Internationalisierung**  
- Nutzung von CoreMedia-Language-/Locale-Konzept:  
  - Master-Inhalte (z. B. globaler Architekten-Hub),  
  - lokalisierte Varianten (Land X/Y) mit länderspezifischen Dokumenten, Normen und Ansprechpartnern.  
- Klare Regel: welche Inhalte sind global, welche lokal? (z. B. Produktbeschreibung global, Zulassung/Prüfzeugnis lokal).  

**4.6 DAM-Anbindung**  
- BIM/CAD, Pläne, Renderings, Projektfotos zentral über DAM:  
  - Metadaten-Mapping (Produkt-ID, Gebäudetyp, Region, Projektphase).  
  - Referenzierung im CMS, keine direkten Uploads im CMS für relevante Dateien.  

**4.7 Governance**  
- Rollen & Verantwortlichkeiten:  
  - **Product Owner Architektenhub**: End-to-End-Verantwortung für Zielbild, KPIs und Priorisierung.  
  - **Content Owner** für Produkt/System, Referenzen, BIM/CAD, Doku.  
  - **Local Content Manager** je Region/Land (für Ländervarianten).  
- Richtlinien:  
  - Naming-Konventionen, Taxonomie-Use, Versionierung von Dokumenten.  
  - Review-Zyklen (z. B. alle 6–12 Monate für technische Inhalte).  

**4.8 Analytics & Messbarkeit (Analytics-Prinzipien anwenden)**  
- **Primäre KPIs**  
  - Anzahl qualifizierter Architekten-Leads (formulareingereicht & qualifizierend markiert).  
  - Anzahl projektbezogener Kontaktaufnahmen (z. B. „Projekt besprechen“).  
- **Sekundäre KPIs**  
  - Nutzung von BIM/CAD-Downloads  
  - Nutzung technischer Dokumente & Ausschreibungstexte  
  - Zugriffe auf Referenzprojekte aus dem Architektenbereich  
- **Frühindikatoren**  
  - Interaktionen mit Filtern (Gebäudetyp, Projektphase, Systemkategorie)  
  - Scroll-Tiefe & Verweildauer auf Architekten-Hub & Grounding Pages  
  - Klicks auf Ansprechpartner-Kontaktoptionen  
- **Tracking Events**  
  - Filter-Nutzung  
  - Klicks auf „Download BIM/CAD“, „Download Datenblatt“, „Download Ausschreibungstext“  
  - Formular-Starts/-Abschlüsse (nach Seitentyp und Use Case).  
- **Dashboard & Alerting**  
  - Dashboard „Architect Experience“ (Monats-/Quartalsansicht).  
  - Alerts bei: plötzlich sinkenden BIM/CAD-Downloads oder Formularkonversionen.  
- **Verantwortlichkeiten & Datenqualität**  
  - Verantwortliche im Digital-/Marketingteam für Monitoring & Reporting.  
  - Regelmäßige QA auf Event-Funktion, Funnel- und Konversionsraten.  

**4.9 SEO & GEO-Fähigkeit**  
- **SEO**  
  - Pillar Page „Lösungen für Architekten“ mit Unterseiten zu:  
    - „BIM mit Schüco“,  
    - „Fassadensysteme für Hochhäuser“,  
    - „Nachhaltigkeits- und Zertifizierungsunterstützung“,  
    - „Brandschutzlösungen für Architekten“, etc.  
  - Gute interne Verlinkung:  
    - von Architekten-Hub zu Produkt-, Referenz-, BIM-, FAQ- und Ansprechpartnerseiten und zurück.  
  - Technische SEO: indexierbare Seiten, klare URL-Struktur, H1/H2-Logik.  
- **GEO**  
  - Eindeutige Entitäten:  
    - Produkt/System als eigene Seiten mit strukturierten Daten (Product).  
    - Referenzprojekt mit Projektentität (Location + Organisation + verwendete Systeme).  
  - FAQ-Content Type mit FAQPage-JSON-LD.  
  - Answer-Blocks: kurzer, direkt zitierfähiger Text in den wichtigsten Architektenthemen.  
  - Grounding Pages pro Cluster (z. B. „BIM-Planung mit Schüco“, „Fassadenplanung für Bürogebäude“).  

**4.10 Leads & HubSpot-Anbindung (HubSpot-Prinzipien)**  
- **Formularzweck**  
  - Unterschiedliche Formulare:  
    - „Allgemeine Architektenberatung“,  
    - „Projektunterstützung anfragen“,  
    - „BIM/CAD-Paket anfordern“,  
    - „Schulung/Webinar anmelden“,  
    - „Planungshandbuch/Whitepaper herunterladen“.  
- **Leadqualität**  
  - Pflichtfelder: Rolle (Architekt/Planer), Projekttyp, Projektphase, Region.  
  - Freitextfeld „Projektbeschreibung (optional)“.  
- **Routing**  
  - Automatisches Routing nach Region & Produktschwerpunkt an zuständige Sales-/Architektenberater.  
- **Nurturing & Attribution**  
  - Nurturing-Strecken abgestimmt auf Projektphase.  
  - Kampagnen-/Seiten-Specific UTM-Tags für klare Attribution.  
- **CRM-Übergabe & Sales Enablement**  
  - Automatische Übergabe relevanter Kontextdaten (besuchte Seiten, Downloads) ins CRM.  
  - Bereitstellung von Content-Links für Sales (z. B. schnell teilbare Referenzseiten, Technikseiten).  

---

5. Konkrete Empfehlungen  

1. **Architekten-Hub als eigenständigen Bereich definieren**  
   - URL-Struktur wie: `/architekten/` mit klarer Unterstruktur.  
   - Navigationspunkt „Für Architekten“ prominent integrieren.  

2. **Content-Modell in CoreMedia schärfen**  
   - Die genannten Content Types formal modellieren/prüfen.  
   - Taxonomie-Sets definieren und mit Redaktionsleitfaden ausrollen.  

3. **Zwei zentrale Pilot-Grounding-Pages bauen**  
   - „BIM mit Schüco – für Architekten“  
   - „Fassadensysteme für Büro- und Hochhäuser – Planung mit Schüco“  
   → Mit Answer-Blocks, FAQ-Content Types, JSON-LD und relevanten Downloads.  

4. **Such- & Filtererlebnis verbessern**  
   - Auf dem Architekten-Hub: intelligente Filter für  
     - Gebäudetyp,  
     - Projektphase,  
     - Anwendung (Fassade/Fenster/Türen etc.),  
     - Region.  
   - Besser: dedizierte Architekten-Suche (ggf. AI-Search) mit semantischem Verständnis von Produktnamen, Systemkategorien, Normen.  

5. **BIM/CAD- und Doku-Zugriff bündeln**  
   - Zentrale „BIM/CAD-Bibliothek für Architekten“ mit:  
     - Filtersystem nach Produkt, System, Gebäudetyp, Region, Phase.  
   - Verlinkung von Produktseiten, Referenzen und Architekten-Hub auf diese Bibliothek.  

6. **Referenzprojekte als Leuchtturm-Inhalte nutzen**  
   - Für zentrale Gebäudetypen (Büro, Wohnhochhaus, Bildung etc.) kuratierte Referenzlisten.  
   - Jedes Referenzprojekt verlinkt auf: verwendete Systeme, Downloads, Ansprechpartner.  

7. **Ansprechpartner in Kontexte einbinden**  
   - Auf relevanten Seiten (Systeme, BIM, Grounding Pages) regionale Ansprechpartner mit Kontaktoptionen einblenden.  

8. **Lead-Logik mit HubSpot implementieren**  
   - Konkrete, kontextuelle CTAs einführen:  
     - „Projekt mit Architektenberater besprechen“,  
     - „Individuelle BIM-Unterstützung anfordern“.  
   - Formulardaten strukturiert in HubSpot übergeben, inkl. Seitentyp & Use Case.  

9. **Analytics-Setup nach Analytics-Prinzipien aufsetzen**  
   - Tracking-Plan erstellen, Events definieren, Dashboard „Architect Experience“ in BI-/Webanalytics-Tool anlegen.  
   - Monatliche Review-Session mit Product Owner Architektenhub.  

10. **Governance & Guidelines festlegen**  
   - Redaktionsleitfaden für:  
     - Taxonomie, Content Types, SEO-/GEO-Konventionen,  
     - Update-Zyklen,  
     - Qualitätssicherung.  

---

6. Offene Fragen  

1. **Status quo & Scope**  
   - Welche bestehenden Architekten-Inhalte gibt es bereits (Struktur, Qualität, Sprachen)?  
   - Welche Systeme, Drittsysteme (BIM-Portale, Datenbanken) sind heute angebunden?  

2. **Regionale Unterschiede**  
   - Wie stark unterscheiden sich Architektenbedürfnisse und regulative Anforderungen in den Hauptmärkten (z. B. DACH, UK, Nordics, Mittlerer Osten, Asien)?  
   - Gibt es regionale Architektenprogramme, die integriert werden müssen?  

3. **Vertrieb & Lead-Prozess**  
   - Wie sieht der aktuelle Lead-Prozess für Architekten/Projekte aus (Rollen, Reaktionszeiten, Tools)?  
   - Welche Informationen benötigt Sales minimal, um einen Architekten-Lead effizient zu bearbeiten?  

4. **BIM-/CAD-Strategie**  
   - Wo liegen die Masterdaten für BIM/CAD heute, wer verantwortet sie, wie oft aktualisiert?  
   - Gibt es bestehende Partnerplattformen (z. B. externe BIM-Portale), die integriert werden müssen?  

5. **Technische Rahmenbedingungen CoreMedia**  
   - Welche CoreMedia-Version ist im Einsatz und welche Module (CAEs, Headless-APIs, DAM-Integration)?  
   - Gibt es bereits ein globales Content-Modell und Taxonomie-Framework, an das angeschlossen werden muss?  

6. **Ressourcen & Organisation**  
   - Wer kann die Rolle „Product Owner Architektenhub“ übernehmen?  
   - Welche redaktionellen und technischen Ressourcen stehen für die Anfangsphase und den laufenden Betrieb zur Verfügung?  

Mit der Beantwortung dieser Fragen lässt sich das Konzept in ein konkretes Backlog (Epics/User Stories) für die Weiterentwicklung des Architektenbereichs in CoreMedia überführen.