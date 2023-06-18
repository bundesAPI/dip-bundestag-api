# Drucksache

Liefert Metadaten zu einer Drucksache.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**drucksachetyp** | **str** |  | 
**dokumentnummer** | **str** |  | 
**herausgeber** | **str** |  | 
**datum** | **date** |  | 
**aktualisiert** | **datetime** | Letzte Aktualisierung der Entität | 
**titel** | **str** |  | 
**autoren_anzahl** | **int** | Gesamtzahl der Autor:innen | 
**fundstelle** | [**Fundstelle**](Fundstelle.md) |  | 
**vorgangsbezug_anzahl** | **int** | Gesamtzahl der zugehörigen Vorgänge | 
**typ** | **str** |  | defaults to "Dokument"
**dokumentart** | **str** |  | defaults to "Drucksache"
**wahlperiode** | **int** |  | [optional] 
**autoren_anzeige** | [**[DrucksacheAutorenAnzeigeInner]**](DrucksacheAutorenAnzeigeInner.md) | Zusammenfassung der ersten 4 zur Anzeige markierten Autor:innen | [optional] 
**pdf_hash** | **str** | MD5-Prüfsumme der PDF-Datei | [optional] 
**urheber** | [**[Urheber]**](Urheber.md) |  | [optional] 
**vorgangsbezug** | [**[Vorgangsbezug]**](Vorgangsbezug.md) | Zusammenfassung der ersten 4 zugehörigen Vorgänge | [optional] 
**ressort** | [**[Ressort]**](Ressort.md) |  | [optional] 
**anlagen** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


