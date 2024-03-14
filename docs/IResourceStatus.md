# IResourceStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | [**ResourceStatusCode**](ResourceStatusCode.md) |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.i_resource_status import IResourceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IResourceStatus from a JSON string
i_resource_status_instance = IResourceStatus.from_json(json)
# print the JSON string representation of the object
print(IResourceStatus.to_json())

# convert the object into a dict
i_resource_status_dict = i_resource_status_instance.to_dict()
# create an instance of IResourceStatus from a dict
i_resource_status_form_dict = i_resource_status.from_dict(i_resource_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


