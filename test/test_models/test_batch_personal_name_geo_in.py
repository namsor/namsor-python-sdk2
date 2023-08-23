# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. By default, enpoints use 1 unit per name (ex. Gender), but Ethnicity classification uses 10 to 20 units per name depending on taxonomy. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    The version of the OpenAPI document: 2.0.27
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""

import unittest

import openapi_client
from openapi_client.model.batch_personal_name_geo_in import BatchPersonalNameGeoIn
from openapi_client import configuration


class TestBatchPersonalNameGeoIn(unittest.TestCase):
    """BatchPersonalNameGeoIn unit test stubs"""
    _configuration = configuration.Configuration()


if __name__ == '__main__':
    unittest.main()