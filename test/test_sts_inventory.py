# coding: utf-8

"""
    TerrAPI

    Terradue Core API v2

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sts_inventory import StsInventory

class TestStsInventory(unittest.TestCase):
    """StsInventory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StsInventory:
        """Test StsInventory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StsInventory`
        """
        model = StsInventory()
        if include_optional:
            return StsInventory(
                storage = openapi_client.models.i_inventory_point.IInventoryPoint(
                    inventory_type = 'UNKNOWN', 
                    inventory_point_uri = '', 
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
                credentials = openapi_client.models.i_inventory_sts.IInventorySTS(
                    api_key = '', 
                    token = '', 
                    expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return StsInventory(
        )
        """

    def testStsInventory(self):
        """Test StsInventory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
