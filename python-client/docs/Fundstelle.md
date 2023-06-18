# Fundstelle

Liefert im Vorgangsablauf das zu einem Vorgangsschritt gehörende Dokument (Drucksache oder Protokoll).   Beispiel: „BT-Drucksache 19/1 (Antrag Fraktion der CDU/CSU)“ oder beim Vorgangsschritt Beratung „BT-Plenarprotokoll 19/1, S. 4C-12A“. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID einer Drucksache oder eines Plenarprotokolls | 
**dokumentart** | **str** |  | 
**dokumentnummer** | **str** |  | 
**datum** | **date** |  | 
**herausgeber** | [**Zuordnung**](Zuordnung.md) |  | 
**urheber** | **[str]** |  | 
**pdf_url** | **str** |  | [optional] 
**drucksachetyp** | **str** |  | [optional] 
**verteildatum** | **date** |  | [optional] 
**seite** | **str** |  | [optional] 
**anfangsseite** | **int** |  | [optional] 
**endseite** | **int** |  | [optional] 
**anfangsquadrant** | [**Quadrant**](Quadrant.md) |  | [optional] 
**endquadrant** | [**Quadrant**](Quadrant.md) |  | [optional] 
**frage_nummer** | **str** |  | [optional] 
**anlagen** | **str** |  | [optional] 
**top** | **int** |  | [optional] 
**top_zusatz** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


