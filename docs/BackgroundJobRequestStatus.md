# BackgroundJobRequestStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] [readonly] 
**status** | [**RequestStatusCode**](RequestStatusCode.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.background_job_request_status import BackgroundJobRequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundJobRequestStatus from a JSON string
background_job_request_status_instance = BackgroundJobRequestStatus.from_json(json)
# print the JSON string representation of the object
print(BackgroundJobRequestStatus.to_json())

# convert the object into a dict
background_job_request_status_dict = background_job_request_status_instance.to_dict()
# create an instance of BackgroundJobRequestStatus from a dict
background_job_request_status_form_dict = background_job_request_status.from_dict(background_job_request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


