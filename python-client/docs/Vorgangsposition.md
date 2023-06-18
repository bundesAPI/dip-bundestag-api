# Vorgangsposition

Liefert Metadaten zu einer Vorgangsposition (Vorgangsschritt).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**vorgangsposition** | **str** |  | 
**zuordnung** | [**Zuordnung**](Zuordnung.md) |  | 
**gang** | **bool** | Alle Vorgangsschritte, die von besonderer Bedeutung für den Fortgang der Beratung sind, werden durch das Attribut &#x60;gang: true&#x60; gekennzeichnet.  Ist ein solcher Vorgangsschritt mit einer Drucksache verknüpft, werden im Frontend unter der Benennung \&quot;Wichtige Drucksachen\&quot; Herausgeber, Nummer und Typ sowie das Datum der entsprechenden Drucksachen ausgegeben (z.B. BT-Drs 18/13014 (Beschlussempfehlung), 28.06.2017).  Ist er mit einem Plenarprotokoll verknüpft, werden im Frontend unter der Benennung \&quot;Plenum\&quot; der Klartext der Vorgangsposition, Datum, Herausgeber und Nummer des Plenarprotokolls mit Anfangsseite/Quadrant und Endseite/Quadrant dargestellt (z.B. 2. Beratung: 29.06.2017, BT-PlPr 18/243, S. 24964C - 24973C).  | 
**fortsetzung** | **bool** | Erstreckt sich eine Beratung über mehrere Plenarprotokolle, so müssen entsprechend viele Vorgangsschritte mit je gleicher Vorgangsposition im Vorgangsablauf angelegt werden. Der zweite und jeder weitere dieser Schritte wird dann als \&quot;Fortsetzung\&quot; gekennzeichnet (Attribut &#x60;fortsetzung: true&#x60;).  Für die Beratung des Gesetzentwurfs für die Feststellung des Haushaltsplanes (Haushaltsberatungen) gelten abweichende Regelungen.  | 
**nachtrag** | **bool** | Eine Auswertungseinheit eines Plenarprotokolls kann nur an genau einen Vorgangsschritt angebunden werden.  Müssen aber mehrere Auswertungseinheiten für einen Vorgangsschritt gebildet werden (weil die Ergänzung einer Rede erst in einem späteren Protokoll erscheint oder weil sich z.B. bei einer Verbundenen Beratung (§ 24 GO-BT) nicht alle Schriftlichen Erklärungen nach § 31 GO-BT auf sämtliche Vorlagen beziehen),  dann müssen im Vorgangsablauf mehrere Vorgangsschritte mit der gleichen Vorgangsposition angelegt werden. Der zweite und jeder weitere dieser Schritte wird dann als \&quot;Nachtrag\&quot; gekennzeichnet (Attribut &#x60;nachtrag: true&#x60;)  | 
**vorgangstyp** | **str** | Vorgangstyp des zugehörigen Vorgangs | 
**titel** | **str** | Titel des zugehörigen Vorgangs | 
**dokumentart** | **str** |  | 
**vorgang_id** | **str** | ID des zugehörigen Vorgangs | 
**datum** | **date** | Datum des zugehörigen Dokuments | 
**aktualisiert** | **datetime** | Letzte Aktualisierung der Entität oder des zugehörigen Dokuments | 
**fundstelle** | [**Fundstelle**](Fundstelle.md) |  | 
**aktivitaet_anzahl** | **int** | Gesamtzahl der zugehörigen Aktivitäten | 
**typ** | **str** |  | defaults to "Vorgangsposition"
**urheber** | [**[Urheber]**](Urheber.md) |  | [optional] 
**ueberweisung** | [**[Ueberweisung]**](Ueberweisung.md) |  | [optional] 
**aktivitaet_anzeige** | [**[AktivitaetAnzeige]**](AktivitaetAnzeige.md) | Zusammenfassung der ersten 4 zur Anzeige vorgesehenen Aktivitäten | [optional] 
**ressort** | [**[Ressort]**](Ressort.md) |  | [optional] 
**beschlussfassung** | [**[Beschlussfassung]**](Beschlussfassung.md) |  | [optional] 
**ratsdok** | **str** | Ratsdok-Nr. | [optional] 
**kom** | **str** | KOM-Nr. | [optional] 
**sek** | **str** | SEK-Nr. | [optional] 
**mitberaten** | [**[Vorgangspositionbezug]**](Vorgangspositionbezug.md) | Es ist eine häufig geübte Praxis, mehrere thematisch verwandte Vorlagen (z.B. konkurrierende Anträge der verschiedenen Fraktionen zum Thema Diesel-Fahrverbote) in einer Debatte gemeinsam zu beraten (\&quot;Zusammenberatung\&quot;).  &#x60;mitberaten&#x60; liefert, von einem Vorgang ausgehend, alle anderen Vorgänge, die Gegenstand der Zusammenberatung sind.  | [optional] 
**abstract** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


