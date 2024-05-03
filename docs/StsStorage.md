# StsStorage

Represents the response object for STS (Security Token Service) operations for storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage** | [**IStoragePoint**](IStoragePoint.md) |  | [optional] 
**credentials** | [**IStorageSTS**](IStorageSTS.md) |  | [optional] 

## Example

```python
from openapi_client.models.sts_storage import StsStorage

# TODO update the JSON string below
json = "{}"
# create an instance of StsStorage from a JSON string
sts_storage_instance = StsStorage.from_json(json)
# print the JSON string representation of the object
print(StsStorage.to_json())

# convert the object into a dict
sts_storage_dict = sts_storage_instance.to_dict()
# create an instance of StsStorage from a dict
sts_storage_from_dict = StsStorage.from_dict(sts_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


