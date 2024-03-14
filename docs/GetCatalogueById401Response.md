# GetCatalogueById401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 
**errors** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from openapi_client.models.get_catalogue_by_id401_response import GetCatalogueById401Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCatalogueById401Response from a JSON string
get_catalogue_by_id401_response_instance = GetCatalogueById401Response.from_json(json)
# print the JSON string representation of the object
print(GetCatalogueById401Response.to_json())

# convert the object into a dict
get_catalogue_by_id401_response_dict = get_catalogue_by_id401_response_instance.to_dict()
# create an instance of GetCatalogueById401Response from a dict
get_catalogue_by_id401_response_form_dict = get_catalogue_by_id401_response.from_dict(get_catalogue_by_id401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


