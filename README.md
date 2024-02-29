# TerrAPI Python Client
Terradue Core API v2

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = openapi_client.ControlApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Get the status of a job
        api_response = api_instance.get_job_status(job_id)
        print("The response of ControlApi->get_job_status:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ControlApi->get_job_status: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.bios-dev.terradue.com/core*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ControlApi* | [**get_job_status**](docs/ControlApi.md#get_job_status) | **GET** /v2/jobs/{jobId} | Get the status of a job
*ServicesApi* | [**cast_time_series**](docs/ServicesApi.md#cast_time_series) | **POST** /v2/services/timeseries/cast | Request casting for a time series.
*ServicesApi* | [**get_data_casting_status_async**](docs/ServicesApi.md#get_data_casting_status_async) | **GET** /v2/services/datacast/casts/{castId} | Get the status of a casting request
*ServicesApi* | [**post_data_casting**](docs/ServicesApi.md#post_data_casting) | **POST** /v2/services/datacast/cast | Request casting for a generic data resource
*StorageApi* | [**claim_workspace**](docs/StorageApi.md#claim_workspace) | **POST** /v2/storage/workspaces/{workspaceId}/claim | Claim a workspace
*StorageApi* | [**get_shared_folder_by_id**](docs/StorageApi.md#get_shared_folder_by_id) | **GET** /v2/storage/sharedfolders/{sharedFolderId} | Get the shared folder information for a specific id
*StorageApi* | [**get_workspace_by_id**](docs/StorageApi.md#get_workspace_by_id) | **GET** /v2/storage/workspaces/{workspaceId} | Get the workspace information for a specific id
*StorageApi* | [**get_workspace_import_status**](docs/StorageApi.md#get_workspace_import_status) | **GET** /v2/storage/workspaces/imports/{importId} | Get Status of an import
*StorageApi* | [**get_workspaces**](docs/StorageApi.md#get_workspaces) | **GET** /v2/storage/workspaces | Get all the workspaces information related to an authenticated user
*StorageApi* | [**share_folder**](docs/StorageApi.md#share_folder) | **POST** /v2/storage/workspaces/{workspaceId}/share | Share a folder from a workspace with users
*StorageApi* | [**v2_storage_download_post**](docs/StorageApi.md#v2_storage_download_post) | **POST** /v2/storage/download | Request a download URL for a given resource
*StorageApi* | [**v2_storage_token_get**](docs/StorageApi.md#v2_storage_token_get) | **GET** /v2/storage/token | Get Credentials for specific storage point (e.g workspace, shared folder...)
*StorageApi* | [**v2_storage_workspaces_workspace_id_import_catalog_post**](docs/StorageApi.md#v2_storage_workspaces_workspace_id_import_catalog_post) | **POST** /v2/storage/workspaces/{workspaceId}/import-catalog | Import resources from exisiting catalog
*UserApi* | [**v2_user_info_get**](docs/UserApi.md#v2_user_info_get) | **GET** /v2/user/info | Get the principal user identities from the identity management system
*UserApi* | [**v2_user_platforms_get**](docs/UserApi.md#v2_user_platforms_get) | **GET** /v2/user/platforms | Get the principal user identities from the identity management system


## Documentation For Models

 - [AccessToken](docs/AccessToken.md)
 - [AuthResourceType](docs/AuthResourceType.md)
 - [ClaimLite](docs/ClaimLite.md)
 - [DataCastingEnum](docs/DataCastingEnum.md)
 - [DataCastingRequest](docs/DataCastingRequest.md)
 - [GetJobStatus401Response](docs/GetJobStatus401Response.md)
 - [HttpValidationProblemDetails](docs/HttpValidationProblemDetails.md)
 - [IResourceStatus](docs/IResourceStatus.md)
 - [ISharedFolder](docs/ISharedFolder.md)
 - [IStoragePoint](docs/IStoragePoint.md)
 - [IStorageSTS](docs/IStorageSTS.md)
 - [IWorkspace](docs/IWorkspace.md)
 - [ImportRequest](docs/ImportRequest.md)
 - [Link](docs/Link.md)
 - [PrincipalContext](docs/PrincipalContext.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [RequestStatus](docs/RequestStatus.md)
 - [RequestStatusCode](docs/RequestStatusCode.md)
 - [ResourceStatusCode](docs/ResourceStatusCode.md)
 - [ShareFolderRequest](docs/ShareFolderRequest.md)
 - [StorageType](docs/StorageType.md)
 - [StsResponse](docs/StsResponse.md)
 - [Subject](docs/Subject.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="AccessToken"></a>
### AccessToken

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://iam-dev.terradue.com/realms/master/protocol/openid-connect/auth
- **Scopes**: 
 - **openid**: openid
 - **profile**: profile
 - **bios-dev**: bios-dev
 - **offline_access**: offline_access


## Author




