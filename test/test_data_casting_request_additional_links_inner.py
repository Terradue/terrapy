# coding: utf-8

"""
    Core API v2

    Terradue Core API v2

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.data_casting_request_additional_links_inner import DataCastingRequestAdditionalLinksInner

class TestDataCastingRequestAdditionalLinksInner(unittest.TestCase):
    """DataCastingRequestAdditionalLinksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataCastingRequestAdditionalLinksInner:
        """Test DataCastingRequestAdditionalLinksInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataCastingRequestAdditionalLinksInner`
        """
        model = DataCastingRequestAdditionalLinksInner()
        if include_optional:
            return DataCastingRequestAdditionalLinksInner(
                type = '',
                rel = '',
                title = '',
                href = ''
            )
        else:
            return DataCastingRequestAdditionalLinksInner(
                rel = '',
        )
        """

    def testDataCastingRequestAdditionalLinksInner(self):
        """Test DataCastingRequestAdditionalLinksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
