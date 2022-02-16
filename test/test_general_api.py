# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. By default, enpoints use 1 unit per name (ex. Gender), but Ethnicity classification uses 10 to 20 units per name depending on taxonomy. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.18
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.general_api import GeneralApi  # noqa: E501
from openapi_client.rest import ApiException


class TestGeneralApi(unittest.TestCase):
    """GeneralApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.general_api.GeneralApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_name_type(self):
        """Test case for name_type

        Infer the likely type of a proper noun (personal name, brand name, place name etc.)  # noqa: E501
        """
        pass

    def test_name_type_batch(self):
        """Test case for name_type_batch

        Infer the likely common type of up to 100 proper nouns (personal name, brand name, place name etc.)  # noqa: E501
        """
        pass

    def test_name_type_geo(self):
        """Test case for name_type_geo

        Infer the likely type of a proper noun (personal name, brand name, place name etc.)  # noqa: E501
        """
        pass

    def test_name_type_geo_batch(self):
        """Test case for name_type_geo_batch

        Infer the likely common type of up to 100 proper nouns (personal name, brand name, place name etc.)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
