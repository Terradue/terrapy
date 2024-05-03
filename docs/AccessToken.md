# AccessToken

Represents an access token used for authentication and authorization.  https://www.oauth.com/oauth2-servers/access-tokens/access-token-response/

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the ID of the access token. | [optional] 
**principal_id** | **str** | Gets or sets the principal ID associated with the access token. | 
**token** | **str** | Gets or sets the access token. | 
**valid_to** | **datetime** | Gets or sets the expiration date and time of the access token. | 
**refresh_token** | **str** | Gets or sets the refresh token associated with the access token. | [optional] 
**id_token** | **str** | Gets or sets the ID token associated with the access token. | [optional] 

## Example

```python
from openapi_client.models.access_token import AccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of AccessToken from a JSON string
access_token_instance = AccessToken.from_json(json)
# print the JSON string representation of the object
print(AccessToken.to_json())

# convert the object into a dict
access_token_dict = access_token_instance.to_dict()
# create an instance of AccessToken from a dict
access_token_from_dict = AccessToken.from_dict(access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


