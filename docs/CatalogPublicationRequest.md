# CatalogPublicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**catalog_id** | **str** |  | [optional] 
**additional_links** | [**List[Link]**](Link.md) |  | [optional] 
**subjects** | [**List[Subject]**](Subject.md) |  | [optional] 
**collection** | **str** |  | [optional] 
**depth** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.catalog_publication_request import CatalogPublicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogPublicationRequest from a JSON string
catalog_publication_request_instance = CatalogPublicationRequest.from_json(json)
# print the JSON string representation of the object
print(CatalogPublicationRequest.to_json())

# convert the object into a dict
catalog_publication_request_dict = catalog_publication_request_instance.to_dict()
# create an instance of CatalogPublicationRequest from a dict
catalog_publication_request_form_dict = catalog_publication_request.from_dict(catalog_publication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


