# dip_bundestag.DrucksachenApi

All URIs are relative to *https://search.dip.bundestag.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_drucksache**](DrucksachenApi.md#get_drucksache) | **GET** /drucksache/{id} | Liefert Metadaten zu einer Drucksache
[**get_drucksache_list**](DrucksachenApi.md#get_drucksache_list) | **GET** /drucksache | Liefert eine Liste von Metadaten zu Drucksachen
[**get_drucksache_text**](DrucksachenApi.md#get_drucksache_text) | **GET** /drucksache-text/{id} | Liefert Volltext und Metadaten zu einer Drucksache
[**get_drucksache_text_list**](DrucksachenApi.md#get_drucksache_text_list) | **GET** /drucksache-text | Liefert eine Liste von Volltexten und Metadaten zu Drucksachen


# **get_drucksache**
> Drucksache get_drucksache(id)

Liefert Metadaten zu einer Drucksache

### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyQuery):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import drucksachen_api
from deutschland.dip_bundestag.model.drucksache import Drucksache
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
    api_instance = drucksachen_api.DrucksachenApi(api_client)
    id = 1 # int | 
    format = "json" # str | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. (optional) if omitted the server will use the default value of "json"

    # example passing only required values which don't have defaults set
    try:
        # Liefert Metadaten zu einer Drucksache
        api_response = api_instance.get_drucksache(id)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling DrucksachenApi->get_drucksache: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert Metadaten zu einer Drucksache
        api_response = api_instance.get_drucksache(id, format=format)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling DrucksachenApi->get_drucksache: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **format** | **str**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] if omitted the server will use the default value of "json"

### Return type

[**Drucksache**](Drucksache.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadaten einer Drucksache |  -  |
**401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |
**404** | Die angefragte Entität wurde nicht gefunden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drucksache_list**
> DrucksacheListResponse get_drucksache_list()

Liefert eine Liste von Metadaten zu Drucksachen

### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyQuery):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import drucksachen_api
from deutschland.dip_bundestag.model.zuordnung import Zuordnung
from deutschland.dip_bundestag.model.get_vorgang_list400_response import GetVorgangList400Response
from deutschland.dip_bundestag.model.drucksache_list_response import DrucksacheListResponse
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
    api_instance = drucksachen_api.DrucksachenApi(api_client)
    f_aktualisiert_start = dateutil_parser('2022-06-01T15:00:00+02:00') # datetime | Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  (optional)
    f_aktualisiert_end = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  (optional)
    f_datum_start = dateutil_parser('2021-01-11').date() # date | Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  (optional)
    f_datum_end = dateutil_parser('2021-01-15').date() # date | Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  (optional)
    f_wahlperiode = 1 # int | Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren.  (optional)
    f_id = 1 # int | ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  (optional)
    f_dokumentnummer = "f.dokumentnummer_example" # str | Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren.  (optional)
    f_drucksachetyp = "f.drucksachetyp_example" # str | Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind.  (optional)
    f_zuordnung = Zuordnung("BT") # Zuordnung | Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer (optional)
    format = "json" # str | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. (optional) if omitted the server will use the default value of "json"
    cursor = "cursor_example" # str | Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert eine Liste von Metadaten zu Drucksachen
        api_response = api_instance.get_drucksache_list(f_aktualisiert_start=f_aktualisiert_start, f_aktualisiert_end=f_aktualisiert_end, f_datum_start=f_datum_start, f_datum_end=f_datum_end, f_wahlperiode=f_wahlperiode, f_id=f_id, f_dokumentnummer=f_dokumentnummer, f_drucksachetyp=f_drucksachetyp, f_zuordnung=f_zuordnung, format=format, cursor=cursor)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling DrucksachenApi->get_drucksache_list: %s\n" % e)
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
 **f_drucksachetyp** | **str**| Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind.  | [optional]
 **f_zuordnung** | **Zuordnung**| Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer | [optional]
 **format** | **str**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] if omitted the server will use the default value of "json"
 **cursor** | **str**| Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  | [optional]

### Return type

[**DrucksacheListResponse**](DrucksacheListResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadaten zu Drucksachen |  -  |
**400** | Syntaxfehler in einem der Anfrageparameter |  -  |
**401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drucksache_text**
> DrucksacheText get_drucksache_text(id)

Liefert Volltext und Metadaten zu einer Drucksache

### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyQuery):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import drucksachen_api
from deutschland.dip_bundestag.model.drucksache_text import DrucksacheText
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
    api_instance = drucksachen_api.DrucksachenApi(api_client)
    id = 1 # int | 
    format = "json" # str | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. (optional) if omitted the server will use the default value of "json"

    # example passing only required values which don't have defaults set
    try:
        # Liefert Volltext und Metadaten zu einer Drucksache
        api_response = api_instance.get_drucksache_text(id)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling DrucksachenApi->get_drucksache_text: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert Volltext und Metadaten zu einer Drucksache
        api_response = api_instance.get_drucksache_text(id, format=format)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling DrucksachenApi->get_drucksache_text: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **format** | **str**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] if omitted the server will use the default value of "json"

### Return type

[**DrucksacheText**](DrucksacheText.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Volltext und Metadaten einer Drucksache |  -  |
**401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |
**404** | Die angefragte Entität wurde nicht gefunden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drucksache_text_list**
> DrucksacheTextListResponse get_drucksache_text_list()

Liefert eine Liste von Volltexten und Metadaten zu Drucksachen

### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyQuery):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import drucksachen_api
from deutschland.dip_bundestag.model.zuordnung import Zuordnung
from deutschland.dip_bundestag.model.get_vorgang_list400_response import GetVorgangList400Response
from deutschland.dip_bundestag.model.drucksache_text_list_response import DrucksacheTextListResponse
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
    api_instance = drucksachen_api.DrucksachenApi(api_client)
    f_aktualisiert_start = dateutil_parser('2022-06-01T15:00:00+02:00') # datetime | Frühestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  (optional)
    f_aktualisiert_end = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Spätestes Aktualisierungsdatum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten Aktualisierungsdatum.  (optional)
    f_datum_start = dateutil_parser('2021-01-11').date() # date | Frühestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  (optional)
    f_datum_end = dateutil_parser('2021-01-15').date() # date | Spätestes Datum der Entität  Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente herangezogen.  (optional)
    f_wahlperiode = 1 # int | Nummer der Wahlperiode  Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann wiederholt werden, um mehrere Wahlperioden zu selektieren.  (optional)
    f_id = 1 # int | ID der Entität  Kann wiederholt werden, um mehrere Entitäten zu selektieren.  (optional)
    f_dokumentnummer = "f.dokumentnummer_example" # str | Dokumentnummer einer Drucksache oder eines Plenarprotokolls  Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren.  (optional)
    f_drucksachetyp = "f.drucksachetyp_example" # str | Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind.  (optional)
    f_zuordnung = Zuordnung("BT") # Zuordnung | Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer (optional)
    format = "json" # str | Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. (optional) if omitted the server will use the default value of "json"
    cursor = "cursor_example" # str | Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert eine Liste von Volltexten und Metadaten zu Drucksachen
        api_response = api_instance.get_drucksache_text_list(f_aktualisiert_start=f_aktualisiert_start, f_aktualisiert_end=f_aktualisiert_end, f_datum_start=f_datum_start, f_datum_end=f_datum_end, f_wahlperiode=f_wahlperiode, f_id=f_id, f_dokumentnummer=f_dokumentnummer, f_drucksachetyp=f_drucksachetyp, f_zuordnung=f_zuordnung, format=format, cursor=cursor)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling DrucksachenApi->get_drucksache_text_list: %s\n" % e)
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
 **f_drucksachetyp** | **str**| Typ der Drucksache  Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind.  | [optional]
 **f_zuordnung** | **Zuordnung**| Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder Europakammer | [optional]
 **format** | **str**| Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder XML. | [optional] if omitted the server will use the default value of "json"
 **cursor** | **str**| Position des Cursors zur Anfrage weiterer Entitäten  Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr ändert. Dies signalisiert, dass alle Entitäten geladen wurden.  | [optional]

### Return type

[**DrucksacheTextListResponse**](DrucksacheTextListResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Volltext und Metadaten zu Drucksachen |  -  |
**400** | Syntaxfehler in einem der Anfrageparameter |  -  |
**401** | Ein gültiger API-Key ist für alle Anfragen erforderlich. Dieser kann entweder im HTTP Authorization Header oder als Anfrageparameter apikey gesendet werden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

