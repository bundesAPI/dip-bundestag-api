# Aktivitaet

Liefert Metadaten zu einer Aktivität.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**aktivitaetsart** | **str** |  | 
**dokumentart** | **str** |  | 
**wahlperiode** | **int** |  | 
**datum** | **date** |  | 
**aktualisiert** | **datetime** | Letzte Aktualisierung der Entität oder des zugehörigen Dokuments | 
**titel** | **str** |  | 
**fundstelle** | [**Fundstelle**](Fundstelle.md) |  | 
**vorgangsbezug_anzahl** | **int** | Gesamtzahl der zugehörigen Vorgänge | 
**typ** | **str** |  | defaults to "Aktivität"
**vorgangsbezug** | [**[Vorgangspositionbezug]**](Vorgangspositionbezug.md) | Zusammenfassung der ersten 4 zugehörigen Vorgänge | [optional] 
**deskriptor** | [**[Deskriptor]**](Deskriptor.md) |  | [optional] 
**abstract** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


