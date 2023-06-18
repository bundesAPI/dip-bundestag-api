# Vorgang

Liefert Metadaten zu einem Vorgang.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**vorgangstyp** | **str** |  | 
**wahlperiode** | **int** |  | 
**aktualisiert** | **datetime** | Letzte Aktualisierung der Entität | 
**titel** | **str** |  | 
**typ** | **str** |  | defaults to "Vorgang"
**beratungsstand** | **str** |  | [optional] 
**initiative** | **[str]** |  | [optional] 
**datum** | **date** | Datierung des letzten zugehörigen Dokuments | [optional] 
**abstract** | **str** |  | [optional] 
**sachgebiet** | **[str]** |  | [optional] 
**deskriptor** | [**[VorgangDeskriptor]**](VorgangDeskriptor.md) |  | [optional] 
**gesta** | **str** | GESTA-Ordnungsnummer | [optional] 
**zustimmungsbeduerftigkeit** | **[str]** |  | [optional] 
**kom** | **str** | KOM-Nr. | [optional] 
**ratsdok** | **str** | Ratsdok-Nr. | [optional] 
**verkuendung** | [**[Verkuendung]**](Verkuendung.md) |  | [optional] 
**inkrafttreten** | [**[Inkrafttreten]**](Inkrafttreten.md) |  | [optional] 
**archiv** | **str** | Archivsignatur | [optional] 
**mitteilung** | **str** |  | [optional] 
**vorgang_verlinkung** | [**[VorgangVerlinkung]**](VorgangVerlinkung.md) |  | [optional] 
**sek** | **str** | SEK-Nr. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


