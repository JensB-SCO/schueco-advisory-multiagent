from __future__ import annotations

from pathlib import Path
import re

from src.task_context import parse_task_context


ROLE_FOCUS: dict[str, tuple[str, ...]] = {
    "analytics": (
        "Optionale Messziele und Erfolgskennzahlen eindeutig abgrenzen.",
        "Tracking nur bei ausdruecklicher Beauftragung und Freigabe vorsehen.",
    ),
    "architecture": (
        "Systemgrenzen, Datenfluss, Hosting und Integrationsverantwortung festlegen.",
        "Abhaengigkeiten zu CoreMedia, Azure, Keycloak und API dokumentieren.",
    ),
    "backend_api": (
        "API-Vertrag, Fehlerfaelle, Pagination und Filtersemantik spezifizieren.",
        "OAuth/OpenID Connect, Rollen und Token-Validierung konkretisieren.",
    ),
    "coremedia": (
        "Content-Typ, Preview, Vorfilter und konfigurierbare Parameter definieren.",
        "Fallback-Verhalten und technische Kapselung im Seitenrahmen pruefen.",
    ),
    "cfo": (
        "Business Case, TCO, ROI und Investitionsszenarien konkretisieren.",
        "Sensitivitaeten fuer Aufwand, Nutzen, Adoption und Time-to-Value pruefen.",
    ),
    "design": (
        "Komponenten, Zustandsdarstellungen und Kategorie-Default-Bilder spezifizieren.",
        "Designfreigabe und Pflegeverantwortung festlegen.",
    ),
    "engineering": (
        "Teststrategie, Definition of Done, Code Review und Lieferartefakte festlegen.",
        "Messbare nichtfunktionale Anforderungen in automatisierbare Tests ueberfuehren.",
    ),
    "executive_communication": (
        "Kernbotschaft, Entscheidung, Wirkung, Risiko und naechsten Schritt schaerfen.",
        "Fachsprache in managementtaugliche Storyline und Folienlogik uebersetzen.",
    ),
    "frontend": (
        "CSS-/JavaScript-Isolation und Mehrfachinstanzen verbindlich absichern.",
        "Performance, Accessibility und responsive Darstellung pruefbar formulieren.",
    ),
    "geo": (
        "Sprachen, Maerkte und Taxonomien nur bei Projektbezug verbindlich machen.",
        "Maschinenlesbare Metadaten und stabile IDs vorsehen.",
    ),
    "leadmanagement": (
        "Leadmanagement als nicht relevant kennzeichnen, wenn kein Leadprozess beauftragt ist.",
        "Interne Kontakt- oder Einreichprozesse klar vom Leadmanagement abgrenzen.",
    ),
    "marketing": (
        "Markenfit, Zielgruppenbotschaft und Kampagnenanschluss pruefen.",
        "CTA-Logik, Content-Anforderungen und messbare Marketingwirkung konkretisieren.",
    ),
    "operations": (
        "Deployment, Monitoring, Support, Rollback und Betriebsverantwortung definieren.",
        "Azure-Betriebsmodell, Umgebungen und Service Levels klaeren.",
    ),
    "research_evidence": (
        "Quellen, Benchmarks, Praxisbeispiele und Evidenzgrad pruefen.",
        "Fakten, Annahmen, Hypothesen und Datenluecken klar trennen.",
    ),
    "sales": (
        "Angebotsumfang, Optionen und Mitwirkungspflichten vergleichbar strukturieren.",
        "Nachtraege durch klare Annahmen und Abgrenzungen begrenzen.",
    ),
    "security": (
        "Keycloak-Konfiguration, CSP, Secrets und externe URLs pruefen.",
        "Security- und Datenschutzfreigaben als Gates vor Go-live definieren.",
    ),
    "seo": (
        "SEO/GEO als nicht relevant kennzeichnen, wenn die Anwendung nur intern erreichbar ist.",
        "Interne Auffindbarkeit und Metadaten getrennt bewerten.",
    ),
    "strategy": (
        "MVP, Optionen und spaetere Ausbaustufen konsequent trennen.",
        "Nutzen, Entscheidungspunkte und Erfolgskriterien bestaetigen.",
    ),
    "ux": (
        "Nutzeraufgaben, Filterverhalten, Lade-, Fehler- und Leerzustaende pruefen.",
        "Akzeptanzkriterien fuer Bedienbarkeit und Barrierefreiheit konkretisieren.",
    ),
}


def is_insufficient_quota_error(error: BaseException) -> bool:
    text = str(error).lower()
    return "insufficient_quota" in text or (
        "exceeded your current quota" in text and "429" in text
    )


def _project_name(task: str) -> str:
    context = parse_task_context(task)
    if context.display_name:
        return context.display_name

    match = re.search(r"^PROJEKTNAME:\s*(.+?)\s*$", task, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()

    match = re.search(r"^#\s+Projektauftrag:\s*(.+?)\s*$", task, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()

    heading = re.search(r"^##\s+Task[^\n]*[-–]\s*(.+?)\s*$", task, flags=re.MULTILINE)
    if heading:
        return heading.group(1).strip()

    return "Anforderungsbewertung"


def _management_question(task: str) -> str:
    return parse_task_context(task).management_question


def _is_ai_coding_assessment(task: str) -> bool:
    context = parse_task_context(task)
    lower = task.lower()
    if context.is_management_assessment and "coding-system" in lower:
        return True
    return "ki-coding-system" in lower or "ki-basierte coding-systeme" in lower


def build_offline_review(agent_name: str, task: str) -> str:
    focus = ROLE_FOCUS.get(
        agent_name,
        (
            "Anforderungen auf Vollstaendigkeit und Pruefbarkeit untersuchen.",
            "Offene Entscheidungen, Annahmen und Abgrenzungen dokumentieren.",
        ),
    )
    focus_list = "\n".join(f"- {item}" for item in focus)
    project = _project_name(task)

    return f"""\
> **Offline-Fallback:** Dieses Review wurde regelbasiert ohne OpenAI-API erzeugt.
> Es ist eine strukturierte Vorpruefung und kein gleichwertiger Ersatz fuer eine
> semantische Expertenanalyse.

## 1. Kernaussage

Die Managementfrage **{project}** ist aus Sicht der Rolle `{agent_name}` anhand
der verbindlichen Board-Kriterien zu bewerten. Vor einer Managemententscheidung
muessen Nutzen, Risiken, Voraussetzungen, Governance, Wirtschaftlichkeit und
naechste Schritte widerspruchsfrei und objektiv pruefbar sein.

## 2. Chancen

- Einheitliche Entscheidungsgrundlage fuer Management, Budget und Umsetzung.
- Fruehe Klaerung von Abhaengigkeiten reduziert Governance- und Akzeptanzrisiken.
- Klare Bewertungslogik trennt belastbare Empfehlung von unbelegter Technologiebegeisterung.

## 3. Risiken

- Nicht aufgeloeste Annahmen koennen zu einer falschen strategischen Entscheidung fuehren.
- Nicht messbare Nutzenhypothesen erschweren ROI- und Wirkungskontrolle.
- Ungeklaerte Verantwortung, Governance oder Enablement kann Adoption und Compliance blockieren.

## 4. Anforderungen

{focus_list}

## 5. Konkrete Empfehlungen

- Jede Empfehlung mit Annahmen, Evidenz, Risiken und Erfolgskriterien verknuepfen.
- Offene Entscheidungen mit Verantwortlichkeit und Klaerungszeitpunkt versehen.
- Pilot, Skalierung und Governance klar voneinander trennen.
- Nicht relevante Prueffelder ausdruecklich und begruendet kennzeichnen.

## 6. Offene Fragen

- Welche Managemententscheidung soll getroffen werden: Pilot, Rollout, Stopp oder vertiefte Analyse?
- Welche Evidenz, KPIs und finanziellen Annahmen reichen fuer die Entscheidung aus?
- Welche Governance-, Security-, Enablement- und Betriebsverantwortlichen muessen vor Start benannt werden?
"""


def build_offline_recommendation(task: str, reviews: list[str]) -> str:
    if _is_ai_coding_assessment(task):
        return build_ai_coding_systems_recommendation(task, reviews)

    project = _project_name(task)
    review_count = len(reviews)

    return f"""\
# Offline-Board-Empfehlung: {project}

> **Status des Laufs:** OpenAI-API-Kontingent erschoepft. Diese Empfehlung wurde
> lokal und regelbasiert aus dem Task sowie {review_count} Offline-Reviews
> erzeugt. Sie dient als belastbare Checkliste, ersetzt aber nicht die
> semantische Diskussion des vollstaendigen Gremiums.

## 1. Executive Summary

Der Projektauftrag ist **freigabefaehig mit verbindlichen Aenderungen**, sofern
die unten genannten offenen Entscheidungen vor Ausschreibung geschlossen oder
als belastbare Annahmen in die Vergabeunterlagen aufgenommen werden. Kritisch
sind insbesondere eindeutige Verantwortlichkeiten, messbare
Akzeptanzkriterien, Plattform-/Security-Entscheidungen und die Trennung von MVP
und optionalen Leistungen.

## 2. Expertenbewertungen

Die regelbasierten Rollenpruefungen verlangen gemeinsam: eindeutige
Systemgrenzen, spezifizierte Schnittstellen, messbare Performance- und
Qualitaetsziele, technische Kapselung, Security-by-Design, definierte
Betriebsprozesse sowie eine objektiv pruefbare Abnahme.

## 3. Zielkonflikte

- **Flexibilitaet vs. Vergleichbarkeit:** Konfiguration ist vorzusehen, ihre
  erlaubten Werte und Grenzen muessen jedoch verbindlich beschrieben werden.
- **Schneller MVP vs. Betriebsreife:** Monitoring, Fehlerbehandlung, Security
  und Deployment bleiben auch im MVP Pflicht.
- **Markenkonsistenz vs. Fachdetail:** Fachliche Tiefe muss in eine klare,
  zielgruppengerechte Value Proposition und CTA-Logik uebersetzt werden.
- **Investitionssicherheit vs. Geschwindigkeit:** Ein schneller MVP braucht
  dennoch belastbare Kostenannahmen, Nutzenlogik und Entscheidungsszenarien.
- **Beratungsniveau vs. Evidenzluecken:** Managementaussagen muessen als
  Fakten, Benchmarks oder Annahmen kenntlich sein.
- **Optionale Analytics vs. Messbarkeit:** Produktanforderungen bleiben ohne
  Tracking pruefbar; Analytics wird nur bei separater Beauftragung umgesetzt.

## 4. Loesungsoptionen

1. Alle offenen Plattformfragen vor Ausschreibung entscheiden.
2. Nicht entscheidbare Punkte als verbindliche Annahmen mit bepreister Option
   ausschreiben.
3. Fuer risikoreiche Integrationsthemen eine kurze Discovery-Phase vor der
   Festpreisumsetzung beauftragen.

Bevorzugt wird Option 2, ergaenzt um eine zeitlich begrenzte Discovery fuer
CoreMedia-, Azure-, API- und Keycloak-Integration.

## 5. MVP

Der MVP muss funktionale Kernablaeufe, konfigurierbare Filter und Vorfilter,
Kategorie-Default-Bilder, CoreMedia-Einbettung, API-Anbindung, Keycloak-
Absicherung, technische Kapselung, Performance, Accessibility, Fehlerzustaende,
Dokumentation und Betriebsuebergabe enthalten. Analytics bleibt optional.

## 6. Roadmap

Personalisierung, Benachrichtigungen, komplexe Redaktionsworkflows,
Mehrsprachigkeit, Favoriten, KI-Funktionen und Management-Dashboards sind als
separat bepreiste Ausbaustufen zu behandeln.

## Financial Gate

Business Case, TCO, ROI, Payback, Szenarien und Sensitivitaeten sind fuer
Management- oder Budgetentscheidungen zu beschreiben. Wenn belastbare Zahlen
noch fehlen, muessen Annahmen, Bandbreiten, Datenquellen und offene
Finanzierungsentscheidungen transparent markiert werden.

## Evidence Gate

Zentrale Managementaussagen muessen mit internen Daten, Benchmarks,
Marktstudien, Praxisbeispielen oder klar gekennzeichneten Annahmen unterlegt
werden. Quellenqualitaet, Aktualitaet, Uebertragbarkeit und Datenluecken sind
zu bewerten.

## Executive Communication Gate

Die Empfehlung muss eine klare Executive Storyline liefern: Entscheidung,
Business Impact, Optionen, Zielkonflikte, Risiken, Abhaengigkeiten und
naechster Schritt. Fachdetails sind in So-what und Now-what fuer
Geschaeftsfuehrung oder Steering Committee zu uebersetzen.

## 7. CoreMedia-Anforderungen

Content-Typ, Preview, Vorfilter, sichtbare Filter, Parametergrenzen,
Fallback-Inhalt und Mehrfachinstanzen muessen vor Umsetzung bestaetigt werden.
CSS und JavaScript duerfen den einbindenden Seitenrahmen nicht beeinflussen.

## Marketing Gate

Markenfit, Zielgruppenbotschaft, Kampagnenverwertung, Content-Anforderungen,
CTA-Logik und messbare Marketingwirkung muessen fuer oeffentliche oder
vertriebliche Initiativen beschrieben werden. Bei rein internen Anwendungen ist
Marketing als nicht relevant zu begruenden; dennoch sind Tonalitaet,
Adressatenlogik und interne Aktivierung zu klaeren.

## 8. SEO-/GEO-Anforderungen

Fuer eine ausschliesslich interne Intranet-App ist externe SEO nicht relevant.
Interne Auffindbarkeit, strukturierte Metadaten und stabile Taxonomien bleiben
relevant. GEO ist nur bei einer spaeteren internen KI-Nutzung zu vertiefen.

## 9. Leadmanagement-Auswirkungen

Klassisches Leadmanagement ist fuer den beschriebenen internen MVP nicht
relevant. Ein interner Einreich-CTA ist als separater Fachprozess zu behandeln.

## 10. Analytics Gate

Analytics ist optional. Ohne Beauftragung werden keine Tracking-Events
implementiert. Bei Beauftragung sind Eventmodell, Datenschutzfreigabe,
Testverfahren, Reporting und Verantwortlichkeit vor Entwicklung festzulegen.
Optionale KPIs beziehungsweise Erfolgskennzahlen sind Seitenaufrufe,
Filterverwendung, Klicks auf Originalquellen, leere Ergebnismengen und
technische Fehlerraten. Reporting beziehungsweise Dashboard und Monitoring
sind nur bei Beauftragung des Analytics-Moduls umzusetzen. Datenqualitaet und
Consent-Vorgaben sind vor Aktivierung zu pruefen.

## 11. Risiken

- **Architecture Gate:** Azure-, CoreMedia- und API-Systemgrenzen sind zu bestaetigen.
- **Financial Gate:** Business Case, TCO, ROI und Szenarien sind fuer Managemententscheidungen zu quantifizieren oder als Annahmen zu markieren.
- **Evidence Gate:** Quellenbasis, Benchmarks und Evidenzgrad zentraler Aussagen sind offenzulegen.
- **Executive Communication Gate:** Management-Storyline, Entscheidung und naechster Schritt sind zu schaerfen.
- **Engineering Gate:** Teststrategie, Code Review und Definition of Done sind zu konkretisieren.
- **Security Gate:** Keycloak-Flow, Rollen, Token-Handling und CSP sind festzulegen.
- **Operations Gate:** Deployment, Monitoring, Support, Rollback und Service Levels fehlen als verbindliche Betriebsvereinbarung.
- **Marketing Gate:** Markenfit, Zielgruppenbotschaft, Kampagnenanschluss und CTA-Logik sind zu bestaetigen.
- Ungeklaerte Bildpflege und Taxonomie koennen Daten- und Darstellungsfehler verursachen.

## 12. Entscheidungsempfehlung

Status: **freigabefaehig mit verbindlichen Aenderungen**.

Vor Versand an Dienstleister sind die kritischen Restpunkte entweder zu
entscheiden oder als eindeutige, bepreiste Annahmen und Optionen aufzunehmen.

## Verbindliche Aenderungsliste

| ID | Prioritaet | Abschnitt | Problem | Aenderung | Verantwortlich | Status |
|---|---|---|---|---|---|---|
| A-01 | kritisch | Architektur | Azure-Betriebsmodell nicht abschliessend spezifiziert | Hosting, Netzwerk, Deployment und Verantwortlichkeit festlegen | Plattform/Architektur | noch zu entscheiden |
| A-02 | kritisch | Security | Keycloak-Flow und Rollen offen | Realm, Client, Flow, Audience und Rollen dokumentieren | Security/IAM | noch zu entscheiden |
| A-03 | hoch | Performance | Referenzumgebung nicht definiert | Browser, Netzwerk, Datenmenge und Messverfahren festlegen | Product Owner/IT | noch zu entscheiden |
| A-04 | hoch | Betrieb | Support und Monitoring nicht verbindlich | SLA, Alerting, Rollback und Betriebsuebergabe ergaenzen | Operations | noch zu entscheiden |
| A-05 | mittel | Daten | Pflege der Kategorien und Default-Bilder offen | Source of Truth und Pflegeprozess benennen | Fachbereich/Redaktion | noch zu entscheiden |

## Gemeinsame Restpunkteliste

| ID | Kategorie | Beschreibung | Auswirkung | Verantwortlich | Benoetigte Information | Klaerungszeitpunkt | Uebergangsloesung | Status |
|---|---|---|---|---|---|---|---|---|
| R-01 | Offener Punkt | Zielarchitektur fuer Azure, CoreMedia und API bestaetigen | Angebot, Betrieb, Termin | Architektur/Plattform | freigegebenes Architekturdiagramm | vor Ausschreibung | Discovery als Option | offen |
| R-02 | Offene Frage | Welcher Keycloak-Realm, Client und Flow wird verwendet? | Security und Integration | IAM/Security | Client- und Rollenkonfiguration | vor Beauftragung | Authorization Code mit PKCE als Annahme | offen |
| R-03 | Annahme | Die bestehende News-Datenquelle liefert stabile IDs und Facetten | API-Aufwand und Budget | Datenverantwortliche | API-Beispiel und Datenqualitaet | vor Beauftragung | Middleware-Aufwand separat bepreisen | angenommen |
| R-04 | Erwartung | Schueco stellt Product Owner sowie CoreMedia-, IAM- und API-Ansprechpartner termingerecht bereit | Projektlaufzeit | Schueco Projektleitung | Ressourcenbestaetigung | vor Projektstart | Terminplan verschiebt sich bei Verzug | offen |
| R-05 | Abgrenzung | Analytics, Personalisierung, Alerts und KI-Funktionen gehoeren nicht zum verbindlichen MVP | Scope und Budget | Product Owner/Einkauf | Bestaetigung der Leistungsabgrenzung | vor Ausschreibung | als Optionen anbieten lassen | offen |
"""


def build_ai_coding_systems_recommendation(task: str, reviews: list[str]) -> str:
    question = _management_question(task) or _project_name(task)
    review_count = len(reviews)

    return f"""\
# Offline-Board-Empfehlung: KI-Coding-Systeme im Marketing

> **Status des Laufs:** OpenAI-API-Kontingent erschoepft. Diese Empfehlung wurde
> lokal und regelbasiert aus der Managementfrage sowie {review_count}
> Offline-Reviews erzeugt. Sie bewertet die gestellte Anforderung und ist kein
> Projektauftrag, keine Ausschreibung und kein Umsetzungskonzept.

## 1. Executive Summary

Die Managementfrage lautet: **{question}**

Vorlaeufige Board-Empfehlung: **Ja, bedingt und kontrolliert.** Schueco sollte
KI-Coding-Systeme im Marketing strategisch etablieren, aber zunaechst als
governance-gefuerten, messbaren Piloten fuer klar abgegrenzte Marketing-Use-
Cases. Der Nutzen liegt vor allem in schnellerer Prototypisierung, Content- und
SEO/GEO-Automatisierung, internen Tools, Datenaufbereitung und besserer
Uebersetzung von Marketinganforderungen in digitale Artefakte.

Die Einfuehrung ist nicht als ungesteuerter Tool-Rollout zu verstehen. Kritisch
sind Datenschutz, IP, Shadow AI, Vendor Lock-in, Qualifizierung, Qualitaet,
Security-Freigaben und ein belastbarer Business Case.

## 2. Expertenbewertungen

- **Strategy:** Strategisch sinnvoll, wenn KI-Coding-Systeme als Marketing-
  Produktivitaets- und Innovationsfaehigkeit verstanden werden, nicht als
  Spielzeug einzelner Power User.
- **CFO:** Freigabe nur mit Szenarien fuer Lizenzkosten, Enablement,
  Governance-Aufwand, eingesparte Agentur-/Entwicklungszeit und Time-to-Market.
- **Marketing:** Hoher Nutzen fuer Kampagnen-Prototypen, Landingpage-
  Varianten, Content-Operations, SEO/GEO-Experimente und interne Tools.
- **Research & Evidence:** Externe Benchmarks muessen nachgereicht werden;
  zentrale Nutzenannahmen sind im Piloten mit internen Messdaten zu validieren.
- **Executive Communication:** Die Managementstory muss klar lauten:
  kontrollierte Befaehigung statt unkontrollierter Shadow-AI.
- **Security:** Ohne Tool-Freigabe, Datenklassifizierung, Prompt-Regeln,
  Code-Review und IP-Leitplanken keine breite Nutzung.
- **Engineering/Architecture:** Sinnvoll, wenn Repositories, Review-Prozesse,
  Dokumentation, Testing und Plattformgrenzen verbindlich geregelt sind.
- **Analytics:** Erfolg muss ueber Produktivitaet, Durchlaufzeit, Qualitaet,
  Wiederverwendung, Fehlerquote und Business-Wirkung messbar sein.

## 3. Zielkonflikte

- **Geschwindigkeit vs. Governance:** KI-Coding beschleunigt Prototypen, kann
  aber ohne Regeln Datenschutz-, IP- und Qualitaetsrisiken erhoehen.
- **Demokratisierung vs. Engineering-Qualitaet:** Marketing kann schneller
  digitale Loesungen entwerfen; produktionsreifer Code braucht weiter Review,
  Testing und Architekturverantwortung.
- **Toolvielfalt vs. Standardisierung:** Codex, Cursor, GitHub Copilot,
  ChatGPT, Claude und andere Tools bieten unterschiedliche Staerken; Schueco
  braucht Kriterien statt Tool-Wildwuchs.
- **Kurzfristiger Effizienzgewinn vs. langfristiger Kompetenzaufbau:** Der
  groesste Wert entsteht nicht durch Einzellizenzen, sondern durch Enablement,
  Standards und wiederverwendbare Patterns.

## 4. Loesungsoptionen

1. **Kein strategischer Einsatz:** minimiert Governance-Aufwand, erhoeht aber
   Shadow-AI-Risiko und bremst Lernkurve.
2. **Ungesteuerter Tool-Rollout:** schnell, aber nicht empfehlenswert wegen
   Datenschutz-, IP-, Qualitaets- und Kostenrisiken.
3. **Governance-gefuehrter Pilot:** empfohlen. Begrenzter Nutzerkreis,
   freigegebene Tools, klare Use Cases, KPIs, Security-Regeln und Review.
4. **Direkter Skalierungsrollout:** erst nach Pilot-Evidenz, Toolauswahl,
   Betriebsmodell und Enablement sinnvoll.

## 5. MVP

Der MVP ist ein 8- bis 12-woechiger Pilot im Marketing mit:

- 3 bis 5 priorisierten Use Cases, z. B. Landingpage-Prototyping,
  Content-Transformation, SEO/GEO-Strukturierung, kleine interne Tools und
  Reporting-Automatisierung.
- freigegebenem Toolset und klarer Datenklassifizierung.
- Prompt-, Repository-, Review- und Dokumentationsstandards.
- Security-, Legal- und Betriebsfreigabe fuer den Pilotrahmen.
- KPI-Set fuer Produktivitaet, Qualitaet, Time-to-Market und Akzeptanz.

## 6. Roadmap

- **0-3 Monate:** Pilotdesign, Tool-Shortlist, Governance, Schulung,
  Use-Case-Auswahl, Baseline-Messung.
- **3-12 Monate:** Pilot auswerten, Standards schaerfen, Toolentscheidung,
  Best Practices, Enablement-Programm, erste skalierte Marketing-Workflows.
- **12-24 Monate:** Integration in Content-, SEO/GEO-, Analytics- und
  Kampagnenprozesse; Aufbau wiederverwendbarer Agenten und Templates.
- **24-36 Monate:** strategisches Operating Model fuer AI-assisted Marketing
  Engineering mit Portfolio-Steuerung, Governance und Kompetenzmodell.

## 7. CoreMedia-Anforderungen

KI-Coding-Systeme duerfen CoreMedia-Prozesse nur unter klaren Leitplanken
unterstuetzen. Relevant sind Content-Type-Verstaendnis, Template-nahe
Prototypen, redaktionelle Workflows, strukturierte Daten, Preview-Faehigkeit,
Dokumentation und klare Trennung zwischen Prototyp, Content-Artefakt und
produktionsreifer Implementierung.

## 8. SEO-/GEO-Anforderungen

Der Einsatz ist besonders relevant fuer SEO/GEO: strukturierte Content-
Briefings, FAQ-Module, Schema.org/JSON-LD-Entwuerfe, Entity Mapping,
Grounding-Pages, interne Verlinkungslogik und Varianten fuer AI Search. Alle
Outputs brauchen fachliche Pruefung, Quellenkontrolle und Qualitaetsstandards.

## 9. Leadmanagement-Auswirkungen

Direkter Leadmanagement-Nutzen entsteht, wenn KI-Coding-Systeme Landingpages,
Formularlogik, Segmentierungsprototypen, Kampagnen-CTAs, HubSpot-nahe
Automatisierungen oder Reporting-Artefakte beschleunigen. MQL/SQL-Regeln,
Consent, Attribution und Sales Routing duerfen nicht ohne fachliche Freigabe
veraendert werden.

## 10. Analytics Gate

Pflicht-KPIs fuer den Piloten:

- Durchlaufzeit von Idee zu Prototyp.
- Anteil wiederverwendbarer Artefakte.
- Qualitaetsquote nach Review.
- Fehler- oder Nacharbeitsrate.
- eingesparte interne oder externe Aufwaende.
- Akzeptanz und aktive Nutzung durch Marketingteams.
- Business-nahe Wirkung je Use Case, z. B. schnellere Kampagnenstarts,
  bessere SEO/GEO-Abdeckung oder reduzierte Reporting-Aufwaende.

Tracking, Dashboard, Review-Protokolle und Datenqualitaet muessen vor Pilotstart
definiert werden. Ohne Baseline keine ROI-Aussage.

## 11. Risiken

- **Financial Gate:** Lizenz-, Enablement-, Governance- und Review-Aufwaende
  koennen den Nutzen uebersteigen, wenn Use Cases zu unscharf bleiben.
- **Evidence Gate:** Externe Benchmarks sind nur begrenzt uebertragbar; Schueco
  braucht interne Pilotdaten.
- **Executive Communication Gate:** Management darf nicht den Eindruck eines
  freien Tool-Rollouts bekommen; die Story ist kontrollierte Befaehigung.
- **Marketing Gate:** Ohne klare Use Cases entsteht Tool-Spielerei statt
  Kampagnen- und Content-Wirkung.
- **Security Gate:** Datenschutz, IP, Prompt-Injection, Secret Leakage und
  Shadow AI sind kritisch.
- **Engineering Gate:** KI-generierter Code darf nicht ohne Review, Tests und
  Dokumentation produktiv gehen.
- **Operations Gate:** Betrieb, Support und Ownership fuer entstehende Tools
  muessen geklaert sein.

## 12. Entscheidungsempfehlung

Status: **READY WITH RISKS**.

Schueco sollte KI-Coding-Systeme im Marketing strategisch etablieren, aber nur
ueber einen kontrollierten Piloten mit klarer Governance, freigegebenen Tools,
messbaren Use Cases und Management-Review nach 8 bis 12 Wochen. Eine breite
Skalierung sollte erst nach nachgewiesenem Nutzen, Security-Freigabe,
Toolentscheidung und Enablement-Konzept erfolgen.

## SWOT

| Staerken | Schwaechen |
|---|---|
| Schnellere Prototypen, bessere Automatisierung, hoeheres Innovationstempo | Abhaengig von Kompetenzen, Review-Aufwand, Datenqualitaet und Governance |

| Chancen | Risiken |
|---|---|
| SEO/GEO-Vorsprung, Kampagnenbeschleunigung, weniger externe Abhaengigkeit | Shadow AI, Datenschutz, IP-Risiken, Vendor Lock-in, Qualitaetsschwankungen |

## Top 10 Chancen

1. Schnellere Kampagnen- und Landingpage-Prototypen.
2. Bessere SEO/GEO-Strukturierung.
3. Automatisierung repetitiver Marketingaufgaben.
4. Schnellere Daten- und Reporting-Artefakte.
5. Hoehere Experimentiergeschwindigkeit.
6. Besseres Briefing zwischen Marketing und IT.
7. Wiederverwendbare Templates und Patterns.
8. Weniger Abhaengigkeit von kleinen externen Umsetzungen.
9. Kompetenzaufbau fuer AI-assisted Marketing.
10. Reduktion von Time-to-Market.

## Top 10 Risiken

1. Shadow AI und unkontrollierte Toolnutzung.
2. Datenschutz- und IP-Verletzungen.
3. Unerlaubte Nutzung vertraulicher Daten.
4. Vendor Lock-in.
5. Ungepruefter oder unsicherer Code.
6. Falsche ROI-Erwartungen.
7. Fehlende Akzeptanz im Team.
8. Qualitaetsschwankungen bei Outputs.
9. Unklare Ownership fuer interne Tools.
10. Toolkosten ohne skalierbaren Nutzen.

## Marktvergleich

| Tool | Staerke | Risiko | Geeigneter Marketingeinsatz |
|---|---|---|---|
| Codex | Agentische Umsetzung, Repo-nahe Aufgaben, Automatisierung | braucht klare Repo- und Review-Regeln | interne Tools, Prototypen, Automatisierung |
| Cursor | IDE-nahe Entwicklung und schnelle Iteration | Entwicklernahe Nutzung, Governance noetig | Prototyping mit technischen Power Usern |
| GitHub Copilot | Breite Entwicklerproduktivitaet, Enterprise-Integration | Lizenz- und Codequalitaetssteuerung | Engineering-nahe Marketingprojekte |
| ChatGPT | Ideation, Strukturierung, Code- und Content-Hilfe | Datenklassifizierung und Quellenkontrolle | Briefings, kleine Skripte, Content-Struktur |
| Claude | lange Kontexte, Analyse, Text- und Codeunterstuetzung | Tool- und Datenschutzfreigabe pruefen | Dokumentation, Analyse, Konzeptarbeit |

## Business Case

Der Business Case sollte nicht pauschal ueber Lizenzen entschieden werden,
sondern ueber Pilot-KPIs. Relevante Nutzenhebel sind eingesparte Agentur- oder
Entwicklungsaufwaende, schnellere Kampagnenstarts, weniger manuelle
Routinearbeit, bessere Wiederverwendung und schnellere Tests neuer Ideen.

Mindestanforderung vor Skalierung: messbare Baseline, Pilotkosten,
Zeitersparnis, Qualitaetsbewertung, Adoptionsrate und Risikokosten.

## Governance

- freigegebene Tools und klare Datenklassifizierung.
- keine Secrets, Kundendaten oder vertraulichen Informationen in nicht
  freigegebenen Systemen.
- Code-Review, Tests und Dokumentation fuer alle produktionsnahen Artefakte.
- Prompt- und Output-Guidelines.
- Schulung fuer Marketing, SEO/GEO, Analytics und technische Power User.
- zentrales Register fuer Use Cases, Tools, Risiken und Ergebnisse.

## Massnahmenplan

### Quick Wins

- Pilotteam und Use Cases definieren.
- Tool-Freigabe und Datenregeln klaeren.
- Baseline fuer Durchlaufzeit und Aufwand messen.
- Prompt-, Review- und Dokumentationsstandards erstellen.

### Mid Term

- Pilot auswerten und Toolentscheidung vorbereiten.
- Enablement-Programm fuer Marketingrollen aufsetzen.
- Wiederverwendbare Templates, Agenten und Automatisierungen etablieren.
- SEO/GEO- und Analytics-Workflows integrieren.

### Long Term

- AI-assisted Marketing Engineering als Operating Model etablieren.
- Portfolio-Steuerung fuer Automatisierungs-Use-Cases einfuehren.
- Governance, Security und ROI-Reporting dauerhaft betreiben.

## Management Storyline

**Warum?** Marketing braucht mehr Geschwindigkeit, bessere Skalierbarkeit und
mehr technische Umsetzungsfaehigkeit.

**Warum jetzt?** KI-Coding-Systeme werden Standardwerkzeuge; ohne Leitplanken
entsteht Shadow AI.

**Warum Schueco?** Schueco hat komplexe Produkte, viele Zielgruppen und hohe
Anforderungen an digitale Content- und Servicequalitaet.

**Welcher Nutzen?** Schnellere Prototypen, bessere SEO/GEO-Faehigkeit,
effizientere Marketingprozesse und geringere Abhaengigkeit bei kleinen
digitalen Umsetzungen.

**Welche Risiken?** Datenschutz, IP, Qualitaet, Vendor Lock-in, Akzeptanz und
unklare Ownership.

**Welche Investitionen?** Lizenzen, Enablement, Governance, Review-Kapazitaet
und Pilotsteuerung.

**Was passiert, wenn wir nichts tun?** Einzelne Teams nutzen KI unkontrolliert,
Lerneffekte bleiben zufaellig und Schueco verliert Geschwindigkeit.

**Naechster Schritt:** Governance-gefuehrten Pilot beschliessen und nach 8 bis
12 Wochen anhand messbarer Ergebnisse ueber Skalierung entscheiden.
"""
