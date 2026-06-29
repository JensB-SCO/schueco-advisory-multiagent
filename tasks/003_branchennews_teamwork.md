# Aufgabe: Branchennews im Schüco Teamwork/Intranet

Entwickle ein Lösungskonzept für die Anzeige recherchierter Branchennews im Schüco Teamwork/Intranet.

## Ausgangslage

In einer Datenbank befinden sich recherchierte News aus der Bau- und Bauelementebranche. Die News werden im Internet recherchiert, kuratiert und in der Datenbank gespeichert.

Ein News-Eintrag enthält mindestens:
- Titel
- Kurzbeschreibung
- Link auf den externen Originalartikel im Internet
- Zuordnung zu mehreren Kategorien
- Land beziehungsweise Markt
- Thema beziehungsweise Themencluster
- Veröffentlichungs- oder Recherchedatum

Die Kategorien dienen dazu, News im Teamwork/Intranet zu filtern und für unterschiedliche Nutzergruppen relevanter zu machen.

## Zielbild

Mitarbeitende sollen im Schüco Teamwork/Intranet aktuelle, relevante und kuratierte Branchennews auf einen Blick sehen und gezielt nach Land, Thema, Zeitraum und weiteren Kriterien filtern können.

Die Lösung soll:
- Branchenentwicklungen schneller intern sichtbar machen.
- Rechercheergebnisse aus der bestehenden Datenbank nutzbar machen.
- News nach Kategorien, Ländern, Themen und Zeitraum filterbar machen.
- Externe Originalquellen transparent verlinken.
- In den bestehenden Teamwork-/CoreMedia-Seitenrahmen integrierbar sein.
- Eine spätere Erweiterung um weitere Märkte, Themen, Personalisierung oder Benachrichtigungen ermöglichen.

## Lösungsidee

Bewerte die Entwicklung einer eigenständigen App, zum Beispiel auf Basis von React.

Die App soll als Web-Komponente oder vergleichbarer Frontend-Baustein in den CoreMedia-Seitenrahmen eingebunden werden. Die Einbindung kann über einen CMS-Content-Typ erfolgen, zum Beispiel ein Action-Objekt oder einen vergleichbaren CoreMedia-Objekttyp.

Die App soll die News aus einer bestehenden Datenbank beziehungsweise über eine geeignete API beziehen und im Teamwork/Intranet anzeigen.

## Funktionsanforderungen

Prüfe mindestens folgende Funktionen:
- News-Liste mit Titel, Kurzbeschreibung, Kategorien, Land/Markt und Link zum externen Originalartikel.
- Filter für Land, Thema, Zeitraum und weitere sinnvolle Kriterien.
- Kombinierbare Filter mit klarer Rücksetzung.
- Pagination oder Lazy Loading für längere Listen.
- Tab- oder Segmentlogik zur Unterscheidung von Teamwork News und Branchen News.
- Call-to-Action für Detailansicht oder externen Artikel, zum Beispiel "Mehr erfahren".
- Responsives Verhalten für Desktop, Tablet und mobile Nutzung.
- Leere Zustände, Ladezustände und Fehlerzustände.
- Optional: Möglichkeit, eigene Hinweise oder News-Vorschläge intern einzureichen.

## Design-Kontext

Der erste Design-Entwurf zeigt eine Teamwork-News-Seite mit:
- Schüco Teamwork-Net-Header und bestehender Hauptnavigation.
- Seitentitel "Alle News auf einen Blick".
- Tabs für "Teamwork News" und "Branchen News".
- Filterbereich oberhalb der Ergebnisliste.
- Kartenartige News-Teaser mit Kategorie- und Länder-Tags.
- Bildbereich je News-Teaser.
- Pagination.
- Unterem Hinweisbereich "Jetzt eigene Beiträge einreichen!".

Bewerte, welche Elemente aus dem Entwurf für ein MVP erforderlich sind und welche später ergänzt werden können.

## Aufgaben für das Advisory Board

Analysiere die Anforderung aus fachlicher, UX-, technischer, CoreMedia-, SEO/GEO-, Leadmanagement-, Analytics-, Security- und Operations-Perspektive.

Bewerte insbesondere:
- Ob eine eigenständige React-App als eingebettete Web-Komponente sinnvoll ist.
- Welche Integrationsvariante in CoreMedia und Teamwork/Intranet empfohlen wird.
- Welche API- und Datenmodellanforderungen bestehen.
- Welche Filterlogik für Nutzer sinnvoll und performant ist.
- Welche redaktionellen und rechtlichen Anforderungen durch externe Quellen entstehen.
- Wie externe Links, Quellenhinweise und Nutzungsrechte behandelt werden sollen.
- Ob Bilder aus Originalartikeln verwendet werden dürfen oder ob neutrale/kurierte Bilder erforderlich sind.
- Welche Accessibility-, Performance- und Security-Anforderungen gelten.
- Welche Analytics-Events erforderlich sind, um Nutzung und Relevanz zu messen.
- Welche MVP-Abgrenzung realistisch ist.
- Welche Roadmap für spätere Ausbaustufen empfohlen wird.

## Erwartete Ergebnisstruktur

Die finale Empfehlung muss folgende Struktur enthalten:

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

## Zusätzliche Bewertungsfragen

- Welche Inhalte sollen im Intranet indexierbar oder auffindbar sein, obwohl die Originalartikel extern liegen?
- Soll die App nur kuratierte News anzeigen oder auch automatisch recherchierte, noch nicht redaktionell geprüfte News?
- Welche Rollen benötigen Pflege-, Freigabe- oder Administrationsfunktionen?
- Wie werden Länder, Themen und Kategorien zentral gepflegt?
- Wie aktuell müssen die News sein und welche Aktualisierungsfrequenz ist erforderlich?
- Welche Anforderungen entstehen durch Mehrsprachigkeit und internationale Märkte?
- Wie wird verhindert, dass externe Links veralten oder auf problematische Inhalte führen?
- Welche Datenschutz- und Compliance-Aspekte gelten beim Tracking von News-Interaktionen im Intranet?

## Ergebnisablage

Speichere Reviews und finale Empfehlung in einem eigenen Unterverzeichnis unter `outputs/`, zum Beispiel:

```text
outputs/branchennews_teamwork/
```
