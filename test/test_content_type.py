# coding: utf-8

"""
    TerrAPI

    Terradue Core API v2

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.content_type import ContentType

class TestContentType(unittest.TestCase):
    """ContentType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentType:
        """Test ContentType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentType`
        """
        model = ContentType()
        if include_optional:
            return ContentType(
                boundary = '',
                char_set = '',
                media_type = '',
                name = '',
                parameters = [
                    null
                    ]
            )
        else:
            return ContentType(
        )
        """

    def testContentType(self):
        """Test ContentType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
