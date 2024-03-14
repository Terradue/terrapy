# coding: utf-8

"""
    TerrAPI

    Terradue Core API v2

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sts_storage import StsStorage

class TestStsStorage(unittest.TestCase):
    """StsStorage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StsStorage:
        """Test StsStorage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StsStorage`
        """
        model = StsStorage()
        if include_optional:
            return StsStorage(
                storage = openapi_client.models.i_storage_point.IStoragePoint(
                    storage_type = 'UNKNOWN', 
                    storage_point_uri = '', 
                    service_uri = '', 
                    initialized = True, 
                    remote_id = '', 
                    resource_server = '', 
                    owner = '', 
                    type = 'StorageWorkspace', 
                    status = openapi_client.models.i_resource_status.IResourceStatus(
                        status_code = 'OK', 
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
                    self = '', ),
                credentials = openapi_client.models.i_storage_sts.IStorageSTS(
                    access_key = '', 
                    secret_key = '', 
                    use_token = True, 
                    token = '', 
                    expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return StsStorage(
        )
        """

    def testStsStorage(self):
        """Test StsStorage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
