# dip_bundestag.PlenarprotokolleApi

All URIs are relative to *https://search.dip.bundestag.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_plenarprotokoll**](PlenarprotokolleApi.md#get_plenarprotokoll) | **GET** /plenarprotokoll/{id} | Liefert Metadaten zu einem Plenarprotokoll
[**get_plenarprotokoll_list**](PlenarprotokolleApi.md#get_plenarprotokoll_list) | **GET** /plenarprotokoll | Liefert eine Liste von Metadaten zu Plenarprotokollen
[**get_plenarprotokoll_text**](PlenarprotokolleApi.md#get_plenarprotokoll_text) | **GET** /plenarprotokoll-text/{id} | Liefert Volltext und Metadaten zu einem Plenarprotokoll
[**get_plenarprotokoll_text_list**](PlenarprotokolleApi.md#get_plenarprotokoll_text_list) | **GET** /plenarprotokoll-text | Liefert eine Liste von Volltexten und Metadaten zu Plenarprotokollen


# **get_plenarprotokoll**
> Plenarprotokoll get_plenarprotokoll(id)

Liefert Metadaten zu einem Plenarprotokoll

### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyQuery):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import plenarprotokolle_api
from deutschland.dip_bundestag.model.plenarprotokoll import Plenarprotokoll
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
    api_instance = plenarprotokolle_api.PlenarprotokolleApi(api_client)
    id = 1 # int | 
    format = "json" # str | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. (optional) if omitted the server will use the default value of "json"

    # example passing only required values which don't have defaults set
    try:
        # Liefert Metadaten zu einem Plenarprotokoll
        api_response = api_instance.get_plenarprotokoll(id)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling PlenarprotokolleApi->get_plenarprotokoll: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert Metadaten zu einem Plenarprotokoll
        api_response = api_instance.get_plenarprotokoll(id, format=format)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling PlenarprotokolleApi->get_plenarprotokoll: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **format** | **str**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] if omitted the server will use the default value of "json"

### Return type

[**Plenarprotokoll**](Plenarprotokoll.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadaten eines Plenarprotokolls |  -  |
**401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |
**404** | Die angefragte Entität wurde nicht gefunden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plenarprotokoll_list**
> PlenarprotokollListResponse get_plenarprotokoll_list()

Liefert eine Liste von Metadaten zu Plenarprotokollen

### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyQuery):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import plenarprotokolle_api
from deutschland.dip_bundestag.model.zuordnung import Zuordnung
from deutschland.dip_bundestag.model.plenarprotokoll_list_response import PlenarprotokollListResponse
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
    api_instance = plenarprotokolle_api.PlenarprotokolleApi(api_client)
    f_aktualisiert_start = dateutil_parser('2022-06-01T15:00:00+02:00') # datetime | Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  (optional)
    f_aktualisiert_end = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  (optional)
    f_datum_start = dateutil_parser('2021-01-11').date() # date | Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  (optional)
    f_datum_end = dateutil_parser('2021-01-15').date() # date | Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  (optional)
    f_wahlperiode = 1 # int | Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren.  (optional)
    f_id = 1 # int | ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  (optional)
    f_dokumentnummer = "f.dokumentnummer_example" # str | Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren.  (optional)
    f_zuordnung = Zuordnung("BT") # Zuordnung | Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer (optional)
    format = "json" # str | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. (optional) if omitted the server will use the default value of "json"
    cursor = "cursor_example" # str | Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert eine Liste von Metadaten zu Plenarprotokollen
        api_response = api_instance.get_plenarprotokoll_list(f_aktualisiert_start=f_aktualisiert_start, f_aktualisiert_end=f_aktualisiert_end, f_datum_start=f_datum_start, f_datum_end=f_datum_end, f_wahlperiode=f_wahlperiode, f_id=f_id, f_dokumentnummer=f_dokumentnummer, f_zuordnung=f_zuordnung, format=format, cursor=cursor)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling PlenarprotokolleApi->get_plenarprotokoll_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_aktualisiert_start** | **datetime**| Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  | [optional]
 **f_aktualisiert_end** | **datetime**| Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  | [optional]
 **f_datum_start** | **date**| Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  | [optional]
 **f_datum_end** | **date**| Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  | [optional]
 **f_wahlperiode** | **int**| Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren.  | [optional]
 **f_id** | **int**| ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  | [optional]
 **f_dokumentnummer** | **str**| Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren.  | [optional]
 **f_zuordnung** | **Zuordnung**| Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer | [optional]
 **format** | **str**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] if omitted the server will use the default value of "json"
 **cursor** | **str**| Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  | [optional]

### Return type

[**PlenarprotokollListResponse**](PlenarprotokollListResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadaten zu Plenarprotokollen |  -  |
**400** | Syntaxfehler in einem der Anfrageparameter |  -  |
**401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plenarprotokoll_text**
> PlenarprotokollText get_plenarprotokoll_text(id)

Liefert Volltext und Metadaten zu einem Plenarprotokoll

### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyQuery):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import plenarprotokolle_api
from deutschland.dip_bundestag.model.plenarprotokoll_text import PlenarprotokollText
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
    api_instance = plenarprotokolle_api.PlenarprotokolleApi(api_client)
    id = 1 # int | 
    format = "json" # str | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. (optional) if omitted the server will use the default value of "json"

    # example passing only required values which don't have defaults set
    try:
        # Liefert Volltext und Metadaten zu einem Plenarprotokoll
        api_response = api_instance.get_plenarprotokoll_text(id)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling PlenarprotokolleApi->get_plenarprotokoll_text: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert Volltext und Metadaten zu einem Plenarprotokoll
        api_response = api_instance.get_plenarprotokoll_text(id, format=format)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling PlenarprotokolleApi->get_plenarprotokoll_text: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **format** | **str**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] if omitted the server will use the default value of "json"

### Return type

[**PlenarprotokollText**](PlenarprotokollText.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Volltext und Metadaten eines Plenarprotokolls |  -  |
**401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |
**404** | Die angefragte Entität wurde nicht gefunden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plenarprotokoll_text_list**
> PlenarprotokollTextListResponse get_plenarprotokoll_text_list()

Liefert eine Liste von Volltexten und Metadaten zu Plenarprotokollen

### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyQuery):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import plenarprotokolle_api
from deutschland.dip_bundestag.model.zuordnung import Zuordnung
from deutschland.dip_bundestag.model.get_vorgang_list400_response import GetVorgangList400Response
from deutschland.dip_bundestag.model.plenarprotokoll_text_list_response import PlenarprotokollTextListResponse
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
    api_instance = plenarprotokolle_api.PlenarprotokolleApi(api_client)
    f_aktualisiert_start = dateutil_parser('2022-06-01T15:00:00+02:00') # datetime | Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  (optional)
    f_aktualisiert_end = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  (optional)
    f_datum_start = dateutil_parser('2021-01-11').date() # date | Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  (optional)
    f_datum_end = dateutil_parser('2021-01-15').date() # date | Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  (optional)
    f_wahlperiode = 1 # int | Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren.  (optional)
    f_id = 1 # int | ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  (optional)
    f_dokumentnummer = "f.dokumentnummer_example" # str | Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren.  (optional)
    f_zuordnung = Zuordnung("BT") # Zuordnung | Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer (optional)
    format = "json" # str | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. (optional) if omitted the server will use the default value of "json"
    cursor = "cursor_example" # str | Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert eine Liste von Volltexten und Metadaten zu Plenarprotokollen
        api_response = api_instance.get_plenarprotokoll_text_list(f_aktualisiert_start=f_aktualisiert_start, f_aktualisiert_end=f_aktualisiert_end, f_datum_start=f_datum_start, f_datum_end=f_datum_end, f_wahlperiode=f_wahlperiode, f_id=f_id, f_dokumentnummer=f_dokumentnummer, f_zuordnung=f_zuordnung, format=format, cursor=cursor)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling PlenarprotokolleApi->get_plenarprotokoll_text_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f_aktualisiert_start** | **datetime**| Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  | [optional]
 **f_aktualisiert_end** | **datetime**| Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  | [optional]
 **f_datum_start** | **date**| Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  | [optional]
 **f_datum_end** | **date**| Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  | [optional]
 **f_wahlperiode** | **int**| Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren.  | [optional]
 **f_id** | **int**| ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  | [optional]
 **f_dokumentnummer** | **str**| Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren.  | [optional]
 **f_zuordnung** | **Zuordnung**| Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer | [optional]
 **format** | **str**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] if omitted the server will use the default value of "json"
 **cursor** | **str**| Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  | [optional]

### Return type

[**PlenarprotokollTextListResponse**](PlenarprotokollTextListResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Volltext und Metadaten zu Plenarprotokollen |  -  |
**400** | Syntaxfehler in einem der Anfrageparameter |  -  |
**401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

