# IInventoryCatalog


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
**background_job_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**content_type** | [**ContentType**](ContentType.md) |  | [optional] 
**resource_type** | [**ResourceType**](ResourceType.md) |  | [optional] 
**content_length** | **int** |  | [optional] [readonly] 
**content_disposition** | [**ContentDisposition**](ContentDisposition.md) |  | [optional] 
**uri** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.i_inventory_catalog import IInventoryCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of IInventoryCatalog from a JSON string
i_inventory_catalog_instance = IInventoryCatalog.from_json(json)
# print the JSON string representation of the object
print(IInventoryCatalog.to_json())

# convert the object into a dict
i_inventory_catalog_dict = i_inventory_catalog_instance.to_dict()
# create an instance of IInventoryCatalog from a dict
i_inventory_catalog_from_dict = IInventoryCatalog.from_dict(i_inventory_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


