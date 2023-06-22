# openapi-client
NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. By default, enpoints use 1 unit per name (ex. Gender), but Ethnicity classification uses 10 to 20 units per name depending on taxonomy. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it! 

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.26
- Package version: 2.0.26
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [http://www.namsor.com/](http://www.namsor.com/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/namsor/namsor-python-sdk2.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/namsor/namsor-python-sdk2.git`)

Then import the package:
```python
import openapi_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = openapi_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
first_name = 'first_name_example' # str | 
last_name = 'last_name_example' # str | 
country_iso2 = 'country_iso2_example' # str | 

try:
    # Infer the likely gender of a name, given a local context (ISO2 country code).
    api_response = api_instance.gender_geo(first_name, last_name, country_iso2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->gender_geo: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**anonymize**](docs/AdminApi.md#anonymize) | **GET** /api2/json/anonymize/{source}/{anonymized}/{token} | Activate/deactivate anonymization for a source.
*AdminApi* | [**api_key_info**](docs/AdminApi.md#api_key_info) | **GET** /api2/json/apiKeyInfo | Read API Key info.
*AdminApi* | [**api_status**](docs/AdminApi.md#api_status) | **GET** /api2/json/apiStatus | Prints the current status of the classifiers. A classifier name in apiStatus corresponds to a service name in apiServices.
*AdminApi* | [**api_usage**](docs/AdminApi.md#api_usage) | **GET** /api2/json/apiUsage | Print current API usage.
*AdminApi* | [**api_usage_history**](docs/AdminApi.md#api_usage_history) | **GET** /api2/json/apiUsageHistory | Print historical API usage.
*AdminApi* | [**api_usage_history_aggregate**](docs/AdminApi.md#api_usage_history_aggregate) | **GET** /api2/json/apiUsageHistoryAggregate | Print historical API usage (in an aggregated view, by service, by day/hour/min).
*AdminApi* | [**available_services**](docs/AdminApi.md#available_services) | **GET** /api2/json/apiServices | List of classification services and usage cost in Units per classification (default is 1&#x3D;ONE Unit). Some API endpoints (ex. Corridor) combine multiple classifiers.
*AdminApi* | [**learnable**](docs/AdminApi.md#learnable) | **GET** /api2/json/learnable/{source}/{learnable}/{token} | Activate/deactivate learning from a source.
*AdminApi* | [**regions**](docs/AdminApi.md#regions) | **GET** /api2/json/regions | Print basic source statistics.
*AdminApi* | [**software_version**](docs/AdminApi.md#software_version) | **GET** /api2/json/softwareVersion | Get the current software version
*AdminApi* | [**taxonomy_classes**](docs/AdminApi.md#taxonomy_classes) | **GET** /api2/json/taxonomyClasses/{classifierName} | Print the taxonomy classes valid for the given classifier.
*ChineseApi* | [**chinese_name_candidates**](docs/ChineseApi.md#chinese_name_candidates) | **GET** /api2/json/chineseNameCandidates/{chineseSurnameLatin}/{chineseGivenNameLatin} | Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming
*ChineseApi* | [**chinese_name_candidates_batch**](docs/ChineseApi.md#chinese_name_candidates_batch) | **POST** /api2/json/chineseNameCandidatesBatch | Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname), ex. Wang Xiaoming
*ChineseApi* | [**chinese_name_candidates_gender_batch**](docs/ChineseApi.md#chinese_name_candidates_gender_batch) | **POST** /api2/json/chineseNameCandidatesGenderBatch | Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname) ex. Wang Xiaoming.
*ChineseApi* | [**chinese_name_gender_candidates**](docs/ChineseApi.md#chinese_name_gender_candidates) | **GET** /api2/json/chineseNameGenderCandidates/{chineseSurnameLatin}/{chineseGivenNameLatin}/{knownGender} | Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming - having a known gender (&#39;male&#39; or &#39;female&#39;)
*ChineseApi* | [**chinese_name_match**](docs/ChineseApi.md#chinese_name_match) | **GET** /api2/json/chineseNameMatch/{chineseSurnameLatin}/{chineseGivenNameLatin}/{chineseName} | Return a score for matching Chinese name ex. 王晓明 with a romanized name ex. Wang Xiaoming
*ChineseApi* | [**chinese_name_match_batch**](docs/ChineseApi.md#chinese_name_match_batch) | **POST** /api2/json/chineseNameMatchBatch | Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname), ex. Wang Xiaoming
*ChineseApi* | [**gender_chinese_name**](docs/ChineseApi.md#gender_chinese_name) | **GET** /api2/json/genderChineseName/{chineseName} | Infer the likely gender of a Chinese full name ex. 王晓明
*ChineseApi* | [**gender_chinese_name_batch**](docs/ChineseApi.md#gender_chinese_name_batch) | **POST** /api2/json/genderChineseNameBatch | Infer the likely gender of up to 100 full names ex. 王晓明
*ChineseApi* | [**gender_chinese_name_pinyin**](docs/ChineseApi.md#gender_chinese_name_pinyin) | **GET** /api2/json/genderChineseNamePinyin/{chineseSurnameLatin}/{chineseGivenNameLatin} | Infer the likely gender of a Chinese name in LATIN (Pinyin).
*ChineseApi* | [**gender_chinese_name_pinyin_batch**](docs/ChineseApi.md#gender_chinese_name_pinyin_batch) | **POST** /api2/json/genderChineseNamePinyinBatch | Infer the likely gender of up to 100 Chinese names in LATIN (Pinyin).
*ChineseApi* | [**parse_chinese_name**](docs/ChineseApi.md#parse_chinese_name) | **GET** /api2/json/parseChineseName/{chineseName} | Infer the likely first/last name structure of a name, ex. 王晓明 -&gt; 王(surname) 晓明(given name)
*ChineseApi* | [**parse_chinese_name_batch**](docs/ChineseApi.md#parse_chinese_name_batch) | **POST** /api2/json/parseChineseNameBatch | Infer the likely first/last name structure of a name, ex. 王晓明 -&gt; 王(surname) 晓明(given name).
*ChineseApi* | [**pinyin_chinese_name**](docs/ChineseApi.md#pinyin_chinese_name) | **GET** /api2/json/pinyinChineseName/{chineseName} | Romanize the Chinese name to Pinyin, ex. 王晓明 -&gt; Wang (surname) Xiaoming (given name)
*ChineseApi* | [**pinyin_chinese_name_batch**](docs/ChineseApi.md#pinyin_chinese_name_batch) | **POST** /api2/json/pinyinChineseNameBatch | Romanize a list of Chinese name to Pinyin, ex. 王晓明 -&gt; Wang (surname) Xiaoming (given name).
*GeneralApi* | [**name_type**](docs/GeneralApi.md#name_type) | **GET** /api2/json/nameType/{properNoun} | Infer the likely type of a proper noun (personal name, brand name, place name etc.)
*GeneralApi* | [**name_type_batch**](docs/GeneralApi.md#name_type_batch) | **POST** /api2/json/nameTypeBatch | Infer the likely common type of up to 100 proper nouns (personal name, brand name, place name etc.)
*GeneralApi* | [**name_type_geo**](docs/GeneralApi.md#name_type_geo) | **GET** /api2/json/nameTypeGeo/{properNoun}/{countryIso2} | Infer the likely type of a proper noun (personal name, brand name, place name etc.)
*GeneralApi* | [**name_type_geo_batch**](docs/GeneralApi.md#name_type_geo_batch) | **POST** /api2/json/nameTypeGeoBatch | Infer the likely common type of up to 100 proper nouns (personal name, brand name, place name etc.)
*IndianApi* | [**castegroup_indian_full**](docs/IndianApi.md#castegroup_indian_full) | **GET** /api2/json/castegroupIndianFull/{subDivisionIso31662}/{personalNameFull} | [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of a personal full name.
*IndianApi* | [**castegroup_indian_full_batch**](docs/IndianApi.md#castegroup_indian_full_batch) | **POST** /api2/json/castegroupIndianFullBatch | [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of up to 100 personal full names. 
*IndianApi* | [**religion**](docs/IndianApi.md#religion) | **GET** /api2/json/religionIndianFull/{subDivisionIso31662}/{personalNameFull} | [USES 10 UNITS PER NAME] Infer the likely religion of a personal Indian full name, provided the Indian state or Union territory (NB/ this can be inferred using the subclassification endpoint).
*IndianApi* | [**religion_indian_full_batch**](docs/IndianApi.md#religion_indian_full_batch) | **POST** /api2/json/religionIndianFullBatch | [USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal full Indian names, provided the subclassification at State or Union territory level (NB/ can be inferred using the subclassification endpoint).
*IndianApi* | [**subclassification_indian**](docs/IndianApi.md#subclassification_indian) | **GET** /api2/json/subclassificationIndian/{firstName}/{lastName} | [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.
*IndianApi* | [**subclassification_indian_batch**](docs/IndianApi.md#subclassification_indian_batch) | **POST** /api2/json/subclassificationIndianBatch | [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.
*IndianApi* | [**subclassification_indian_full**](docs/IndianApi.md#subclassification_indian_full) | **GET** /api2/json/subclassificationIndianFull/{fullName} | [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.
*IndianApi* | [**subclassification_indian_full_batch**](docs/IndianApi.md#subclassification_indian_full_batch) | **POST** /api2/json/subclassificationIndianFullBatch | [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.
*JapaneseApi* | [**gender_japanese_name_full**](docs/JapaneseApi.md#gender_japanese_name_full) | **GET** /api2/json/genderJapaneseNameFull/{japaneseName} | Infer the likely gender of a Japanese full name ex. 王晓明
*JapaneseApi* | [**gender_japanese_name_full_batch**](docs/JapaneseApi.md#gender_japanese_name_full_batch) | **POST** /api2/json/genderJapaneseNameFullBatch | Infer the likely gender of up to 100 full names
*JapaneseApi* | [**gender_japanese_name_pinyin**](docs/JapaneseApi.md#gender_japanese_name_pinyin) | **GET** /api2/json/genderJapaneseName/{japaneseSurname}/{japaneseGivenName} | Infer the likely gender of a Japanese name in LATIN (Pinyin).
*JapaneseApi* | [**gender_japanese_name_pinyin_batch**](docs/JapaneseApi.md#gender_japanese_name_pinyin_batch) | **POST** /api2/json/genderJapaneseNameBatch | Infer the likely gender of up to 100 Japanese names in LATIN (Pinyin).
*JapaneseApi* | [**japanese_name_gender_kanji_candidates_batch**](docs/JapaneseApi.md#japanese_name_gender_kanji_candidates_batch) | **POST** /api2/json/japaneseNameGenderKanjiCandidatesBatch | Identify japanese name candidates in KANJI, based on the romanized name (firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname) with KNOWN gender, ex. Yamamoto Sanae
*JapaneseApi* | [**japanese_name_kanji_candidates**](docs/JapaneseApi.md#japanese_name_kanji_candidates) | **GET** /api2/json/japaneseNameKanjiCandidates/{japaneseSurnameLatin}/{japaneseGivenNameLatin} | Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae
*JapaneseApi* | [**japanese_name_kanji_candidates1**](docs/JapaneseApi.md#japanese_name_kanji_candidates1) | **GET** /api2/json/japaneseNameKanjiCandidates/{japaneseSurnameLatin}/{japaneseGivenNameLatin}/{knownGender} | Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae - and a known gender.
*JapaneseApi* | [**japanese_name_kanji_candidates_batch**](docs/JapaneseApi.md#japanese_name_kanji_candidates_batch) | **POST** /api2/json/japaneseNameKanjiCandidatesBatch | Identify japanese name candidates in KANJI, based on the romanized name (firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname), ex. Yamamoto Sanae
*JapaneseApi* | [**japanese_name_latin_candidates**](docs/JapaneseApi.md#japanese_name_latin_candidates) | **GET** /api2/json/japaneseNameLatinCandidates/{japaneseSurnameKanji}/{japaneseGivenNameKanji} | Romanize japanese name, based on the name in Kanji.
*JapaneseApi* | [**japanese_name_latin_candidates_batch**](docs/JapaneseApi.md#japanese_name_latin_candidates_batch) | **POST** /api2/json/japaneseNameLatinCandidatesBatch | Romanize japanese names, based on the name in KANJI
*JapaneseApi* | [**japanese_name_match**](docs/JapaneseApi.md#japanese_name_match) | **GET** /api2/json/japaneseNameMatch/{japaneseSurnameLatin}/{japaneseGivenNameLatin}/{japaneseName} | Return a score for matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae
*JapaneseApi* | [**japanese_name_match_batch**](docs/JapaneseApi.md#japanese_name_match_batch) | **POST** /api2/json/japaneseNameMatchBatch | Return a score for matching a list of Japanese names in KANJI ex. 山本 早苗 with romanized names ex. Yamamoto Sanae
*JapaneseApi* | [**japanese_name_match_feedback_loop**](docs/JapaneseApi.md#japanese_name_match_feedback_loop) | **GET** /api2/json/japaneseNameMatchFeedbackLoop/{japaneseSurnameLatin}/{japaneseGivenNameLatin}/{japaneseName} | [CREDITS 1 UNIT] Feedback loop to better perform matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae
*JapaneseApi* | [**parse_japanese_name**](docs/JapaneseApi.md#parse_japanese_name) | **GET** /api2/json/parseJapaneseName/{japaneseName} | Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae
*JapaneseApi* | [**parse_japanese_name_batch**](docs/JapaneseApi.md#parse_japanese_name_batch) | **POST** /api2/json/parseJapaneseNameBatch | Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae 
*PersonalApi* | [**corridor**](docs/PersonalApi.md#corridor) | **GET** /api2/json/corridor/{countryIso2From}/{firstNameFrom}/{lastNameFrom}/{countryIso2To}/{firstNameTo}/{lastNameTo} | [USES 20 UNITS PER NAME COUPLE] Infer several classifications for a cross border interaction between names (ex. remit, travel, intl com)
*PersonalApi* | [**corridor_batch**](docs/PersonalApi.md#corridor_batch) | **POST** /api2/json/corridorBatch | [USES 20 UNITS PER NAME PAIR] Infer several classifications for up to 100 cross border interaction between names (ex. remit, travel, intl com)
*PersonalApi* | [**country**](docs/PersonalApi.md#country) | **GET** /api2/json/country/{personalNameFull} | [USES 10 UNITS PER NAME] Infer the likely country of residence of a personal full name, or one surname. Assumes names as they are in the country of residence OR the country of origin.
*PersonalApi* | [**country_batch**](docs/PersonalApi.md#country_batch) | **POST** /api2/json/countryBatch | [USES 10 UNITS PER NAME] Infer the likely country of residence of up to 100 personal full names, or surnames. Assumes names as they are in the country of residence OR the country of origin.
*PersonalApi* | [**diaspora**](docs/PersonalApi.md#diaspora) | **GET** /api2/json/diaspora/{countryIso2}/{firstName}/{lastName} | [USES 20 UNITS PER NAME] Infer the likely ethnicity/diaspora of a personal name, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)
*PersonalApi* | [**diaspora_batch**](docs/PersonalApi.md#diaspora_batch) | **POST** /api2/json/diasporaBatch | [USES 20 UNITS PER NAME] Infer the likely ethnicity/diaspora of up to 100 personal names, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)
*PersonalApi* | [**gender**](docs/PersonalApi.md#gender) | **GET** /api2/json/gender/{firstName}/{lastName} | Infer the likely gender of a name.
*PersonalApi* | [**gender1**](docs/PersonalApi.md#gender1) | **GET** /api2/json/gender/{firstName} | Infer the likely gender of a just a fiven name, assuming default &#39;US&#39; local context. Please use preferably full names and local geographic context for better accuracy.
*PersonalApi* | [**gender_batch**](docs/PersonalApi.md#gender_batch) | **POST** /api2/json/genderBatch | Infer the likely gender of up to 100 names, detecting automatically the cultural context.
*PersonalApi* | [**gender_full**](docs/PersonalApi.md#gender_full) | **GET** /api2/json/genderFull/{fullName} | Infer the likely gender of a full name, ex. John H. Smith
*PersonalApi* | [**gender_full_batch**](docs/PersonalApi.md#gender_full_batch) | **POST** /api2/json/genderFullBatch | Infer the likely gender of up to 100 full names, detecting automatically the cultural context.
*PersonalApi* | [**gender_full_geo**](docs/PersonalApi.md#gender_full_geo) | **GET** /api2/json/genderFullGeo/{fullName}/{countryIso2} | Infer the likely gender of a full name, given a local context (ISO2 country code).
*PersonalApi* | [**gender_full_geo_batch**](docs/PersonalApi.md#gender_full_geo_batch) | **POST** /api2/json/genderFullGeoBatch | Infer the likely gender of up to 100 full names, with a given cultural context (country ISO2 code).
*PersonalApi* | [**gender_geo**](docs/PersonalApi.md#gender_geo) | **GET** /api2/json/genderGeo/{firstName}/{lastName}/{countryIso2} | Infer the likely gender of a name, given a local context (ISO2 country code).
*PersonalApi* | [**gender_geo_batch**](docs/PersonalApi.md#gender_geo_batch) | **POST** /api2/json/genderGeoBatch | Infer the likely gender of up to 100 names, each given a local context (ISO2 country code).
*PersonalApi* | [**origin**](docs/PersonalApi.md#origin) | **GET** /api2/json/origin/{firstName}/{lastName} | [USES 10 UNITS PER NAME] Infer the likely country of origin of a personal name. Assumes names as they are in the country of origin. For US, CA, AU, NZ and other melting-pots : use &#39;diaspora&#39; instead.
*PersonalApi* | [**origin_batch**](docs/PersonalApi.md#origin_batch) | **POST** /api2/json/originBatch | [USES 10 UNITS PER NAME] Infer the likely country of origin of up to 100 names, detecting automatically the cultural context.
*PersonalApi* | [**parse_name**](docs/PersonalApi.md#parse_name) | **GET** /api2/json/parseName/{nameFull} | Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. 
*PersonalApi* | [**parse_name_batch**](docs/PersonalApi.md#parse_name_batch) | **POST** /api2/json/parseNameBatch | Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John.
*PersonalApi* | [**parse_name_geo**](docs/PersonalApi.md#parse_name_geo) | **GET** /api2/json/parseName/{nameFull}/{countryIso2} | Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. For better accuracy, provide a geographic context.
*PersonalApi* | [**parse_name_geo_batch**](docs/PersonalApi.md#parse_name_geo_batch) | **POST** /api2/json/parseNameGeoBatch | Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. Giving a local context improves precision. 
*PersonalApi* | [**religion_full**](docs/PersonalApi.md#religion_full) | **GET** /api2/json/religionFull/{countryIso2}/{subDivisionIso31662}/{personalNameFull} | [USES 10 UNITS PER NAME] Infer the likely religion of a personal full name. NB: only for INDIA (as of current version).
*PersonalApi* | [**religion_full_batch**](docs/PersonalApi.md#religion_full_batch) | **POST** /api2/json/religionFullBatch | [USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal full names. NB: only for India as of currently.
*PersonalApi* | [**subclassification**](docs/PersonalApi.md#subclassification) | **GET** /api2/json/subclassification/{countryIso2}/{firstName}/{lastName} | [USES 10 UNITS PER NAME] Infer the likely origin of a name at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code &#39;IN&#39;).
*PersonalApi* | [**subclassification_batch**](docs/PersonalApi.md#subclassification_batch) | **POST** /api2/json/subclassificationBatch | [USES 10 UNITS PER NAME] Infer the likely origin of a list of up to 100 names at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code &#39;IN&#39;).
*PersonalApi* | [**subclassification_full**](docs/PersonalApi.md#subclassification_full) | **GET** /api2/json/subclassificationFull/{countryIso2}/{fullName} | [USES 10 UNITS PER NAME] Infer the likely origin of a name at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code &#39;IN&#39;).
*PersonalApi* | [**subclassification_full_batch**](docs/PersonalApi.md#subclassification_full_batch) | **POST** /api2/json/subclassificationFullBatch | [USES 10 UNITS PER NAME] Infer the likely origin of a list of up to 100 names at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code &#39;IN&#39;).
*PersonalApi* | [**us_race_ethnicity**](docs/PersonalApi.md#us_race_ethnicity) | **GET** /api2/json/usRaceEthnicity/{firstName}/{lastName} | [USES 10 UNITS PER NAME] Infer a US resident&#39;s likely race/ethnicity according to US Census taxonomy W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).
*PersonalApi* | [**us_race_ethnicity_batch**](docs/PersonalApi.md#us_race_ethnicity_batch) | **POST** /api2/json/usRaceEthnicityBatch | [USES 10 UNITS PER NAME] Infer up-to 100 US resident&#39;s likely race/ethnicity according to US Census taxonomy. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).
*PersonalApi* | [**us_race_ethnicity_zip5**](docs/PersonalApi.md#us_race_ethnicity_zip5) | **GET** /api2/json/usRaceEthnicityZIP5/{firstName}/{lastName}/{zip5Code} | [USES 10 UNITS PER NAME] Infer a US resident&#39;s likely race/ethnicity according to US Census taxonomy, using (optional) ZIP5 code info. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).
*PersonalApi* | [**us_zip_race_ethnicity_batch**](docs/PersonalApi.md#us_zip_race_ethnicity_batch) | **POST** /api2/json/usZipRaceEthnicityBatch | [USES 10 UNITS PER NAME] Infer up-to 100 US resident&#39;s likely race/ethnicity according to US Census taxonomy, with (optional) ZIP code. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).
*SocialApi* | [**phone_code**](docs/SocialApi.md#phone_code) | **GET** /api2/json/phoneCode/{firstName}/{lastName}/{phoneNumber} | [USES 11 UNITS PER NAME] Infer the likely country and phone prefix, given a personal name and formatted / unformatted phone number.
*SocialApi* | [**phone_code_batch**](docs/SocialApi.md#phone_code_batch) | **POST** /api2/json/phoneCodeBatch | [USES 11 UNITS PER NAME] Infer the likely country and phone prefix, of up to 100 personal names, detecting automatically the local context given a name and formatted / unformatted phone number.
*SocialApi* | [**phone_code_geo**](docs/SocialApi.md#phone_code_geo) | **GET** /api2/json/phoneCodeGeo/{firstName}/{lastName}/{phoneNumber}/{countryIso2} | [USES 11 UNITS PER NAME] Infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).
*SocialApi* | [**phone_code_geo_batch**](docs/SocialApi.md#phone_code_geo_batch) | **POST** /api2/json/phoneCodeGeoBatch | [USES 11 UNITS PER NAME] Infer the likely country and phone prefix, of up to 100 personal names, with a local context (ISO2 country of residence).
*SocialApi* | [**phone_code_geo_feedback_loop**](docs/SocialApi.md#phone_code_geo_feedback_loop) | **GET** /api2/json/phoneCodeGeoFeedbackLoop/{firstName}/{lastName}/{phoneNumber}/{phoneNumberE164}/{countryIso2} | [CREDITS 1 UNIT] Feedback loop to better infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).


## Documentation For Models

 - [APIBillingPeriodUsageOut](docs/APIBillingPeriodUsageOut.md)
 - [APIClassifierOut](docs/APIClassifierOut.md)
 - [APIClassifierTaxonomyOut](docs/APIClassifierTaxonomyOut.md)
 - [APIClassifiersStatusOut](docs/APIClassifiersStatusOut.md)
 - [APICounterV2Out](docs/APICounterV2Out.md)
 - [APIKeyOut](docs/APIKeyOut.md)
 - [APIPeriodUsageOut](docs/APIPeriodUsageOut.md)
 - [APIPlanSubscriptionOut](docs/APIPlanSubscriptionOut.md)
 - [APIServiceOut](docs/APIServiceOut.md)
 - [APIServicesOut](docs/APIServicesOut.md)
 - [APIUsageAggregatedOut](docs/APIUsageAggregatedOut.md)
 - [APIUsageHistoryOut](docs/APIUsageHistoryOut.md)
 - [BatchCorridorIn](docs/BatchCorridorIn.md)
 - [BatchCorridorOut](docs/BatchCorridorOut.md)
 - [BatchFirstLastNameDiasporaedOut](docs/BatchFirstLastNameDiasporaedOut.md)
 - [BatchFirstLastNameGenderIn](docs/BatchFirstLastNameGenderIn.md)
 - [BatchFirstLastNameGenderedOut](docs/BatchFirstLastNameGenderedOut.md)
 - [BatchFirstLastNameGeoIn](docs/BatchFirstLastNameGeoIn.md)
 - [BatchFirstLastNameGeoSubclassificationOut](docs/BatchFirstLastNameGeoSubclassificationOut.md)
 - [BatchFirstLastNameGeoZippedIn](docs/BatchFirstLastNameGeoZippedIn.md)
 - [BatchFirstLastNameIn](docs/BatchFirstLastNameIn.md)
 - [BatchFirstLastNameOriginedOut](docs/BatchFirstLastNameOriginedOut.md)
 - [BatchFirstLastNamePhoneCodedOut](docs/BatchFirstLastNamePhoneCodedOut.md)
 - [BatchFirstLastNamePhoneNumberGeoIn](docs/BatchFirstLastNamePhoneNumberGeoIn.md)
 - [BatchFirstLastNamePhoneNumberIn](docs/BatchFirstLastNamePhoneNumberIn.md)
 - [BatchFirstLastNameUSRaceEthnicityOut](docs/BatchFirstLastNameUSRaceEthnicityOut.md)
 - [BatchMatchPersonalFirstLastNameIn](docs/BatchMatchPersonalFirstLastNameIn.md)
 - [BatchNameGeoIn](docs/BatchNameGeoIn.md)
 - [BatchNameIn](docs/BatchNameIn.md)
 - [BatchNameMatchCandidatesOut](docs/BatchNameMatchCandidatesOut.md)
 - [BatchNameMatchedOut](docs/BatchNameMatchedOut.md)
 - [BatchPersonalNameCastegroupOut](docs/BatchPersonalNameCastegroupOut.md)
 - [BatchPersonalNameGenderedOut](docs/BatchPersonalNameGenderedOut.md)
 - [BatchPersonalNameGeoIn](docs/BatchPersonalNameGeoIn.md)
 - [BatchPersonalNameGeoOut](docs/BatchPersonalNameGeoOut.md)
 - [BatchPersonalNameGeoSubclassificationOut](docs/BatchPersonalNameGeoSubclassificationOut.md)
 - [BatchPersonalNameGeoSubdivisionIn](docs/BatchPersonalNameGeoSubdivisionIn.md)
 - [BatchPersonalNameIn](docs/BatchPersonalNameIn.md)
 - [BatchPersonalNameParsedOut](docs/BatchPersonalNameParsedOut.md)
 - [BatchPersonalNameReligionedOut](docs/BatchPersonalNameReligionedOut.md)
 - [BatchPersonalNameSubdivisionIn](docs/BatchPersonalNameSubdivisionIn.md)
 - [BatchProperNounCategorizedOut](docs/BatchProperNounCategorizedOut.md)
 - [CorridorIn](docs/CorridorIn.md)
 - [CorridorOut](docs/CorridorOut.md)
 - [FactIn](docs/FactIn.md)
 - [FeedbackLoopOut](docs/FeedbackLoopOut.md)
 - [FirstLastNameDiasporaedOut](docs/FirstLastNameDiasporaedOut.md)
 - [FirstLastNameGenderIn](docs/FirstLastNameGenderIn.md)
 - [FirstLastNameGenderedOut](docs/FirstLastNameGenderedOut.md)
 - [FirstLastNameGeoIn](docs/FirstLastNameGeoIn.md)
 - [FirstLastNameGeoSubclassificationOut](docs/FirstLastNameGeoSubclassificationOut.md)
 - [FirstLastNameGeoZippedIn](docs/FirstLastNameGeoZippedIn.md)
 - [FirstLastNameIn](docs/FirstLastNameIn.md)
 - [FirstLastNameOriginedOut](docs/FirstLastNameOriginedOut.md)
 - [FirstLastNameOut](docs/FirstLastNameOut.md)
 - [FirstLastNamePhoneCodedOut](docs/FirstLastNamePhoneCodedOut.md)
 - [FirstLastNamePhoneNumberGeoIn](docs/FirstLastNamePhoneNumberGeoIn.md)
 - [FirstLastNamePhoneNumberIn](docs/FirstLastNamePhoneNumberIn.md)
 - [FirstLastNameUSRaceEthnicityOut](docs/FirstLastNameUSRaceEthnicityOut.md)
 - [MatchPersonalFirstLastNameIn](docs/MatchPersonalFirstLastNameIn.md)
 - [NameGeoIn](docs/NameGeoIn.md)
 - [NameIn](docs/NameIn.md)
 - [NameMatchCandidateOut](docs/NameMatchCandidateOut.md)
 - [NameMatchCandidatesOut](docs/NameMatchCandidatesOut.md)
 - [NameMatchedOut](docs/NameMatchedOut.md)
 - [PersonalNameCastegroupOut](docs/PersonalNameCastegroupOut.md)
 - [PersonalNameGenderedOut](docs/PersonalNameGenderedOut.md)
 - [PersonalNameGeoIn](docs/PersonalNameGeoIn.md)
 - [PersonalNameGeoOut](docs/PersonalNameGeoOut.md)
 - [PersonalNameGeoSubclassificationOut](docs/PersonalNameGeoSubclassificationOut.md)
 - [PersonalNameGeoSubdivisionIn](docs/PersonalNameGeoSubdivisionIn.md)
 - [PersonalNameIn](docs/PersonalNameIn.md)
 - [PersonalNameParsedOut](docs/PersonalNameParsedOut.md)
 - [PersonalNameReligionedOut](docs/PersonalNameReligionedOut.md)
 - [PersonalNameSubdivisionIn](docs/PersonalNameSubdivisionIn.md)
 - [ProperNounCategorizedOut](docs/ProperNounCategorizedOut.md)
 - [RegionISO](docs/RegionISO.md)
 - [RegionOut](docs/RegionOut.md)
 - [ReligionStatOut](docs/ReligionStatOut.md)
 - [SoftwareVersionOut](docs/SoftwareVersionOut.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author

contact@namsor.com


