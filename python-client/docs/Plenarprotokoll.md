# Plenarprotokoll

Liefert Metadaten zu einem Plenarprotokoll.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**dokumentnummer** | **str** |  | 
**herausgeber** | [**Zuordnung**](Zuordnung.md) |  | 
**datum** | **date** |  | 
**aktualisiert** | **datetime** | Letzte Aktualisierung der Entität | 
**titel** | **str** |  | 
**fundstelle** | [**Fundstelle**](Fundstelle.md) |  | 
**vorgangsbezug_anzahl** | **int** | Gesamtzahl der zugehörigen Vorgänge | 
**dokumentart** | **str** |  | defaults to "Plenarprotokoll"
**typ** | **str** |  | defaults to "Dokument"
**wahlperiode** | **int** |  | [optional] 
**pdf_hash** | **str** | MD5-Prüfsumme der PDF-Datei | [optional] 
**vorgangsbezug** | [**[Vorgangsbezug]**](Vorgangsbezug.md) | Zusammenfassung der ersten 4 zugehörigen Vorgänge | [optional] 
**sitzungsbemerkung** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


