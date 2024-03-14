# coding: utf-8

"""
    TerrAPI

    Terradue Core API v2

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_catalogue_by_id401_response import GetCatalogueById401Response

class TestGetCatalogueById401Response(unittest.TestCase):
    """GetCatalogueById401Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCatalogueById401Response:
        """Test GetCatalogueById401Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCatalogueById401Response`
        """
        model = GetCatalogueById401Response()
        if include_optional:
            return GetCatalogueById401Response(
                type = '',
                title = '',
                status = 56,
                detail = '',
                instance = '',
                errors = {
                    'key' : [
                        ''
                        ]
                    }
            )
        else:
            return GetCatalogueById401Response(
        )
        """

    def testGetCatalogueById401Response(self):
        """Test GetCatalogueById401Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
