# IInventoryPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_type** | [**InventoryType**](InventoryType.md) |  | 
**inventory_point_uri** | **str** |  | [readonly] 
**initialized** | **bool** |  | [optional] [readonly] 
**remote_id** | **str** |  | [optional] [readonly] 
**resource_server** | **str** |  | [optional] [readonly] 
**owner** | **str** |  | [optional] [readonly] 
**type** | [**AuthResourceType**](AuthResourceType.md) |  | 
**status** | [**IResourceStatus**](IResourceStatus.md) |  | [optional] 
**resource_uris** | **List[str]** |  | [readonly] 
**scopes** | **List[str]** |  | [optional] [readonly] 
**properties** | **Dict[str, List[object]]** |  | [readonly] 
**platform_id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [readonly] 
**var_self** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.i_inventory_point import IInventoryPoint

# TODO update the JSON string below
json = "{}"
# create an instance of IInventoryPoint from a JSON string
i_inventory_point_instance = IInventoryPoint.from_json(json)
# print the JSON string representation of the object
print(IInventoryPoint.to_json())

# convert the object into a dict
i_inventory_point_dict = i_inventory_point_instance.to_dict()
# create an instance of IInventoryPoint from a dict
i_inventory_point_form_dict = i_inventory_point.from_dict(i_inventory_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


