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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IStorageSTS(BaseModel):
    """
    IStorageSTS
    """ # noqa: E501
    access_key: Optional[StrictStr] = Field(default=None, alias="accessKey")
    secret_key: Optional[StrictStr] = Field(default=None, alias="secretKey")
    use_token: Optional[StrictBool] = Field(default=None, alias="useToken")
    token: Optional[StrictStr] = None
    expiration: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["accessKey", "secretKey", "useToken", "token", "expiration"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IStorageSTS from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "access_key",
            "secret_key",
            "use_token",
            "token",
            "expiration",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if access_key (nullable) is None
        # and model_fields_set contains the field
        if self.access_key is None and "access_key" in self.model_fields_set:
            _dict['accessKey'] = None

        # set to None if secret_key (nullable) is None
        # and model_fields_set contains the field
        if self.secret_key is None and "secret_key" in self.model_fields_set:
            _dict['secretKey'] = None

        # set to None if token (nullable) is None
        # and model_fields_set contains the field
        if self.token is None and "token" in self.model_fields_set:
            _dict['token'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IStorageSTS from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessKey": obj.get("accessKey"),
            "secretKey": obj.get("secretKey"),
            "useToken": obj.get("useToken"),
            "token": obj.get("token"),
            "expiration": obj.get("expiration")
        })
        return _obj


