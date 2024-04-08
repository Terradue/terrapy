# openapi_client.StorageApi

All URIs are relative to *https://api.bios-dev.terradue.com/core*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claim_workspace**](StorageApi.md#claim_workspace) | **POST** /v2/storage/workspaces/{workspaceId}/claim | Claim a workspace
[**delete_shared_folder_by_id**](StorageApi.md#delete_shared_folder_by_id) | **DELETE** /v2/storage/sharedfolders/{sharedFolderId} | 
[**download**](StorageApi.md#download) | **POST** /v2/storage/download | Request a download URL for a given resource
[**get_shared_folder_by_id**](StorageApi.md#get_shared_folder_by_id) | **GET** /v2/storage/sharedfolders/{sharedFolderId} | Get the shared folder information for a specific id
[**get_shared_folders**](StorageApi.md#get_shared_folders) | **GET** /v2/storage/sharedfolders | Get all the workspaces information related to an authenticated user
[**get_storage_sts**](StorageApi.md#get_storage_sts) | **GET** /v2/storage/token | Get Credentials for specific storage point (e.g workspace, shared folder...)
[**get_workspace_by_id**](StorageApi.md#get_workspace_by_id) | **GET** /v2/storage/workspaces/{workspaceId} | Get the workspace information for a specific id
[**get_workspace_import_status**](StorageApi.md#get_workspace_import_status) | **GET** /v2/storage/workspaces/imports/{importId} | Get Status of an import
[**get_workspaces**](StorageApi.md#get_workspaces) | **GET** /v2/storage/workspaces | Get all the workspaces information related to an authenticated user
[**import_from_url**](StorageApi.md#import_from_url) | **POST** /v2/storage/workspaces/{workspaceId}/import-catalog | Import resources from exisiting catalog
[**share_folder**](StorageApi.md#share_folder) | **POST** /v2/storage/workspaces/{workspaceId}/share | Share a folder from a workspace with users


# **claim_workspace**
> IWorkspace claim_workspace(workspace_id)

Claim a workspace

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.i_workspace import IWorkspace
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
    api_instance = openapi_client.StorageApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace Identifier

    try:
        # Claim a workspace
        api_response = api_instance.claim_workspace(workspace_id)
        print("The response of StorageApi->claim_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->claim_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace Identifier | 

### Return type

[**IWorkspace**](IWorkspace.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Workspace claim accepted |  -  |
**404** | Workspace not found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shared_folder_by_id**
> ResourceDeletionTask delete_shared_folder_by_id(shared_folder_id)



### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.resource_deletion_task import ResourceDeletionTask
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
    api_instance = openapi_client.StorageApi(api_client)
    shared_folder_id = 'shared_folder_id_example' # str | 

    try:
        api_response = api_instance.delete_shared_folder_by_id(shared_folder_id)
        print("The response of StorageApi->delete_shared_folder_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->delete_shared_folder_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_folder_id** | **str**|  | 

### Return type

[**ResourceDeletionTask**](ResourceDeletionTask.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Shared Folder deletion task |  -  |
**401** | Unauthorized |  -  |
**404** | Shared Folder not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download**
> download(url=url, redirect=redirect)

Request a download URL for a given resource

This method will return a download URL for a given resource based on the user's storage information.  If the given resource is not in the user's storage, the method will return the resource's original URL.  If the resource is in the user's storage, the method will return a download URL for the resource  based on the user access permissions and the resource's storage policies.

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
    api_instance = openapi_client.StorageApi(api_client)
    url = 'url_example' # str | URL of the resource (optional)
    redirect = True # bool | Redirect to the download URL (optional) (default to True)

    try:
        # Request a download URL for a given resource
        api_instance.download(url=url, redirect=redirect)
    except Exception as e:
        print("Exception when calling StorageApi->download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| URL of the resource | [optional] 
 **redirect** | **bool**| Redirect to the download URL | [optional] [default to True]

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
**302** | Redirect |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_folder_by_id**
> ISharedFolder get_shared_folder_by_id(shared_folder_id)

Get the shared folder information for a specific id

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.i_shared_folder import ISharedFolder
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
    api_instance = openapi_client.StorageApi(api_client)
    shared_folder_id = 'shared_folder_id_example' # str | 

    try:
        # Get the shared folder information for a specific id
        api_response = api_instance.get_shared_folder_by_id(shared_folder_id)
        print("The response of StorageApi->get_shared_folder_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_shared_folder_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_folder_id** | **str**|  | 

### Return type

[**ISharedFolder**](ISharedFolder.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shared Folder |  -  |
**401** | Unauthorized |  -  |
**404** | Shared Folder not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_folders**
> List[ISharedFolder] get_shared_folders()

Get all the workspaces information related to an authenticated user

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.i_shared_folder import ISharedFolder
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
    api_instance = openapi_client.StorageApi(api_client)

    try:
        # Get all the workspaces information related to an authenticated user
        api_response = api_instance.get_shared_folders()
        print("The response of StorageApi->get_shared_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_shared_folders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ISharedFolder]**](ISharedFolder.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shared folders |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_sts**
> StsStorage get_storage_sts(storage_point_id=storage_point_id)

Get Credentials for specific storage point (e.g workspace, shared folder...)



### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.sts_storage import StsStorage
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
    api_instance = openapi_client.StorageApi(api_client)
    storage_point_id = 'storage_point_id_example' # str |  (optional)

    try:
        # Get Credentials for specific storage point (e.g workspace, shared folder...)
        api_response = api_instance.get_storage_sts(storage_point_id=storage_point_id)
        print("The response of StorageApi->get_storage_sts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_storage_sts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_point_id** | **str**|  | [optional] 

### Return type

[**StsStorage**](StsStorage.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pair Storage and Credentials |  -  |
**401** | Unauthorized |  -  |
**404** | If the storage point is not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_by_id**
> IWorkspace get_workspace_by_id(workspace_id)

Get the workspace information for a specific id

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.i_workspace import IWorkspace
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
    api_instance = openapi_client.StorageApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get the workspace information for a specific id
        api_response = api_instance.get_workspace_by_id(workspace_id)
        print("The response of StorageApi->get_workspace_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_workspace_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**IWorkspace**](IWorkspace.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace |  -  |
**404** | Workspace not found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_import_status**
> get_workspace_import_status(import_id)

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
    api_instance = openapi_client.StorageApi(api_client)
    import_id = 'import_id_example' # str | 

    try:
        # Get Status of an import
        api_instance.get_workspace_import_status(import_id)
    except Exception as e:
        print("Exception when calling StorageApi->get_workspace_import_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Import status |  -  |
**404** | If the import is not found |  -  |
**200** | Returns the import status |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspaces**
> List[IWorkspace] get_workspaces()

Get all the workspaces information related to an authenticated user

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.i_workspace import IWorkspace
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
    api_instance = openapi_client.StorageApi(api_client)

    try:
        # Get all the workspaces information related to an authenticated user
        api_response = api_instance.get_workspaces()
        print("The response of StorageApi->get_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_workspaces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[IWorkspace]**](IWorkspace.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of workspaces |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_from_url**
> ImportRequest import_from_url(workspace_id, import_request=import_request)

Import resources from exisiting catalog



### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.import_request import ImportRequest
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
    api_instance = openapi_client.StorageApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    import_request = openapi_client.ImportRequest() # ImportRequest |  (optional)

    try:
        # Import resources from exisiting catalog
        api_response = api_instance.import_from_url(workspace_id, import_request=import_request)
        print("The response of StorageApi->import_from_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->import_from_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **import_request** | [**ImportRequest**](ImportRequest.md)|  | [optional] 

### Return type

[**ImportRequest**](ImportRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2, application/json; x-api-version=2, text/json; x-api-version=2, application/*+json; x-api-version=2
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the STAC catalog of the imported resources |  -  |
**404** | Workspace not found |  -  |
**400** | If the import creation raised an issue |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_folder**
> ISharedFolder share_folder(workspace_id, share_folder_request=share_folder_request)

Share a folder from a workspace with users

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.i_shared_folder import ISharedFolder
from openapi_client.models.share_folder_request import ShareFolderRequest
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
    api_instance = openapi_client.StorageApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace Identifier
    share_folder_request = openapi_client.ShareFolderRequest() # ShareFolderRequest | Shared folder request (optional)

    try:
        # Share a folder from a workspace with users
        api_response = api_instance.share_folder(workspace_id, share_folder_request=share_folder_request)
        print("The response of StorageApi->share_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->share_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace Identifier | 
 **share_folder_request** | [**ShareFolderRequest**](ShareFolderRequest.md)| Shared folder request | [optional] 

### Return type

[**ISharedFolder**](ISharedFolder.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2, application/json; x-api-version=2, text/json; x-api-version=2, application/*+json; x-api-version=2
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Shared folder created |  -  |
**404** | Workspace not found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

