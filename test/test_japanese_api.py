# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. By default, enpoints use 1 unit per name (ex. Gender), but Ethnicity classification uses 10 to 20 units per name depending on taxonomy. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.26
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.japanese_api import JapaneseApi  # noqa: E501
from openapi_client.rest import ApiException


class TestJapaneseApi(unittest.TestCase):
    """JapaneseApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.japanese_api.JapaneseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_gender_japanese_name_full(self):
        """Test case for gender_japanese_name_full

        Infer the likely gender of a Japanese full name ex. 王晓明  # noqa: E501
        """
        pass

    def test_gender_japanese_name_full_batch(self):
        """Test case for gender_japanese_name_full_batch

        Infer the likely gender of up to 100 full names  # noqa: E501
        """
        pass

    def test_gender_japanese_name_pinyin(self):
        """Test case for gender_japanese_name_pinyin

        Infer the likely gender of a Japanese name in LATIN (Pinyin).  # noqa: E501
        """
        pass

    def test_gender_japanese_name_pinyin_batch(self):
        """Test case for gender_japanese_name_pinyin_batch

        Infer the likely gender of up to 100 Japanese names in LATIN (Pinyin).  # noqa: E501
        """
        pass

    def test_japanese_name_gender_kanji_candidates_batch(self):
        """Test case for japanese_name_gender_kanji_candidates_batch

        Identify japanese name candidates in KANJI, based on the romanized name (firstName = japaneseGivenName; lastName=japaneseSurname) with KNOWN gender, ex. Yamamoto Sanae  # noqa: E501
        """
        pass

    def test_japanese_name_kanji_candidates(self):
        """Test case for japanese_name_kanji_candidates

        Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae  # noqa: E501
        """
        pass

    def test_japanese_name_kanji_candidates1(self):
        """Test case for japanese_name_kanji_candidates1

        Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae - and a known gender.  # noqa: E501
        """
        pass

    def test_japanese_name_kanji_candidates_batch(self):
        """Test case for japanese_name_kanji_candidates_batch

        Identify japanese name candidates in KANJI, based on the romanized name (firstName = japaneseGivenName; lastName=japaneseSurname), ex. Yamamoto Sanae  # noqa: E501
        """
        pass

    def test_japanese_name_latin_candidates(self):
        """Test case for japanese_name_latin_candidates

        Romanize japanese name, based on the name in Kanji.  # noqa: E501
        """
        pass

    def test_japanese_name_latin_candidates_batch(self):
        """Test case for japanese_name_latin_candidates_batch

        Romanize japanese names, based on the name in KANJI  # noqa: E501
        """
        pass

    def test_japanese_name_match(self):
        """Test case for japanese_name_match

        Return a score for matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae  # noqa: E501
        """
        pass

    def test_japanese_name_match_batch(self):
        """Test case for japanese_name_match_batch

        Return a score for matching a list of Japanese names in KANJI ex. 山本 早苗 with romanized names ex. Yamamoto Sanae  # noqa: E501
        """
        pass

    def test_japanese_name_match_feedback_loop(self):
        """Test case for japanese_name_match_feedback_loop

        [CREDITS 1 UNIT] Feedback loop to better perform matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae  # noqa: E501
        """
        pass

    def test_parse_japanese_name(self):
        """Test case for parse_japanese_name

        Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae  # noqa: E501
        """
        pass

    def test_parse_japanese_name_batch(self):
        """Test case for parse_japanese_name_batch

        Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
