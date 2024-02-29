# coding: utf-8

"""
    Core API v2

    Terradue Core API v2

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.i_shared_folder import ISharedFolder

class TestISharedFolder(unittest.TestCase):
    """ISharedFolder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ISharedFolder:
        """Test ISharedFolder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ISharedFolder`
        """
        model = ISharedFolder()
        if include_optional:
            return ISharedFolder(
                storage_type = 'UNKNOWN',
                storage_point_uri = '',
                service_uri = '',
                initialized = True,
                remote_id = '',
                resource_server = '',
                owner = '',
                type = 'urn:resource:storage:workspace',
                status = openapi_client.models.i_resource_status.IResourceStatus(
                    status_code = 0, 
                    message = '', ),
                resource_uris = [
                    ''
                    ],
                scopes = [
                    ''
                    ],
                properties = {
                    'key' : [
                        null
                        ]
                    },
                platform_id = '',
                name = '0',
                var_self = '',
                background_job_id = ''
            )
        else:
            return ISharedFolder(
                type = 'urn:resource:storage:workspace',
                resource_uris = [
                    ''
                    ],
                properties = {
                    'key' : [
                        null
                        ]
                    },
                name = '0',
        )
        """

    def testISharedFolder(self):
        """Test ISharedFolder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()