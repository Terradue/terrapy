# openapi_client.ControlApi

All URIs are relative to *https://api.bios-dev.terradue.com/core*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_status**](ControlApi.md#get_job_status) | **GET** /v2/jobs/{jobId} | Get the status of a job


# **get_job_status**
> RequestStatus get_job_status(job_id)

Get the status of a job

### Example

* OAuth Authentication (AccessToken):

```python
import openapi_client
from openapi_client.models.request_status import RequestStatus
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
    except Exception as e:
        print("Exception when calling ControlApi->get_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**RequestStatus**](RequestStatus.md)

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

