# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.api2_json_chinese_name_gender_candidates_chinese_surname_latin_chinese_given_name_latin_known_gender import get  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApi2JsonChineseNameGenderCandidatesChineseSurnameLatinChineseGivenNameLatinKnownGender(ApiTestMixin, unittest.TestCase):
    """
    Api2JsonChineseNameGenderCandidatesChineseSurnameLatinChineseGivenNameLatinKnownGender unit test stubs
        Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming - having a known gender ('male' or 'female')  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
