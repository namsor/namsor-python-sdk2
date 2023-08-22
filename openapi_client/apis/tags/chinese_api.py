# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. By default, enpoints use 1 unit per name (ex. Gender), but Ethnicity classification uses 10 to 20 units per name depending on taxonomy. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    The version of the OpenAPI document: 2.0.27
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api2_json_chinese_name_candidates_chinese_surname_latin_chinese_given_name_latin.get import ChineseNameCandidates
from openapi_client.paths.api2_json_chinese_name_candidates_batch.post import ChineseNameCandidatesBatch
from openapi_client.paths.api2_json_chinese_name_candidates_gender_batch.post import ChineseNameCandidatesGenderBatch
from openapi_client.paths.api2_json_chinese_name_gender_candidates_chinese_surname_latin_chinese_given_name_latin_known_gender.get import ChineseNameGenderCandidates
from openapi_client.paths.api2_json_chinese_name_match_chinese_surname_latin_chinese_given_name_latin_chinese_name.get import ChineseNameMatch
from openapi_client.paths.api2_json_chinese_name_match_batch.post import ChineseNameMatchBatch
from openapi_client.paths.api2_json_gender_chinese_name_chinese_name.get import GenderChineseName
from openapi_client.paths.api2_json_gender_chinese_name_batch.post import GenderChineseNameBatch
from openapi_client.paths.api2_json_gender_chinese_name_pinyin_chinese_surname_latin_chinese_given_name_latin.get import GenderChineseNamePinyin
from openapi_client.paths.api2_json_gender_chinese_name_pinyin_batch.post import GenderChineseNamePinyinBatch
from openapi_client.paths.api2_json_parse_chinese_name_chinese_name.get import ParseChineseName
from openapi_client.paths.api2_json_parse_chinese_name_batch.post import ParseChineseNameBatch
from openapi_client.paths.api2_json_pinyin_chinese_name_chinese_name.get import PinyinChineseName
from openapi_client.paths.api2_json_pinyin_chinese_name_batch.post import PinyinChineseNameBatch


class ChineseApi(
    ChineseNameCandidates,
    ChineseNameCandidatesBatch,
    ChineseNameCandidatesGenderBatch,
    ChineseNameGenderCandidates,
    ChineseNameMatch,
    ChineseNameMatchBatch,
    GenderChineseName,
    GenderChineseNameBatch,
    GenderChineseNamePinyin,
    GenderChineseNamePinyinBatch,
    ParseChineseName,
    ParseChineseNameBatch,
    PinyinChineseName,
    PinyinChineseNameBatch,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
