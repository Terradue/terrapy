# StacLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**rel** | **str** |  | 
**title** | **str** |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.stac_link import StacLink

# TODO update the JSON string below
json = "{}"
# create an instance of StacLink from a JSON string
stac_link_instance = StacLink.from_json(json)
# print the JSON string representation of the object
print StacLink.to_json()

# convert the object into a dict
stac_link_dict = stac_link_instance.to_dict()
# create an instance of StacLink from a dict
stac_link_form_dict = stac_link.from_dict(stac_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


