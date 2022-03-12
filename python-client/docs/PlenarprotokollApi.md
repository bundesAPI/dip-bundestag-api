# dip_bundestag.PlenarprotokollApi

All URIs are relative to *https://search.dip.bundestag.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plenarprotokoll**](PlenarprotokollApi.md#plenarprotokoll) | **GET** /plenarprotokoll | Liste aller Plenarprotokolle
[**plenarprotokoll_id**](PlenarprotokollApi.md#plenarprotokoll_id) | **GET** /plenarprotokoll/{id} | Metadaten zu Plenarprotokoll
[**plenarprotokoll_text**](PlenarprotokollApi.md#plenarprotokoll_text) | **GET** /plenarprotokoll-text | Liste aller Volltexte der Plenarprotokolle
[**plenarprotokoll_text_id_get**](PlenarprotokollApi.md#plenarprotokoll_text_id_get) | **GET** /plenarprotokoll-text/{id} | Volltexte der Plenarprotokolle


# **plenarprotokoll**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} plenarprotokoll()

Liste aller Plenarprotokolle

Liste aller Plenarprotokolle

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import plenarprotokoll_api
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dip_bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plenarprotokoll_api.PlenarprotokollApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste aller Plenarprotokolle
        api_response = api_instance.plenarprotokoll()
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling PlenarprotokollApi->plenarprotokoll: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | An API key is required to access this service. Please refer to https://dip.bundestag.de/über-dip/hilfe/api how to apply for a key. Misuse of this service may lead to blocking your requests. |  -  |
**404** | ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plenarprotokoll_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} plenarprotokoll_id(id)

Metadaten zu Plenarprotokoll

Metadaten zu Plenarprotokoll

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import plenarprotokoll_api
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dip_bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plenarprotokoll_api.PlenarprotokollApi(api_client)
    id = 908 # int | ID des Plenarprotokolles

    # example passing only required values which don't have defaults set
    try:
        # Metadaten zu Plenarprotokoll
        api_response = api_instance.plenarprotokoll_id(id)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling PlenarprotokollApi->plenarprotokoll_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID des Plenarprotokolles |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | An API key is required to access this service. Please refer to https://dip.bundestag.de/über-dip/hilfe/api how to apply for a key. Misuse of this service may lead to blocking your requests. |  -  |
**404** | ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plenarprotokoll_text**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} plenarprotokoll_text()

Liste aller Volltexte der Plenarprotokolle

Liste aller Volltexte der Plenarprotokolle

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import plenarprotokoll_api
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dip_bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plenarprotokoll_api.PlenarprotokollApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste aller Volltexte der Plenarprotokolle
        api_response = api_instance.plenarprotokoll_text()
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling PlenarprotokollApi->plenarprotokoll_text: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | An API key is required to access this service. Please refer to https://dip.bundestag.de/über-dip/hilfe/api how to apply for a key. Misuse of this service may lead to blocking your requests. |  -  |
**404** | ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plenarprotokoll_text_id_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} plenarprotokoll_text_id_get(id)

Volltexte der Plenarprotokolle

Soweit vorhanden werden zusätzlich die Volltexte der Plenarprotokolle ausgegeben

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import plenarprotokoll_api
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dip_bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plenarprotokoll_api.PlenarprotokollApi(api_client)
    id = 908 # int | ID des Plenarprotokolles

    # example passing only required values which don't have defaults set
    try:
        # Volltexte der Plenarprotokolle
        api_response = api_instance.plenarprotokoll_text_id_get(id)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling PlenarprotokollApi->plenarprotokoll_text_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID des Plenarprotokolles |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | An API key is required to access this service. Please refer to https://dip.bundestag.de/über-dip/hilfe/api how to apply for a key. Misuse of this service may lead to blocking your requests. |  -  |
**404** | ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

