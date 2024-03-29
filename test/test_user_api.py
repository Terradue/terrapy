# coding: utf-8

"""
    Core API v2

    Terradue Core API v2

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_v2_user_info_get(self) -> None:
        """Test case for v2_user_info_get

        Get the principal user identities from the identity management system
        """
        pass

    def test_v2_user_platforms_get(self) -> None:
        """Test case for v2_user_platforms_get

        Get the principal user identities from the identity management system
        """
        pass


if __name__ == '__main__':
    unittest.main()
