# dip_bundestag.DrucksacheApi

All URIs are relative to *https://search.dip.bundestag.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drucksache**](DrucksacheApi.md#drucksache) | **GET** /drucksache | Liste aller Drucksachen
[**drucksache_id**](DrucksacheApi.md#drucksache_id) | **GET** /drucksache/{id} | Metadaten zu Drucksache
[**drucksache_text**](DrucksacheApi.md#drucksache_text) | **GET** /drucksache-text | Liste aller Volltexte der Drucksachen
[**drucksache_text_id**](DrucksacheApi.md#drucksache_text_id) | **GET** /drucksache-text/{id} | Volltexte einer Drucksache


# **drucksache**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} drucksache()

Liste aller Drucksachen

Liste aller Drucksachen

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import drucksache_api
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
    api_instance = drucksache_api.DrucksacheApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste aller Drucksachen
        api_response = api_instance.drucksache()
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling DrucksacheApi->drucksache: %s\n" % e)
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

# **drucksache_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} drucksache_id(id)

Metadaten zu Drucksache

Metadaten zu Drucksache

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import drucksache_api
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
    api_instance = drucksache_api.DrucksacheApi(api_client)
    id = 908 # int | ID der Drucksache

    # example passing only required values which don't have defaults set
    try:
        # Metadaten zu Drucksache
        api_response = api_instance.drucksache_id(id)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling DrucksacheApi->drucksache_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID der Drucksache |

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

# **drucksache_text**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} drucksache_text()

Liste aller Volltexte der Drucksachen

Liste aller Volltexte der Drucksachen

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import drucksache_api
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
    api_instance = drucksache_api.DrucksacheApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste aller Volltexte der Drucksachen
        api_response = api_instance.drucksache_text()
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling DrucksacheApi->drucksache_text: %s\n" % e)
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

# **drucksache_text_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} drucksache_text_id(id)

Volltexte einer Drucksache

Soweit vorhanden werden zusätzlich die Volltexte einer Drucksache ausgegeben

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
from deutschland import dip_bundestag
from deutschland.dip_bundestag.api import drucksache_api
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
    api_instance = drucksache_api.DrucksacheApi(api_client)
    id = 908 # int | ID der Drucksache

    # example passing only required values which don't have defaults set
    try:
        # Volltexte einer Drucksache
        api_response = api_instance.drucksache_text_id(id)
        pprint(api_response)
    except dip_bundestag.ApiException as e:
        print("Exception when calling DrucksacheApi->drucksache_text_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID der Drucksache |

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

