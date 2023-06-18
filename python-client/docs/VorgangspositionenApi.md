# dip_bundestag.VorgangspositionenApi

All URIs are relative to *https://search.dip.bundestag.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vorgangsposition**](VorgangspositionenApi.md#get_vorgangsposition) | **GET** /vorgangsposition/{id} | Liefert Metadaten zu einer Vorgangsposition
[**get_vorgangsposition_list**](VorgangspositionenApi.md#get_vorgangsposition_list) | **GET** /vorgangsposition | Liefert eine Liste von Metadaten zu Vorgangspositionen


# **get_vorgangsposition**
> Vorgangsposition get_vorgangsposition(id)

Liefert Metadaten zu einer Vorgangsposition

### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyQuery):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import vorgangspositionen_api
from deutschland.dip_bundestag.model.vorgangsposition import Vorgangsposition
from deutschland.dip_bundestag.model.get_vorgang_list401_response import GetVorgangList401Response
from deutschland.dip_bundestag.model.get_vorgang404_response import GetVorgang404Response
from pprint import pprint
# Defining the host is optional and defaults to https://search.dip.bundestag.de/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dip_bundestag.Configuration(
    host = "https://search.dip.bundestag.de/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeader
configuration.api_key['ApiKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyHeader'] = 'Bearer'

# Configure API key authorization: ApiKeyQuery
configuration.api_key['ApiKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyQuery'] = 'Bearer'

# Enter a context with an instance of the API client
with dip_bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vorgangspositionen_api.VorgangspositionenApi(api_client)
    id = 1 # int | 
    format = "json" # str | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. (optional) if omitted the server will use the default value of "json"

    # example passing only required values which don't have defaults set
    try:
        # Liefert Metadaten zu einer Vorgangsposition
        api_response = api_instance.get_vorgangsposition(id)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling VorgangspositionenApi->get_vorgangsposition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert Metadaten zu einer Vorgangsposition
        api_response = api_instance.get_vorgangsposition(id, format=format)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling VorgangspositionenApi->get_vorgangsposition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **format** | **str**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] if omitted the server will use the default value of "json"

### Return type

[**Vorgangsposition**](Vorgangsposition.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadaten einer Vorgangsposition |  -  |
**401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |
**404** | Die angefragte Entität wurde nicht gefunden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vorgangsposition_list**
> VorgangspositionListResponse get_vorgangsposition_list()

Liefert eine Liste von Metadaten zu Vorgangspositionen

### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyQuery):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import vorgangspositionen_api
from deutschland.dip_bundestag.model.zuordnung import Zuordnung
from deutschland.dip_bundestag.model.vorgangsposition_list_response import VorgangspositionListResponse
from deutschland.dip_bundestag.model.get_vorgang_list400_response import GetVorgangList400Response
from deutschland.dip_bundestag.model.get_vorgang_list401_response import GetVorgangList401Response
from pprint import pprint
# Defining the host is optional and defaults to https://search.dip.bundestag.de/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dip_bundestag.Configuration(
    host = "https://search.dip.bundestag.de/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeader
configuration.api_key['ApiKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyHeader'] = 'Bearer'

# Configure API key authorization: ApiKeyQuery
configuration.api_key['ApiKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyQuery'] = 'Bearer'

# Enter a context with an instance of the API client
with dip_bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vorgangspositionen_api.VorgangspositionenApi(api_client)
    f_aktualisiert_start = dateutil_parser('2022-06-01T15:00:00+02:00') # datetime | Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  (optional)
    f_aktualisiert_end = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  (optional)
    f_aktivitaet = 1 # int | ID einer verknüpften Aktivität  Selektiert alle Entitäten, die mit der angegebenen Aktivität verknüpft sind.  (optional)
    f_datum_start = dateutil_parser('2021-01-11').date() # date | Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  (optional)
    f_datum_end = dateutil_parser('2021-01-15').date() # date | Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  (optional)
    f_wahlperiode = 1 # int | Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren.  (optional)
    f_drucksache = 1 # int | ID einer verknüpften Drucksache  Selektiert alle Entitäten, die mit der angegebenen Drucksache verknüpft sind.  (optional)
    f_id = 1 # int | ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  (optional)
    f_plenarprotokoll = 1 # int | ID eines verknüpften Plenarprotokolls  Selektiert alle Entitäten, die mit dem angegebenen Plenarprotokoll verknüpft sind.  (optional)
    f_vorgang = 1 # int | ID eines verknüpften Vorgangs  Selektiert alle Entitäten, die mit dem angegebenen Vorgang verknüpft sind.  (optional)
    f_dokumentart = "Drucksache" # str | Drucksache oder Plenarprotokoll  Selektiert alle Entitäten, die mit der angegebenen Dokumentart verknüpft sind.  (optional)
    f_dokumentnummer = "f.dokumentnummer_example" # str | Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren.  (optional)
    f_drucksachetyp = "f.drucksachetyp_example" # str | Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind.  (optional)
    f_frage_nummer = "f.frage_nummer_example" # str | Fragenummer/Listenziffer  Selektiert alle Entitäten, die mit der angegebenen Fragenummer in einer Drucksache verknüpft sind. Kann wiederholt werden, um mehrere Fragenummern zu selektieren.  (optional)
    f_zuordnung = Zuordnung("BT") # Zuordnung | Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer (optional)
    format = "json" # str | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. (optional) if omitted the server will use the default value of "json"
    cursor = "cursor_example" # str | Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert eine Liste von Metadaten zu Vorgangspositionen
        api_response = api_instance.get_vorgangsposition_list(f_aktualisiert_start=f_aktualisiert_start, f_aktualisiert_end=f_aktualisiert_end, f_aktivitaet=f_aktivitaet, f_datum_start=f_datum_start, f_datum_end=f_datum_end, f_wahlperiode=f_wahlperiode, f_drucksache=f_drucksache, f_id=f_id, f_plenarprotokoll=f_plenarprotokoll, f_vorgang=f_vorgang, f_dokumentart=f_dokumentart, f_dokumentnummer=f_dokumentnummer, f_drucksachetyp=f_drucksachetyp, f_frage_nummer=f_frage_nummer, f_zuordnung=f_zuordnung, format=format, cursor=cursor)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling VorgangspositionenApi->get_vorgangsposition_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_aktualisiert_start** | **datetime**| Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  | [optional]
 **f_aktualisiert_end** | **datetime**| Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  | [optional]
 **f_aktivitaet** | **int**| ID einer verknüpften Aktivität  Selektiert alle Entitäten, die mit der angegebenen Aktivität verknüpft sind.  | [optional]
 **f_datum_start** | **date**| Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  | [optional]
 **f_datum_end** | **date**| Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  | [optional]
 **f_wahlperiode** | **int**| Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren.  | [optional]
 **f_drucksache** | **int**| ID einer verknüpften Drucksache  Selektiert alle Entitäten, die mit der angegebenen Drucksache verknüpft sind.  | [optional]
 **f_id** | **int**| ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  | [optional]
 **f_plenarprotokoll** | **int**| ID eines verknüpften Plenarprotokolls  Selektiert alle Entitäten, die mit dem angegebenen Plenarprotokoll verknüpft sind.  | [optional]
 **f_vorgang** | **int**| ID eines verknüpften Vorgangs  Selektiert alle Entitäten, die mit dem angegebenen Vorgang verknüpft sind.  | [optional]
 **f_dokumentart** | **str**| Drucksache oder Plenarprotokoll  Selektiert alle Entitäten, die mit der angegebenen Dokumentart verknüpft sind.  | [optional]
 **f_dokumentnummer** | **str**| Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren.  | [optional]
 **f_drucksachetyp** | **str**| Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind.  | [optional]
 **f_frage_nummer** | **str**| Fragenummer/Listenziffer  Selektiert alle Entitäten, die mit der angegebenen Fragenummer in einer Drucksache verknüpft sind. Kann wiederholt werden, um mehrere Fragenummern zu selektieren.  | [optional]
 **f_zuordnung** | **Zuordnung**| Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer | [optional]
 **format** | **str**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] if omitted the server will use the default value of "json"
 **cursor** | **str**| Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  | [optional]

### Return type

[**VorgangspositionListResponse**](VorgangspositionListResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadaten zu Vorgangspositionen |  -  |
**400** | Syntaxfehler in einem der Anfrageparameter |  -  |
**401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

