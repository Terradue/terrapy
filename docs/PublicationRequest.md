# PublicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**catalog_id** | **str** |  | 
**token** | [**AccessToken**](AccessToken.md) |  | [optional] 
**url** | **str** |  | 
**additional_links** | [**List[Link]**](Link.md) |  | [optional] 
**subjects** | [**List[Subject]**](Subject.md) |  | [optional] 
**collection** | **str** | Path in the workspace where the imported data will be stored.  Not mandatory, usually the service prepares a unique path according to the type of import | [optional] 
**depth** | **int** |  | [optional] 
**background_job_id** | **str** |  | [optional] 
**publication_link** | [**List[Link]**](Link.md) |  | [optional] 
**context_id** | **str** |  | [optional] 
**properties** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.publication_request import PublicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationRequest from a JSON string
publication_request_instance = PublicationRequest.from_json(json)
# print the JSON string representation of the object
print(PublicationRequest.to_json())

# convert the object into a dict
publication_request_dict = publication_request_instance.to_dict()
# create an instance of PublicationRequest from a dict
publication_request_form_dict = publication_request.from_dict(publication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


