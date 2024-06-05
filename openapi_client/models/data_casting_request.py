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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.data_casting_enum import DataCastingEnum
from openapi_client.models.link import Link
from openapi_client.models.subject import Subject
from typing import Optional, Set
from typing_extensions import Self

class DataCastingRequest(BaseModel):
    """
    DataCastingRequest
    """ # noqa: E501
    url: Annotated[str, Field(min_length=1, strict=True)]
    catalog_id: Annotated[str, Field(min_length=1, strict=True)]
    workspace_id: Annotated[str, Field(min_length=1, strict=True)]
    processor_id: Annotated[str, Field(min_length=1, strict=True)]
    additional_links: Optional[List[Link]] = None
    subjects: Optional[List[Subject]] = None
    collection: Optional[StrictStr] = None
    asset_filters: Optional[List[StrictStr]] = None
    path: Optional[StrictStr] = None
    casting: Optional[DataCastingEnum] = None
    depth: Optional[StrictInt] = None
    background_job_id: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    assets_filters: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["url", "catalog_id", "workspace_id", "processor_id", "additional_links", "subjects", "collection", "asset_filters", "path", "casting", "depth", "background_job_id", "id", "assets_filters"]

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
        """Create an instance of DataCastingRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in additional_links (list)
        _items = []
        if self.additional_links:
            for _item in self.additional_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additional_links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in subjects (list)
        _items = []
        if self.subjects:
            for _item in self.subjects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subjects'] = _items
        # set to None if additional_links (nullable) is None
        # and model_fields_set contains the field
        if self.additional_links is None and "additional_links" in self.model_fields_set:
            _dict['additional_links'] = None

        # set to None if subjects (nullable) is None
        # and model_fields_set contains the field
        if self.subjects is None and "subjects" in self.model_fields_set:
            _dict['subjects'] = None

        # set to None if collection (nullable) is None
        # and model_fields_set contains the field
        if self.collection is None and "collection" in self.model_fields_set:
            _dict['collection'] = None

        # set to None if asset_filters (nullable) is None
        # and model_fields_set contains the field
        if self.asset_filters is None and "asset_filters" in self.model_fields_set:
            _dict['asset_filters'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if background_job_id (nullable) is None
        # and model_fields_set contains the field
        if self.background_job_id is None and "background_job_id" in self.model_fields_set:
            _dict['background_job_id'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if assets_filters (nullable) is None
        # and model_fields_set contains the field
        if self.assets_filters is None and "assets_filters" in self.model_fields_set:
            _dict['assets_filters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataCastingRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "catalog_id": obj.get("catalog_id"),
            "workspace_id": obj.get("workspace_id"),
            "processor_id": obj.get("processor_id"),
            "additional_links": [Link.from_dict(_item) for _item in obj["additional_links"]] if obj.get("additional_links") is not None else None,
            "subjects": [Subject.from_dict(_item) for _item in obj["subjects"]] if obj.get("subjects") is not None else None,
            "collection": obj.get("collection"),
            "asset_filters": obj.get("asset_filters"),
            "path": obj.get("path"),
            "casting": obj.get("casting"),
            "depth": obj.get("depth"),
            "background_job_id": obj.get("background_job_id"),
            "id": obj.get("id"),
            "assets_filters": obj.get("assets_filters")
        })
        return _obj


