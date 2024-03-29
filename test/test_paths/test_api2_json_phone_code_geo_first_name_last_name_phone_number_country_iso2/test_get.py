# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.api2_json_phone_code_geo_first_name_last_name_phone_number_country_iso2 import get  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApi2JsonPhoneCodeGeoFirstNameLastNamePhoneNumberCountryIso2(ApiTestMixin, unittest.TestCase):
    """
    Api2JsonPhoneCodeGeoFirstNameLastNamePhoneNumberCountryIso2 unit test stubs
        [USES 11 UNITS PER NAME] Infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).  # noqa: E501
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
