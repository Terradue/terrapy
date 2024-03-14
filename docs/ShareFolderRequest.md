# ShareFolderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**users** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.share_folder_request import ShareFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShareFolderRequest from a JSON string
share_folder_request_instance = ShareFolderRequest.from_json(json)
# print the JSON string representation of the object
print(ShareFolderRequest.to_json())

# convert the object into a dict
share_folder_request_dict = share_folder_request_instance.to_dict()
# create an instance of ShareFolderRequest from a dict
share_folder_request_form_dict = share_folder_request.from_dict(share_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


