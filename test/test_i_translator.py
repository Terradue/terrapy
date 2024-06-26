# coding: utf-8

"""
    TerrAPI

    Terradue Core API v2

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.i_translator import ITranslator

class TestITranslator(unittest.TestCase):
    """ITranslator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ITranslator:
        """Test ITranslator
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ITranslator`
        """
        model = ITranslator()
        if include_optional:
            return ITranslator(
                label = '',
                priority = 56,
                key = ''
            )
        else:
            return ITranslator(
        )
        """

    def testITranslator(self):
        """Test ITranslator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
