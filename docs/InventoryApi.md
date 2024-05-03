# openapi_client.InventoryApi

All URIs are relative to *https://api.bios-dev.terradue.com/core*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claim_catalogue**](InventoryApi.md#claim_catalogue) | **POST** /v2/inventory/catalogues/{catalogueId}/claim | Claim a catalogue
[**get_catalogue_by_id**](InventoryApi.md#get_catalogue_by_id) | **GET** /v2/inventory/catalogues/{catalogueId} | Get the catalogue information for a specific id
[**get_catalogue_publication_status**](InventoryApi.md#get_catalogue_publication_status) | **GET** /v2/inventory/catalogues/publication/{publicationId} | Get Status of an import
[**get_catalogues**](InventoryApi.md#get_catalogues) | **GET** /v2/inventory/catalogues | Get all the catalogues information related to an authenticated user
[**get_inventory_sts**](InventoryApi.md#get_inventory_sts) | **GET** /v2/inventory/token | Get Credentials for specific inventory point (e.g catalog, collection)
[**get_supported_formats**](InventoryApi.md#get_supported_formats) | **GET** /v2/inventory/formats | Get the supported formats for the inventory point
[**publish**](InventoryApi.md#publish) | **POST** /v2/inventory/catalogues/publish | Submit a catalog publication request


# **claim_catalogue**
> IInventoryCatalog claim_catalogue(catalogue_id)

Claim a catalogue

This endpoint allows to claim a catalogue. Claiming a catalogue means that the user is the owner of the catalogue  and that it request the catalogue to be ready for operations.  According to the catalogue type, the claim operation may have different effects such as creating the index,  creating the collections, etc.

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.i_inventory_catalog import IInventoryCatalog
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
    api_instance = openapi_client.InventoryApi(api_client)
    catalogue_id = 'catalogue_id_example' # str | Catalogue Identifier

    try:
        # Claim a catalogue
        api_response = api_instance.claim_catalogue(catalogue_id)
        print("The response of InventoryApi->claim_catalogue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->claim_catalogue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalogue_id** | **str**| Catalogue Identifier | 

### Return type

[**IInventoryCatalog**](IInventoryCatalog.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The claim request has been accepted and catalog infromation is updated |  -  |
**401** | Unauthorized |  -  |
**404** | Catalogue not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalogue_by_id**
> IInventoryCatalog get_catalogue_by_id(catalogue_id)

Get the catalogue information for a specific id

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.i_inventory_catalog import IInventoryCatalog
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
    api_instance = openapi_client.InventoryApi(api_client)
    catalogue_id = 'catalogue_id_example' # str | 

    try:
        # Get the catalogue information for a specific id
        api_response = api_instance.get_catalogue_by_id(catalogue_id)
        print("The response of InventoryApi->get_catalogue_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_catalogue_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalogue_id** | **str**|  | 

### Return type

[**IInventoryCatalog**](IInventoryCatalog.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The catalogue information |  -  |
**401** | Unauthorized |  -  |
**404** | Catalogue not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalogue_publication_status**
> PublicationStatus get_catalogue_publication_status(publication_id)

Get Status of an import



### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.publication_status import PublicationStatus
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
    api_instance = openapi_client.InventoryApi(api_client)
    publication_id = 'publication_id_example' # str | 

    try:
        # Get Status of an import
        api_response = api_instance.get_catalogue_publication_status(publication_id)
        print("The response of InventoryApi->get_catalogue_publication_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_catalogue_publication_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publication_id** | **str**|  | 

### Return type

[**PublicationStatus**](PublicationStatus.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The publication status |  -  |
**404** | Publication not found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalogues**
> List[SelfInfo] get_catalogues()

Get all the catalogues information related to an authenticated user

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.self_info import SelfInfo
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
    api_instance = openapi_client.InventoryApi(api_client)

    try:
        # Get all the catalogues information related to an authenticated user
        api_response = api_instance.get_catalogues()
        print("The response of InventoryApi->get_catalogues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_catalogues: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SelfInfo]**](SelfInfo.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of catalogues |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_sts**
> StsInventory get_inventory_sts(inventory_point_id=inventory_point_id)

Get Credentials for specific inventory point (e.g catalog, collection)



### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.sts_inventory import StsInventory
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
    api_instance = openapi_client.InventoryApi(api_client)
    inventory_point_id = 'inventory_point_id_example' # str |  (optional)

    try:
        # Get Credentials for specific inventory point (e.g catalog, collection)
        api_response = api_instance.get_inventory_sts(inventory_point_id=inventory_point_id)
        print("The response of InventoryApi->get_inventory_sts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_inventory_sts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_point_id** | **str**|  | [optional] 

### Return type

[**StsInventory**](StsInventory.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pair Inventory and Credentials |  -  |
**401** | Unauthorized |  -  |
**404** | Inventory point not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_formats**
> Dict[str, ITranslator] get_supported_formats()

Get the supported formats for the inventory point



### Example


```python
import openapi_client
from openapi_client.models.i_translator import ITranslator
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bios-dev.terradue.com/core
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.bios-dev.terradue.com/core"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.InventoryApi(api_client)

    try:
        # Get the supported formats for the inventory point
        api_response = api_instance.get_supported_formats()
        print("The response of InventoryApi->get_supported_formats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_supported_formats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dict[str, ITranslator]**](ITranslator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supported formats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish**
> PublicationRequest publish(catalog_publication_request=catalog_publication_request)

Submit a catalog publication request

This endpoint allows to submit a catalog publication request. A publication request triggers a workflow  that performs <see href=\"https://github.com/Terradue/Stars#Documentation\">Stars crawling</see>   and publish collections and items to the specified   <see href=\"/docs/resources/inventory/#catalogs\">catalog of the inventory.</see>

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.catalog_publication_request import CatalogPublicationRequest
from openapi_client.models.publication_request import PublicationRequest
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
    api_instance = openapi_client.InventoryApi(api_client)
    catalog_publication_request = openapi_client.CatalogPublicationRequest() # CatalogPublicationRequest |  (optional)

    try:
        # Submit a catalog publication request
        api_response = api_instance.publish(catalog_publication_request=catalog_publication_request)
        print("The response of InventoryApi->publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_publication_request** | [**CatalogPublicationRequest**](CatalogPublicationRequest.md)|  | [optional] 

### Return type

[**PublicationRequest**](PublicationRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2, application/json; x-api-version=2, text/json; x-api-version=2, application/*+json; x-api-version=2
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The publication request has been created |  -  |
**400** | Bad Request |  -  |
**422** | Client Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

