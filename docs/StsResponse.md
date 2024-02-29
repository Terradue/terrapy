# StsResponse

Represents the response object for STS (Security Token Service) operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage** | [**IStoragePoint**](IStoragePoint.md) |  | [optional] 
**credentials** | [**IStorageSTS**](IStorageSTS.md) |  | [optional] 

## Example

```python
from openapi_client.models.sts_response import StsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StsResponse from a JSON string
sts_response_instance = StsResponse.from_json(json)
# print the JSON string representation of the object
print StsResponse.to_json()

# convert the object into a dict
sts_response_dict = sts_response_instance.to_dict()
# create an instance of StsResponse from a dict
sts_response_form_dict = sts_response.from_dict(sts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


