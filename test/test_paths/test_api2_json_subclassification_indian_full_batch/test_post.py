# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.api2_json_subclassification_indian_full_batch import post  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApi2JsonSubclassificationIndianFullBatch(ApiTestMixin, unittest.TestCase):
    """
    Api2JsonSubclassificationIndianFullBatch unit test stubs
        [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
