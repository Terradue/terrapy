# coding: utf-8

"""
    TerrAPI

    Terradue Core API v2

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class AccessToken(BaseModel):
    """
    Represents an access token used for authentication and authorization.  https://www.oauth.com/oauth2-servers/access-tokens/access-token-response/
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Gets or sets the ID of the access token.")
    principal_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Gets or sets the principal ID associated with the access token.", alias="principalId")
    token: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Gets or sets the access token.")
    valid_to: datetime = Field(description="Gets or sets the expiration date and time of the access token.", alias="validTo")
    refresh_token: Optional[StrictStr] = Field(default=None, description="Gets or sets the refresh token associated with the access token.", alias="refreshToken")
    id_token: Optional[StrictStr] = Field(default=None, description="Gets or sets the ID token associated with the access token.", alias="idToken")
    __properties: ClassVar[List[str]] = ["id", "principalId", "token", "validTo", "refreshToken", "idToken"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AccessToken from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if refresh_token (nullable) is None
        # and model_fields_set contains the field
        if self.refresh_token is None and "refresh_token" in self.model_fields_set:
            _dict['refreshToken'] = None

        # set to None if id_token (nullable) is None
        # and model_fields_set contains the field
        if self.id_token is None and "id_token" in self.model_fields_set:
            _dict['idToken'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "principalId": obj.get("principalId"),
            "token": obj.get("token"),
            "validTo": obj.get("validTo"),
            "refreshToken": obj.get("refreshToken"),
            "idToken": obj.get("idToken")
        })
        return _obj


