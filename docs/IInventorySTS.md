# IInventorySTS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] [readonly] 
**token** | **str** |  | [optional] [readonly] 
**expiration** | **datetime** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.i_inventory_sts import IInventorySTS

# TODO update the JSON string below
json = "{}"
# create an instance of IInventorySTS from a JSON string
i_inventory_sts_instance = IInventorySTS.from_json(json)
# print the JSON string representation of the object
print(IInventorySTS.to_json())

# convert the object into a dict
i_inventory_sts_dict = i_inventory_sts_instance.to_dict()
# create an instance of IInventorySTS from a dict
i_inventory_sts_from_dict = IInventorySTS.from_dict(i_inventory_sts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


