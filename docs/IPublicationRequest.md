# IPublicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**background_job_id** | **str** |  | [optional] [readonly] 
**url** | **str** |  | [optional] [readonly] 
**catalog_id** | **str** |  | [optional] [readonly] 
**additional_links** | [**List[Link]**](Link.md) |  | [optional] [readonly] 
**subjects** | [**List[ISubject]**](ISubject.md) |  | [optional] [readonly] 
**collection** | **str** |  | [optional] [readonly] 
**depth** | **int** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.i_publication_request import IPublicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IPublicationRequest from a JSON string
i_publication_request_instance = IPublicationRequest.from_json(json)
# print the JSON string representation of the object
print(IPublicationRequest.to_json())

# convert the object into a dict
i_publication_request_dict = i_publication_request_instance.to_dict()
# create an instance of IPublicationRequest from a dict
i_publication_request_form_dict = i_publication_request.from_dict(i_publication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


