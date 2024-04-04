# openapi_client.InventoryApi

All URIs are relative to *https://api.bios-dev.terradue.com/core*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claim_catalogue**](InventoryApi.md#claim_catalogue) | **POST** /v2/inventory/catalogues/{catalogueId}/claim | Claim a catalogue
[**get_catalogue_by_id**](InventoryApi.md#get_catalogue_by_id) | **GET** /v2/inventory/catalogues/{catalogueId} | Get the catalogue information for a specific id
[**get_catalogue_publication_status**](InventoryApi.md#get_catalogue_publication_status) | **GET** /v2/inventory/catalogues/publication/{publicationId} | Get Status of an import
[**get_catalogues**](InventoryApi.md#get_catalogues) | **GET** /v2/inventory/catalogues | Get all the catalogues information related to an authenticated user
[**v2_inventory_catalogues_publish_post**](InventoryApi.md#v2_inventory_catalogues_publish_post) | **POST** /v2/inventory/catalogues/publish | Submit a catalog publication request
[**v2_inventory_token_get**](InventoryApi.md#v2_inventory_token_get) | **GET** /v2/inventory/token | Get Credentials for specific inventory point (e.g catalog, collection)


# **claim_catalogue**
> claim_catalogue(catalogue_id)

Claim a catalogue

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
    api_instance = openapi_client.InventoryApi(api_client)
    catalogue_id = 'catalogue_id_example' # str | Catalogue Identifier

    try:
        # Claim a catalogue
        api_instance.claim_catalogue(catalogue_id)
    except Exception as e:
        print("Exception when calling InventoryApi->claim_catalogue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalogue_id** | **str**| Catalogue Identifier | 

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
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalogue_by_id**
> get_catalogue_by_id(catalogue_id)

Get the catalogue information for a specific id

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
    api_instance = openapi_client.InventoryApi(api_client)
    catalogue_id = 'catalogue_id_example' # str | 

    try:
        # Get the catalogue information for a specific id
        api_instance.get_catalogue_by_id(catalogue_id)
    except Exception as e:
        print("Exception when calling InventoryApi->get_catalogue_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalogue_id** | **str**|  | 

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
**200** | List of workspaces |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalogue_publication_status**
> get_catalogue_publication_status(publication_id)

Get Status of an import



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
    api_instance = openapi_client.InventoryApi(api_client)
    publication_id = 'publication_id_example' # str | 

    try:
        # Get Status of an import
        api_instance.get_catalogue_publication_status(publication_id)
    except Exception as e:
        print("Exception when calling InventoryApi->get_catalogue_publication_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publication_id** | **str**|  | 

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
**200** | Returns the STAC catalog of the imported resources |  -  |
**404** | If the import is not found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalogues**
> List[IInventoryCatalog] get_catalogues()

Get all the catalogues information related to an authenticated user

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

[**List[IInventoryCatalog]**](IInventoryCatalog.md)

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

# **v2_inventory_catalogues_publish_post**
> PublicationRequest v2_inventory_catalogues_publish_post(catalog_publication_request=catalog_publication_request)

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
        api_response = api_instance.v2_inventory_catalogues_publish_post(catalog_publication_request=catalog_publication_request)
        print("The response of InventoryApi->v2_inventory_catalogues_publish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->v2_inventory_catalogues_publish_post: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request and the status location of the publication request |  -  |
**400** | If the notification is creating an issue |  -  |
**422** | If the notification payload is not processable |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_token_get**
> StsInventory v2_inventory_token_get(inventory_point_id=inventory_point_id)

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
        api_response = api_instance.v2_inventory_token_get(inventory_point_id=inventory_point_id)
        print("The response of InventoryApi->v2_inventory_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->v2_inventory_token_get: %s\n" % e)
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
**404** | If the inventory point is not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

