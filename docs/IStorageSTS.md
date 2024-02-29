# IStorageSTS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** |  | [optional] [readonly] 
**secret_key** | **str** |  | [optional] [readonly] 
**use_token** | **bool** |  | [optional] [readonly] 
**token** | **str** |  | [optional] [readonly] 
**expiration** | **datetime** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.i_storage_sts import IStorageSTS

# TODO update the JSON string below
json = "{}"
# create an instance of IStorageSTS from a JSON string
i_storage_sts_instance = IStorageSTS.from_json(json)
# print the JSON string representation of the object
print IStorageSTS.to_json()

# convert the object into a dict
i_storage_sts_dict = i_storage_sts_instance.to_dict()
# create an instance of IStorageSTS from a dict
i_storage_sts_form_dict = i_storage_sts.from_dict(i_storage_sts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


