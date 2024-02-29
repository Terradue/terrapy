# DataCastingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**catalog_id** | **str** |  | 
**workspace_id** | **str** |  | 
**processor_id** | **str** |  | 
**additional_links** | [**List[Link]**](Link.md) |  | [optional] 
**subjects** | [**List[Subject]**](Subject.md) |  | [optional] 
**collection** | **str** |  | [optional] 
**asset_filters** | **List[str]** |  | [optional] 
**path** | **str** |  | [optional] 
**casting** | [**DataCastingEnum**](DataCastingEnum.md) |  | [optional] 
**depth** | **int** |  | [optional] 
**background_job_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.data_casting_request import DataCastingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataCastingRequest from a JSON string
data_casting_request_instance = DataCastingRequest.from_json(json)
# print the JSON string representation of the object
print DataCastingRequest.to_json()

# convert the object into a dict
data_casting_request_dict = data_casting_request_instance.to_dict()
# create an instance of DataCastingRequest from a dict
data_casting_request_form_dict = data_casting_request.from_dict(data_casting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


