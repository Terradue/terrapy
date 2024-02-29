# PrincipalContext

Represents the context of a principal, which provides access to identity-related information and functionality.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tokens** | [**AccessToken**](AccessToken.md) |  | [optional] 
**name** | **str** | Gets the name of the principal. | [optional] [readonly] 
**claims** | [**List[ClaimLite]**](ClaimLite.md) | Gets the claims associated with the principal. | [optional] [readonly] 

## Example

```python
from openapi_client.models.principal_context import PrincipalContext

# TODO update the JSON string below
json = "{}"
# create an instance of PrincipalContext from a JSON string
principal_context_instance = PrincipalContext.from_json(json)
# print the JSON string representation of the object
print PrincipalContext.to_json()

# convert the object into a dict
principal_context_dict = principal_context_instance.to_dict()
# create an instance of PrincipalContext from a dict
principal_context_form_dict = principal_context.from_dict(principal_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


