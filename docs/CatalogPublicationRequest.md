# CatalogPublicationRequest

Represents a request to publish metadata to a catalog.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Gets or sets the source URL of the metadata to publish.  This source must point to a valid metadata document in a supported format. | 
**catalog_id** | **str** | Gets or sets the catalog name where the metadata will be published. | [optional] 
**additional_links** | [**List[Link]**](Link.md) | Gets or sets additional links to include in the metadata document. | [optional] 
**subjects** | [**List[Subject]**](Subject.md) | Gets or sets the list of subjects to include in the metadata document. | [optional] 
**collection** | **str** | Gets or sets the collection name where the metadata will be published. | [optional] 
**depth** | **int** | Gets or sets the depth of the metadata to publish.  0 means no publication, 1 means the root metadata document only, 2 means the metadata document and its children, and so on. | [optional] 
**assets_filters** | **List[str]** |  | [optional] 

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
catalog_publication_request_from_dict = CatalogPublicationRequest.from_dict(catalog_publication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


