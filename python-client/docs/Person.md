# Person

Liefert Personenstammdaten zu einer Person

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**nachname** | **str** |  | 
**vorname** | **str** |  | 
**typ** | **str** |  | 
**aktualisiert** | **datetime** | Letzte Aktualisierung der Entität | 
**titel** | **str** |  | 
**namenszusatz** | **str** |  | [optional] 
**wahlperiode** | **int** | Wahlperiode des ersten zugehörigen Dokuments | [optional] 
**basisdatum** | **date** | Datum des ersten zugehörigen Dokuments | [optional] 
**datum** | **date** | Datum des letzten zugehörigen Dokuments | [optional] 
**person_roles** | [**[PersonRole]**](PersonRole.md) | Nebeneinträge mit bspw. abweichenden Funktionen oder Namensänderungen | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


