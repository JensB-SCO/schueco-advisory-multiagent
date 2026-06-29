# Aufgabe: Gremienreview eines Projektauftrags

## Verwendung

Dieser Task dient der fachlichen, technischen, wirtschaftlichen und organisatorischen Prüfung eines bereits erstellten Projektauftrags durch das Schüco Digital Advisory Board.

Vor dem Start sind die folgenden Platzhalter zu ersetzen:

```text
PROJEKTAUFTRAG: C:\Users\BROCJE\OneDrive - Schüco International\Dokumente\Projekte\Visual Studio Code\schueco-advisory-multiagent\outputs\003-branchennews-teamwork\briefing\20260618-projektauftrag-branchennews-teamwork.md
PROJEKTNAME: Branchennews-App für Schüco Teamwork/Intranet
ZIEL_DER_PRÜFUNG: Prüfung auf inhaltliche Vollständigkeit, Freigabe zur Ausschreibung
ZUSÄTZLICHER_KONTEXT: die App soll eingeständig in Azure betrieben werden
```

Der vollständige Inhalt des angegebenen Projektauftrags und der relevanten Referenzdokumente ist als Prüfgegenstand zu verwenden. Wenn der verwendete Runner referenzierte Dateien nicht automatisch lädt, muss der Projektauftrag vollständig unter dem folgenden Abschnitt eingefügt werden:

```text
BEGINN PROJEKTAUFTRAG
<vollständiger Inhalt>
ENDE PROJEKTAUFTRAG
```

Ein reiner Dateipfad ohne geladenen Dokumentinhalt reicht für das Review nicht aus.

## Ziel

Prüfe den Projektauftrag so gründlich, dass er anschließend als belastbare Grundlage für Ausschreibung, Beauftragung, Umsetzung und Abnahme verwendet werden kann.

Das Gremium soll:

- fachliche, technische und organisatorische Lücken identifizieren
- widersprüchliche Anforderungen und Zielkonflikte auflösen
- unklare Anforderungen präzisieren
- fehlende Anforderungen ergänzen
- Anforderungen auf Umsetzbarkeit und Prüfbarkeit untersuchen
- konkrete Lösungen für identifizierte Probleme entwickeln
- Risiken, Abhängigkeiten und notwendige Mitwirkungen transparent machen
- Akzeptanzkriterien auf Eindeutigkeit und Messbarkeit prüfen
- Leistungsumfang und Abgrenzungen belastbar formulieren
- eine gemeinsame Freigabeempfehlung abgeben

## Verbindliches Vorgehen

Das Review erfolgt in aufeinander aufbauenden Beratungsrunden.

### Runde 1: Einzelprüfung

Jede Expertenrolle prüft den Projektauftrag aus ihrer Perspektive und dokumentiert:

- bestätigte Stärken
- fehlende oder unklare Anforderungen
- Widersprüche
- Risiken
- offene Entscheidungen
- konkrete Lösungsvorschläge
- notwendige Änderungen am Projektauftrag

Feststellungen dürfen nicht nur als Kritik formuliert werden. Zu jedem lösbaren Problem ist mindestens ein konkreter Lösungsvorschlag zu liefern.

### Runde 2: Konsolidierung

Das Gremium führt alle Feststellungen zusammen und:

- entfernt Dubletten
- kennzeichnet widersprüchliche Empfehlungen
- ordnet Themen nach Auswirkung und Dringlichkeit
- entwickelt gemeinsame Lösungsoptionen
- bewertet Lösungsoptionen nach Nutzen, Aufwand, Risiko und Umsetzbarkeit
- bestimmt für jedes Thema eine bevorzugte Lösung

### Runde 3: Konfliktklärung

Für alle noch strittigen oder ungelösten Themen muss das Gremium:

1. den Konflikt präzise beschreiben
2. die betroffenen Ziele und Rollen benennen
3. mindestens zwei realistische Lösungsoptionen bewerten
4. eine bevorzugte Lösung oder einen belastbaren Entscheidungsweg formulieren
5. die Konsequenzen einer Nichtentscheidung beschreiben

Das Gremium darf ein Thema nicht allein mit dem Hinweis "muss geklärt werden" abschließen, wenn es selbst eine fachlich begründete Lösung oder sinnvolle Annahme entwickeln kann.

### Runde 4: Vollständigkeitsprüfung

Nach der Konfliktklärung prüft das Gremium den überarbeiteten Zielzustand erneut auf:

- fachliche Vollständigkeit
- technische Umsetzbarkeit
- CoreMedia-/Integrationsfähigkeit
- Daten- und API-Anforderungen
- UX und Accessibility
- Security, Datenschutz und Compliance
- Betrieb, Monitoring und Support
- Performance und Skalierbarkeit
- Testbarkeit und Abnahmefähigkeit
- Liefergegenstände und Dokumentation
- Projektrollen und Mitwirkungspflichten
- Budget-, Termin- und Ressourcenrisiken
- SEO/GEO, sofern für das Projekt relevant
- Leadmanagement, sofern für das Projekt relevant
- Analytics nur, wenn es im Projektauftrag beauftragt oder vorgesehen ist

Nicht relevante Prüffelder sind ausdrücklich als "nicht relevant" mit kurzer Begründung zu kennzeichnen.

### Runde 5: Gemeinsamer Beschluss

Das Gremium formuliert eine gemeinsame Entscheidung:

- freigabefähig
- freigabefähig mit verbindlichen Änderungen
- noch nicht freigabefähig

Bei "freigabefähig mit verbindlichen Änderungen" müssen die Änderungen konkret und direkt in den Projektauftrag übertragbar formuliert sein.

Bei "noch nicht freigabefähig" muss klar beschrieben werden, welche Entscheidungen oder Informationen zwingend fehlen und wer sie liefern muss.

## Diskussions- und Konsensregeln

- Das Gremium diskutiert ein Thema so lange, bis eine tragfähige Lösung, eine dokumentierte Annahme oder eine klar abgegrenzte offene Entscheidung vorliegt.
- Mehrheitsmeinungen ersetzen keine fachliche Begründung.
- Minderheitenpositionen mit erheblichen Security-, Compliance-, Betriebs- oder Architekturfolgen müssen dokumentiert werden.
- Ungeklärte Themen dürfen nicht stillschweigend entfallen.
- Annahmen müssen als Annahmen gekennzeichnet und validierbar sein.
- Erwartungen müssen einer verantwortlichen Rolle oder Vertragspartei zugeordnet werden.
- Abgrenzungen müssen eindeutig beschreiben, was nicht Bestandteil des Auftrags ist.
- Offene Fragen müssen so formuliert sein, dass sie konkret beantwortet werden können.
- Für jeden offenen Punkt sind Verantwortlichkeit, benötigte Information und spätester Klärungszeitpunkt anzugeben.

## Prüfkriterien für den Projektauftrag

Prüfe insbesondere:

- Ist das Projektziel eindeutig und messbar?
- Sind Ausgangslage, Nutzergruppen und erwarteter Nutzen verständlich?
- Sind MVP, optionale Leistungen und spätere Ausbaustufen getrennt?
- Sind Muss-, Soll- und Kann-Anforderungen unterscheidbar?
- Sind funktionale und nichtfunktionale Anforderungen vollständig?
- Sind Schnittstellen, Datenmodelle, Authentifizierung und Berechtigungen beschrieben?
- Sind Performance-Ziele messbar und an eine Referenzumgebung gebunden?
- Sind Einbettung, technische Kapselung und Abhängigkeiten beschrieben?
- Sind Security-, Datenschutz- und Compliance-Anforderungen prüfbar?
- Sind Betriebsmodell, Monitoring, Support und Fehlerbehandlung geklärt?
- Sind Liefergegenstände vollständig?
- Sind Projektphasen, Rollen und Mitwirkungspflichten eindeutig?
- Sind Akzeptanzkriterien objektiv prüfbar?
- Sind Annahmen und Abhängigkeiten transparent?
- Sind offene Punkte vor Angebotsabgabe beziehungsweise Umsetzungsstart klärbar?
- Können Dienstleister auf dieser Grundlage vergleichbare Angebote erstellen?
- Sind Formulierungen frei von unnötigem Interpretationsspielraum?

## Erwartete Ergebnisse

### 1. Executive Summary

Kurze Bewertung des Projektauftrags mit Freigabestatus, wichtigsten Stärken, größten Lücken und zentraler Empfehlung.

### 2. Expertenbewertungen

Konsolidierte Bewertungen aller relevanten Expertenrollen.

### 3. Zielkonflikte

Alle identifizierten Zielkonflikte mit beschlossener Lösung oder Entscheidungsweg.

### 4. Lösungsoptionen

Bewertete Lösungsoptionen für wesentliche fachliche und technische Entscheidungen.

### 5. MVP

Bestätigter oder korrigierter MVP-Umfang mit klarer Abgrenzung.

### 6. Roadmap

Empfohlene Einordnung nicht zum MVP gehörender Anforderungen.

### 7. CoreMedia-Anforderungen

Bewertung und Ergänzung der CMS-, Integrations- und Konfigurationsanforderungen, sofern relevant.

### 8. SEO-/GEO-Anforderungen

Bewertung und Ergänzung, sofern relevant; andernfalls begründete Kennzeichnung als nicht relevant.

### 9. Leadmanagement-Auswirkungen

Bewertung und Ergänzung, sofern relevant; andernfalls begründete Kennzeichnung als nicht relevant.

### 10. Analytics Gate

Nur verbindlich anwenden, wenn Analytics im Projektauftrag beauftragt oder vorgesehen ist. Andernfalls als optional beziehungsweise nicht relevant kennzeichnen.

### 11. Risiken

Konsolidiertes Risikoregister mit Eintrittswahrscheinlichkeit, Auswirkung, Gegenmaßnahme und Verantwortlichkeit.

### 12. Entscheidungsempfehlung

Gemeinsamer Beschluss mit einem der Status:

- freigabefähig
- freigabefähig mit verbindlichen Änderungen
- noch nicht freigabefähig

## Verbindliche Änderungsliste

Erstelle eine priorisierte Liste aller empfohlenen Änderungen am Projektauftrag.

Für jede Änderung sind anzugeben:

| Feld | Inhalt |
|---|---|
| ID | Eindeutige Kennung |
| Priorität | kritisch, hoch, mittel oder niedrig |
| Abschnitt | Betroffener Abschnitt des Projektauftrags |
| Problem | Festgestellte Lücke oder Unklarheit |
| Änderung | Direkt übernehmbare Formulierung oder konkrete Anpassung |
| Begründung | Fachliche Begründung |
| Verantwortlich | Rolle für Entscheidung oder Umsetzung |
| Status | beschlossen, noch zu entscheiden oder verworfen |

## Gemeinsame Restpunkteliste

Falls nach allen Beratungsrunden Themen nicht abschließend lösbar sind, muss das Gremium genau eine gemeinsame, konsolidierte Restpunkteliste liefern.

Die Liste muss folgende Kategorien enthalten:

1. Offene Punkte
2. Offene Fragen
3. Annahmen
4. Erwartungen
5. Abgrenzungen

Für jeden Eintrag sind mindestens anzugeben:

| Feld | Inhalt |
|---|---|
| ID | Eindeutige Kennung |
| Kategorie | Offener Punkt, offene Frage, Annahme, Erwartung oder Abgrenzung |
| Beschreibung | Eindeutige Formulierung |
| Auswirkung | Konsequenz für Angebot, Umsetzung, Termin, Budget oder Betrieb |
| Verantwortlich | Rolle oder Organisation, die klären oder bestätigen muss |
| Benötigte Information | Konkret benötigter Input |
| Klärungszeitpunkt | Vor Ausschreibung, vor Beauftragung, vor Umsetzung, vor Abnahme oder später |
| Übergangslösung | Vorläufige Annahme oder Vorgehensweise |
| Status | offen, angenommen, bestätigt, abgelehnt oder erledigt |

Leere Kategorien sind mit "Keine offenen Einträge" auszuweisen. Widersprüchliche Restpunktelisten einzelner Experten sind nicht zulässig.

## Qualitätsanforderungen

- Empfehlungen müssen konkret und in den Projektauftrag übertragbar sein.
- Anforderungen und Akzeptanzkriterien müssen möglichst messbar formuliert sein.
- Offene Fragen dürfen keine bereits durch den Projektauftrag beantworteten Sachverhalte wiederholen.
- Die Restpunkteliste muss widerspruchsfrei zur Entscheidungsempfehlung sein.
- Kritische offene Punkte müssen eine Freigabe verhindern oder ausdrücklich als Freigabeauflage benannt werden.
- Alle wesentlichen Feststellungen müssen auf einen Abschnitt des Projektauftrags verweisen.
- Das Ergebnis muss auch ohne Kenntnis der einzelnen Expertenreviews verständlich sein.

## Ergebnisablage

Speichere Reviews und finale Empfehlung taskbezogen unter:

```text
outputs/<projektauftrag-name>/reviews/
outputs/<projektauftrag-name>/recommendation/
```

Speichere zusätzlich, sofern vom Runner unterstützt:

```text
outputs/<projektauftrag-name>/change-list/
outputs/<projektauftrag-name>/open-items/
```
