# ImportRequest

Represents a request for importing data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the ID of the import request. | [optional] 
**workspace_id** | **str** | Gets or sets the ID of the workspace. | 
**url** | **str** | Gets or sets the source URL.  According to the import function, this URL refers to a catalog endpoint or a direct URL to the data. | 
**asset_filters** | **List[str]** | Gets or sets the asset filters. | [optional] 
**path** | **str** | Gets or sets the path in the workspace where the imported data will be stored.  Not mandatory, usually the service prepares a unique path according to the type of import. | [optional] 
**fail_on_error** | **bool** | Gets or sets a value indicating whether to fail on import error. | [optional] 

## Example

```python
from openapi_client.models.import_request import ImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportRequest from a JSON string
import_request_instance = ImportRequest.from_json(json)
# print the JSON string representation of the object
print(ImportRequest.to_json())

# convert the object into a dict
import_request_dict = import_request_instance.to_dict()
# create an instance of ImportRequest from a dict
import_request_form_dict = import_request.from_dict(import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


