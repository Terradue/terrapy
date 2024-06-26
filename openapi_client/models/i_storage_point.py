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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.auth_resource_type import AuthResourceType
from openapi_client.models.i_resource_status import IResourceStatus
from openapi_client.models.storage_type import StorageType
from typing import Optional, Set
from typing_extensions import Self

class IStoragePoint(BaseModel):
    """
    IStoragePoint
    """ # noqa: E501
    storage_type: Optional[StorageType] = Field(default=None, alias="storageType")
    storage_point_uri: Optional[StrictStr] = Field(default=None, alias="storagePointUri")
    service_uri: Optional[StrictStr] = Field(default=None, alias="serviceUri")
    initialized: Optional[StrictBool] = None
    end_point: Optional[StrictStr] = Field(default=None, alias="endPoint")
    remote_id: Optional[StrictStr] = Field(default=None, alias="remoteId")
    resource_server: Optional[StrictStr] = Field(default=None, alias="resourceServer")
    owner: Optional[StrictStr] = None
    type: AuthResourceType
    status: Optional[IResourceStatus] = None
    resource_uris: List[StrictStr]
    scopes: Optional[List[StrictStr]] = None
    properties: Dict[str, List[Any]]
    platform_id: Optional[StrictStr] = Field(default=None, alias="platformId")
    name: Annotated[str, Field(min_length=1, strict=True)]
    var_self: Optional[StrictStr] = Field(default=None, alias="self")
    __properties: ClassVar[List[str]] = ["storageType", "storagePointUri", "serviceUri", "initialized", "endPoint", "remoteId", "resourceServer", "owner", "type", "status", "resource_uris", "scopes", "properties", "platformId", "name", "self"]

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
        """Create an instance of IStoragePoint from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "storage_point_uri",
            "service_uri",
            "initialized",
            "end_point",
            "remote_id",
            "resource_server",
            "owner",
            "resource_uris",
            "scopes",
            "properties",
            "platform_id",
            "name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # set to None if storage_point_uri (nullable) is None
        # and model_fields_set contains the field
        if self.storage_point_uri is None and "storage_point_uri" in self.model_fields_set:
            _dict['storagePointUri'] = None

        # set to None if service_uri (nullable) is None
        # and model_fields_set contains the field
        if self.service_uri is None and "service_uri" in self.model_fields_set:
            _dict['serviceUri'] = None

        # set to None if end_point (nullable) is None
        # and model_fields_set contains the field
        if self.end_point is None and "end_point" in self.model_fields_set:
            _dict['endPoint'] = None

        # set to None if remote_id (nullable) is None
        # and model_fields_set contains the field
        if self.remote_id is None and "remote_id" in self.model_fields_set:
            _dict['remoteId'] = None

        # set to None if resource_server (nullable) is None
        # and model_fields_set contains the field
        if self.resource_server is None and "resource_server" in self.model_fields_set:
            _dict['resourceServer'] = None

        # set to None if owner (nullable) is None
        # and model_fields_set contains the field
        if self.owner is None and "owner" in self.model_fields_set:
            _dict['owner'] = None

        # set to None if scopes (nullable) is None
        # and model_fields_set contains the field
        if self.scopes is None and "scopes" in self.model_fields_set:
            _dict['scopes'] = None

        # set to None if platform_id (nullable) is None
        # and model_fields_set contains the field
        if self.platform_id is None and "platform_id" in self.model_fields_set:
            _dict['platformId'] = None

        # set to None if var_self (nullable) is None
        # and model_fields_set contains the field
        if self.var_self is None and "var_self" in self.model_fields_set:
            _dict['self'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IStoragePoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "storageType": obj.get("storageType"),
            "storagePointUri": obj.get("storagePointUri"),
            "serviceUri": obj.get("serviceUri"),
            "initialized": obj.get("initialized"),
            "endPoint": obj.get("endPoint"),
            "remoteId": obj.get("remoteId"),
            "resourceServer": obj.get("resourceServer"),
            "owner": obj.get("owner"),
            "type": obj.get("type"),
            "status": IResourceStatus.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "resource_uris": obj.get("resource_uris"),
            "scopes": obj.get("scopes"),
            "properties": obj.get("properties"),
            "platformId": obj.get("platformId"),
            "name": obj.get("name"),
            "self": obj.get("self")
        })
        return _obj


