# ITranslator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 
**priority** | **int** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.i_translator import ITranslator

# TODO update the JSON string below
json = "{}"
# create an instance of ITranslator from a JSON string
i_translator_instance = ITranslator.from_json(json)
# print the JSON string representation of the object
print(ITranslator.to_json())

# convert the object into a dict
i_translator_dict = i_translator_instance.to_dict()
# create an instance of ITranslator from a dict
i_translator_from_dict = ITranslator.from_dict(i_translator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


