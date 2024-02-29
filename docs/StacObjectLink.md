# StacObjectLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rel** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.stac_object_link import StacObjectLink

# TODO update the JSON string below
json = "{}"
# create an instance of StacObjectLink from a JSON string
stac_object_link_instance = StacObjectLink.from_json(json)
# print the JSON string representation of the object
print StacObjectLink.to_json()

# convert the object into a dict
stac_object_link_dict = stac_object_link_instance.to_dict()
# create an instance of StacObjectLink from a dict
stac_object_link_form_dict = stac_object_link.from_dict(stac_object_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


