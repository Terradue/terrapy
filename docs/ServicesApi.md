# openapi_client.ServicesApi

All URIs are relative to *https://api.bios-dev.terradue.com/core*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cast_time_series**](ServicesApi.md#cast_time_series) | **POST** /v2/services/timeseries/cast | Request casting for a time series.
[**get_data_casting_status_async**](ServicesApi.md#get_data_casting_status_async) | **GET** /v2/services/datacast/casts/{castId} | Get the status of a casting request
[**post_data_casting**](ServicesApi.md#post_data_casting) | **POST** /v2/services/datacast/cast | Request casting for a generic data resource


# **cast_time_series**
> str cast_time_series(data_casting_request=data_casting_request)

Request casting for a time series.

Casting a time series actually creates 3 tasks and links them:  - importing the generic data from the source as per <seealso cref=\"!:Storage.WorkspaceController.ImportFromUrl(ImportRequest, string, CancellationToken)\"><a href=\"#/Storage/ImportFromUrl\">import operation</a></seealso>  - finding the time series in the imported data  - publishing the generic data in the catalog as per <seealso cref=\"M:TerrApi.Server.Controllers.V2.Inventory.CatalogueController.Publish(TerrApi.Server.Controllers.V2.Inventory.Models.CatalogPublicationRequest,System.Threading.CancellationToken)\"><a href=\"#/Inventory/Publish\">publish operation</a></seealso>

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.data_casting_request import DataCastingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bios-dev.terradue.com/core
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.bios-dev.terradue.com/core"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServicesApi(api_client)
    data_casting_request = openapi_client.DataCastingRequest() # DataCastingRequest | The request to cast a time series (optional)

    try:
        # Request casting for a time series.
        api_response = api_instance.cast_time_series(data_casting_request=data_casting_request)
        print("The response of ServicesApi->cast_time_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->cast_time_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_casting_request** | [**DataCastingRequest**](DataCastingRequest.md)| The request to cast a time series | [optional] 

### Return type

**str**

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2, application/json; x-api-version=2, text/json; x-api-version=2, application/*+json; x-api-version=2
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request has been accepted and the cast identifier is returned |  -  |
**400** | Bad Request |  -  |
**422** | Client Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_casting_status_async**
> get_data_casting_status_async(cast_id)

Get the status of a casting request

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bios-dev.terradue.com/core
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.bios-dev.terradue.com/core"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServicesApi(api_client)
    cast_id = 'cast_id_example' # str | 

    try:
        # Get the status of a casting request
        api_instance.get_data_casting_status_async(cast_id)
    except Exception as e:
        print("Exception when calling ServicesApi->get_data_casting_status_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cast_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_data_casting**
> str post_data_casting(data_casting_request=data_casting_request)

Request casting for a generic data resource

Casting a generic data results actually creates 2 task and link them  - importing the generic data from the source as per <seealso cref=\"M:TerrApi.Server.Controllers.V2.Storage.WorkspaceController.ImportFromUrl(TerrApi.Core.Models.ImportRequest,System.String,System.Threading.CancellationToken)\"><a href=\"#/Storage/ImportFromUrl\">import operation</a></seealso>  - publishing the generic data in the catalog as per <seealso cref=\"M:TerrApi.Server.Controllers.V2.Inventory.CatalogueController.Publish(TerrApi.Server.Controllers.V2.Inventory.Models.CatalogPublicationRequest,System.Threading.CancellationToken)\"><a href=\"#/Inventory/Publish\">publish operation</a></seealso>

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.data_casting_request import DataCastingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bios-dev.terradue.com/core
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.bios-dev.terradue.com/core"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServicesApi(api_client)
    data_casting_request = openapi_client.DataCastingRequest() # DataCastingRequest | The casting request (optional)

    try:
        # Request casting for a generic data resource
        api_response = api_instance.post_data_casting(data_casting_request=data_casting_request)
        print("The response of ServicesApi->post_data_casting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->post_data_casting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_casting_request** | [**DataCastingRequest**](DataCastingRequest.md)| The casting request | [optional] 

### Return type

**str**

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A context Id for the casting request |  -  |
**400** | Bad Request |  -  |
**422** | Client Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

