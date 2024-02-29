# IStoragePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_type** | [**StorageType**](StorageType.md) |  | [optional] 
**storage_point_uri** | **str** |  | [optional] [readonly] 
**service_uri** | **str** |  | [optional] [readonly] 
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
from openapi_client.models.i_storage_point import IStoragePoint

# TODO update the JSON string below
json = "{}"
# create an instance of IStoragePoint from a JSON string
i_storage_point_instance = IStoragePoint.from_json(json)
# print the JSON string representation of the object
print IStoragePoint.to_json()

# convert the object into a dict
i_storage_point_dict = i_storage_point_instance.to_dict()
# create an instance of IStoragePoint from a dict
i_storage_point_form_dict = i_storage_point.from_dict(i_storage_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


