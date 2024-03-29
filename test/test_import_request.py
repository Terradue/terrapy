# coding: utf-8

"""
    Core API v2

    Terradue Core API v2

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.import_request import ImportRequest

class TestImportRequest(unittest.TestCase):
    """ImportRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportRequest:
        """Test ImportRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportRequest`
        """
        model = ImportRequest()
        if include_optional:
            return ImportRequest(
                id = '',
                ref = '',
                workspace_id = '0',
                token = openapi_client.models.access_token.AccessToken(
                    id = '', 
                    principal_id = '0', 
                    token = '0', 
                    valid_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    refresh_token = '', 
                    id_token = '', ),
                url = '0',
                asset_filters = [
                    ''
                    ],
                path = '',
                fail_on_error = True,
                background_job_id = '',
                imported_link = None,
                context_id = ''
            )
        else:
            return ImportRequest(
                workspace_id = '0',
                url = '0',
        )
        """

    def testImportRequest(self):
        """Test ImportRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
