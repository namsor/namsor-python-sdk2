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
from openapi_client.api.personal_api import PersonalApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPersonalApi(unittest.TestCase):
    """PersonalApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.personal_api.PersonalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_corridor(self):
        """Test case for corridor

        [USES 20 UNITS PER NAME COUPLE] Infer several classifications for a cross border interaction between names (ex. remit, travel, intl com)  # noqa: E501
        """
        pass

    def test_corridor_batch(self):
        """Test case for corridor_batch

        [USES 20 UNITS PER NAME PAIR] Infer several classifications for up to 100 cross border interaction between names (ex. remit, travel, intl com)  # noqa: E501
        """
        pass

    def test_country(self):
        """Test case for country

        [USES 10 UNITS PER NAME] Infer the likely country of residence of a personal full name, or one surname. Assumes names as they are in the country of residence OR the country of origin.  # noqa: E501
        """
        pass

    def test_country_batch(self):
        """Test case for country_batch

        [USES 10 UNITS PER NAME] Infer the likely country of residence of up to 100 personal full names, or surnames. Assumes names as they are in the country of residence OR the country of origin.  # noqa: E501
        """
        pass

    def test_diaspora(self):
        """Test case for diaspora

        [USES 20 UNITS PER NAME] Infer the likely ethnicity/diaspora of a personal name, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)  # noqa: E501
        """
        pass

    def test_diaspora_batch(self):
        """Test case for diaspora_batch

        [USES 20 UNITS PER NAME] Infer the likely ethnicity/diaspora of up to 100 personal names, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)  # noqa: E501
        """
        pass

    def test_gender(self):
        """Test case for gender

        Infer the likely gender of a name.  # noqa: E501
        """
        pass

    def test_gender1(self):
        """Test case for gender1

        Infer the likely gender of a just a fiven name, assuming default 'US' local context. Please use preferably full names and local geographic context for better accuracy.  # noqa: E501
        """
        pass

    def test_gender_batch(self):
        """Test case for gender_batch

        Infer the likely gender of up to 100 names, detecting automatically the cultural context.  # noqa: E501
        """
        pass

    def test_gender_full(self):
        """Test case for gender_full

        Infer the likely gender of a full name, ex. John H. Smith  # noqa: E501
        """
        pass

    def test_gender_full_batch(self):
        """Test case for gender_full_batch

        Infer the likely gender of up to 100 full names, detecting automatically the cultural context.  # noqa: E501
        """
        pass

    def test_gender_full_geo(self):
        """Test case for gender_full_geo

        Infer the likely gender of a full name, given a local context (ISO2 country code).  # noqa: E501
        """
        pass

    def test_gender_full_geo_batch(self):
        """Test case for gender_full_geo_batch

        Infer the likely gender of up to 100 full names, with a given cultural context (country ISO2 code).  # noqa: E501
        """
        pass

    def test_gender_geo(self):
        """Test case for gender_geo

        Infer the likely gender of a name, given a local context (ISO2 country code).  # noqa: E501
        """
        pass

    def test_gender_geo_batch(self):
        """Test case for gender_geo_batch

        Infer the likely gender of up to 100 names, each given a local context (ISO2 country code).  # noqa: E501
        """
        pass

    def test_origin(self):
        """Test case for origin

        [USES 10 UNITS PER NAME] Infer the likely country of origin of a personal name. Assumes names as they are in the country of origin. For US, CA, AU, NZ and other melting-pots : use 'diaspora' instead.  # noqa: E501
        """
        pass

    def test_origin_batch(self):
        """Test case for origin_batch

        [USES 10 UNITS PER NAME] Infer the likely country of origin of up to 100 names, detecting automatically the cultural context.  # noqa: E501
        """
        pass

    def test_parse_name(self):
        """Test case for parse_name

        Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John.   # noqa: E501
        """
        pass

    def test_parse_name_batch(self):
        """Test case for parse_name_batch

        Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John.  # noqa: E501
        """
        pass

    def test_parse_name_geo(self):
        """Test case for parse_name_geo

        Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. For better accuracy, provide a geographic context.  # noqa: E501
        """
        pass

    def test_parse_name_geo_batch(self):
        """Test case for parse_name_geo_batch

        Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. Giving a local context improves precision.   # noqa: E501
        """
        pass

    def test_subclassification(self):
        """Test case for subclassification

        [USES 10 UNITS PER NAME] Infer the likely origin of a name at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code 'IN').  # noqa: E501
        """
        pass

    def test_subclassification_batch(self):
        """Test case for subclassification_batch

        [USES 10 UNITS PER NAME] Infer the likely origin of a list of up to 100 names at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code 'IN').  # noqa: E501
        """
        pass

    def test_us_race_ethnicity(self):
        """Test case for us_race_ethnicity

        [USES 10 UNITS PER NAME] Infer a US resident's likely race/ethnicity according to US Census taxonomy W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).  # noqa: E501
        """
        pass

    def test_us_race_ethnicity_batch(self):
        """Test case for us_race_ethnicity_batch

        [USES 10 UNITS PER NAME] Infer up-to 100 US resident's likely race/ethnicity according to US Census taxonomy. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).  # noqa: E501
        """
        pass

    def test_us_race_ethnicity_zip5(self):
        """Test case for us_race_ethnicity_zip5

        [USES 10 UNITS PER NAME] Infer a US resident's likely race/ethnicity according to US Census taxonomy, using (optional) ZIP5 code info. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).  # noqa: E501
        """
        pass

    def test_us_zip_race_ethnicity_batch(self):
        """Test case for us_zip_race_ethnicity_batch

        [USES 10 UNITS PER NAME] Infer up-to 100 US resident's likely race/ethnicity according to US Census taxonomy, with (optional) ZIP code. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
