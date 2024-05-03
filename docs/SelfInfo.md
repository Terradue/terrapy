# SelfInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AuthResourceType**](AuthResourceType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**var_self** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.self_info import SelfInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SelfInfo from a JSON string
self_info_instance = SelfInfo.from_json(json)
# print the JSON string representation of the object
print(SelfInfo.to_json())

# convert the object into a dict
self_info_dict = self_info_instance.to_dict()
# create an instance of SelfInfo from a dict
self_info_from_dict = SelfInfo.from_dict(self_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


