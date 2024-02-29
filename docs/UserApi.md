# openapi_client.UserApi

All URIs are relative to *https://api.bios-dev.terradue.com/core*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_user_info_get**](UserApi.md#v2_user_info_get) | **GET** /v2/user/info | Get the principal user identities from the identity management system
[**v2_user_platforms_get**](UserApi.md#v2_user_platforms_get) | **GET** /v2/user/platforms | Get the principal user identities from the identity management system


# **v2_user_info_get**
> PrincipalContext v2_user_info_get()

Get the principal user identities from the identity management system

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.principal_context import PrincipalContext
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
    api_instance = openapi_client.UserApi(api_client)

    try:
        # Get the principal user identities from the identity management system
        api_response = api_instance.v2_user_info_get()
        print("The response of UserApi->v2_user_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v2_user_info_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PrincipalContext**](PrincipalContext.md)

### Authorization

[AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Information |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_user_platforms_get**
> v2_user_platforms_get()

Get the principal user identities from the identity management system

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
    api_instance = openapi_client.UserApi(api_client)

    try:
        # Get the principal user identities from the identity management system
        api_instance.v2_user_platforms_get()
    except Exception as e:
        print("Exception when calling UserApi->v2_user_platforms_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

