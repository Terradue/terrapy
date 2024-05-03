# StsInventory

Represents the response object for STS (Security Token Service) operations for storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage** | [**IInventoryPoint**](IInventoryPoint.md) |  | [optional] 
**credentials** | [**IInventorySTS**](IInventorySTS.md) |  | [optional] 

## Example

```python
from openapi_client.models.sts_inventory import StsInventory

# TODO update the JSON string below
json = "{}"
# create an instance of StsInventory from a JSON string
sts_inventory_instance = StsInventory.from_json(json)
# print the JSON string representation of the object
print(StsInventory.to_json())

# convert the object into a dict
sts_inventory_dict = sts_inventory_instance.to_dict()
# create an instance of StsInventory from a dict
sts_inventory_from_dict = StsInventory.from_dict(sts_inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


