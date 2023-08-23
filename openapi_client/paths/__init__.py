# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API2_JSON_NAME_TYPE_PROPER_NOUN = "/api2/json/nameType/{properNoun}"
    API2_JSON_ORIGIN_FIRST_NAME_LAST_NAME = "/api2/json/origin/{firstName}/{lastName}"
    API2_JSON_REGIONS = "/api2/json/regions"
    API2_JSON_COUNTRY_PERSONAL_NAME_FULL = "/api2/json/country/{personalNameFull}"
    API2_JSON_DISABLE_SOURCE_DISABLED = "/api2/json/disable/{source}/{disabled}"
    API2_JSON_SOFTWARE_VERSION = "/api2/json/softwareVersion"
    API2_JSON_API_STATUS = "/api2/json/apiStatus"
    API2_JSON_API_SERVICES = "/api2/json/apiServices"
    API2_JSON_TAXONOMY_CLASSES_CLASSIFIER_NAME = "/api2/json/taxonomyClasses/{classifierName}"
    API2_JSON_API_USAGE = "/api2/json/apiUsage"
    API2_JSON_API_USAGE_HISTORY = "/api2/json/apiUsageHistory"
    API2_JSON_API_USAGE_HISTORY_AGGREGATE = "/api2/json/apiUsageHistoryAggregate"
    API2_JSON_LEARNABLE_SOURCE_LEARNABLE_TOKEN = "/api2/json/learnable/{source}/{learnable}/{token}"
    API2_JSON_LEARNABLE_SOURCE_LEARNABLE = "/api2/json/learnable/{source}/{learnable}"
    API2_JSON_API_KEY_INFO = "/api2/json/apiKeyInfo"
    API2_JSON_ANONYMIZE_SOURCE_ANONYMIZED_TOKEN = "/api2/json/anonymize/{source}/{anonymized}/{token}"
    API2_JSON_ANONYMIZE_SOURCE_ANONYMIZED = "/api2/json/anonymize/{source}/{anonymized}"
    API2_JSON_NAME_TYPE_GEO_PROPER_NOUN_COUNTRY_ISO2 = "/api2/json/nameTypeGeo/{properNoun}/{countryIso2}"
    API2_JSON_NAME_TYPE_BATCH = "/api2/json/nameTypeBatch"
    API2_JSON_NAME_TYPE_GEO_BATCH = "/api2/json/nameTypeGeoBatch"
    API2_JSON_CORRIDOR_COUNTRY_ISO2FROM_FIRST_NAME_FROM_LAST_NAME_FROM_COUNTRY_ISO2TO_FIRST_NAME_TO_LAST_NAME_TO = "/api2/json/corridor/{countryIso2From}/{firstNameFrom}/{lastNameFrom}/{countryIso2To}/{firstNameTo}/{lastNameTo}"
    API2_JSON_CORRIDOR_BATCH = "/api2/json/corridorBatch"
    API2_JSON_GENDER_FIRST_NAME = "/api2/json/gender/{firstName}"
    API2_JSON_GENDER_FIRST_NAME_LAST_NAME = "/api2/json/gender/{firstName}/{lastName}"
    API2_JSON_GENDER_GEO_FIRST_NAME_LAST_NAME_COUNTRY_ISO2 = "/api2/json/genderGeo/{firstName}/{lastName}/{countryIso2}"
    API2_JSON_GENDER_GEO_BATCH = "/api2/json/genderGeoBatch"
    API2_JSON_GENDER_BATCH = "/api2/json/genderBatch"
    API2_JSON_GENDER_FULL_GEO_FULL_NAME_COUNTRY_ISO2 = "/api2/json/genderFullGeo/{fullName}/{countryIso2}"
    API2_JSON_GENDER_FULL_FULL_NAME = "/api2/json/genderFull/{fullName}"
    API2_JSON_GENDER_FULL_BATCH = "/api2/json/genderFullBatch"
    API2_JSON_GENDER_FULL_GEO_BATCH = "/api2/json/genderFullGeoBatch"
    API2_JSON_ORIGIN_BATCH = "/api2/json/originBatch"
    API2_JSON_SUBCLASSIFICATION_INDIAN_FIRST_NAME_LAST_NAME = "/api2/json/subclassificationIndian/{firstName}/{lastName}"
    API2_JSON_SUBCLASSIFICATION_INDIAN_FULL_FULL_NAME = "/api2/json/subclassificationIndianFull/{fullName}"
    API2_JSON_SUBCLASSIFICATION_COUNTRY_ISO2_FIRST_NAME_LAST_NAME = "/api2/json/subclassification/{countryIso2}/{firstName}/{lastName}"
    API2_JSON_SUBCLASSIFICATION_FULL_COUNTRY_ISO2_FULL_NAME = "/api2/json/subclassificationFull/{countryIso2}/{fullName}"
    API2_JSON_SUBCLASSIFICATION_BATCH = "/api2/json/subclassificationBatch"
    API2_JSON_SUBCLASSIFICATION_FULL_BATCH = "/api2/json/subclassificationFullBatch"
    API2_JSON_SUBCLASSIFICATION_INDIAN_BATCH = "/api2/json/subclassificationIndianBatch"
    API2_JSON_SUBCLASSIFICATION_INDIAN_FULL_BATCH = "/api2/json/subclassificationIndianFullBatch"
    API2_JSON_RELIGION_INDIAN_FULL_SUB_DIVISION_ISO31662_PERSONAL_NAME_FULL = "/api2/json/religionIndianFull/{subDivisionIso31662}/{personalNameFull}"
    API2_JSON_RELIGION_INDIAN_SUB_DIVISION_ISO31662_FIRST_NAME_LAST_NAME = "/api2/json/religionIndian/{subDivisionIso31662}/{firstName}/{lastName}"
    API2_JSON_RELIGION_COUNTRY_ISO2_SUB_DIVISION_ISO31662_FIRST_NAME_LAST_NAME = "/api2/json/religion/{countryIso2}/{subDivisionIso31662}/{firstName}/{lastName}"
    API2_JSON_RELIGION_FULL_COUNTRY_ISO2_SUB_DIVISION_ISO31662_PERSONAL_NAME_FULL = "/api2/json/religionFull/{countryIso2}/{subDivisionIso31662}/{personalNameFull}"
    API2_JSON_RELIGION_FULL_BATCH = "/api2/json/religionFullBatch"
    API2_JSON_RELIGION_INDIAN_FULL_BATCH = "/api2/json/religionIndianFullBatch"
    API2_JSON_RELIGION_BATCH = "/api2/json/religionBatch"
    API2_JSON_RELIGION_INDIAN_BATCH = "/api2/json/religionIndianBatch"
    API2_JSON_CASTEGROUP_INDIAN_FULL_SUB_DIVISION_ISO31662_PERSONAL_NAME_FULL = "/api2/json/castegroupIndianFull/{subDivisionIso31662}/{personalNameFull}"
    API2_JSON_CASTEGROUP_INDIAN_FULL_BATCH = "/api2/json/castegroupIndianFullBatch"
    API2_JSON_CASTEGROUP_INDIAN_SUB_DIVISION_ISO31662_FIRST_NAME_LAST_NAME = "/api2/json/castegroupIndian/{subDivisionIso31662}/{firstName}/{lastName}"
    API2_JSON_CASTEGROUP_INDIAN_BATCH = "/api2/json/castegroupIndianBatch"
    API2_JSON_CASTE_INDIAN_SUB_DIVISION_ISO31662_FIRST_NAME_LAST_NAME = "/api2/json/casteIndian/{subDivisionIso31662}/{firstName}/{lastName}"
    API2_JSON_CASTE_INDIAN_BATCH = "/api2/json/casteIndianBatch"
    API2_JSON_COUNTRY_BATCH = "/api2/json/countryBatch"
    API2_JSON_US_RACE_ETHNICITY_FIRST_NAME_LAST_NAME = "/api2/json/usRaceEthnicity/{firstName}/{lastName}"
    API2_JSON_US_RACE_ETHNICITY_ZIP5_FIRST_NAME_LAST_NAME_ZIP5CODE = "/api2/json/usRaceEthnicityZIP5/{firstName}/{lastName}/{zip5Code}"
    API2_JSON_US_RACE_ETHNICITY_BATCH = "/api2/json/usRaceEthnicityBatch"
    API2_JSON_US_ZIP_RACE_ETHNICITY_BATCH = "/api2/json/usZipRaceEthnicityBatch"
    API2_JSON_DIASPORA_COUNTRY_ISO2_FIRST_NAME_LAST_NAME = "/api2/json/diaspora/{countryIso2}/{firstName}/{lastName}"
    API2_JSON_DIASPORA_BATCH = "/api2/json/diasporaBatch"
    API2_JSON_PARSE_NAME_NAME_FULL_COUNTRY_ISO2 = "/api2/json/parseName/{nameFull}/{countryIso2}"
    API2_JSON_PARSE_NAME_BATCH = "/api2/json/parseNameBatch"
    API2_JSON_PARSE_NAME_GEO_BATCH = "/api2/json/parseNameGeoBatch"
    API2_JSON_PARSE_CHINESE_NAME_CHINESE_NAME = "/api2/json/parseChineseName/{chineseName}"
    API2_JSON_PARSE_CHINESE_NAME_BATCH = "/api2/json/parseChineseNameBatch"
    API2_JSON_PINYIN_CHINESE_NAME_CHINESE_NAME = "/api2/json/pinyinChineseName/{chineseName}"
    API2_JSON_PINYIN_CHINESE_NAME_BATCH = "/api2/json/pinyinChineseNameBatch"
    API2_JSON_CHINESE_NAME_MATCH_CHINESE_SURNAME_LATIN_CHINESE_GIVEN_NAME_LATIN_CHINESE_NAME = "/api2/json/chineseNameMatch/{chineseSurnameLatin}/{chineseGivenNameLatin}/{chineseName}"
    API2_JSON_CHINESE_NAME_MATCH_BATCH = "/api2/json/chineseNameMatchBatch"
    API2_JSON_GENDER_CHINESE_NAME_PINYIN_CHINESE_SURNAME_LATIN_CHINESE_GIVEN_NAME_LATIN = "/api2/json/genderChineseNamePinyin/{chineseSurnameLatin}/{chineseGivenNameLatin}"
    API2_JSON_GENDER_CHINESE_NAME_PINYIN_BATCH = "/api2/json/genderChineseNamePinyinBatch"
    API2_JSON_GENDER_CHINESE_NAME_CHINESE_NAME = "/api2/json/genderChineseName/{chineseName}"
    API2_JSON_GENDER_CHINESE_NAME_BATCH = "/api2/json/genderChineseNameBatch"
    API2_JSON_CHINESE_NAME_CANDIDATES_CHINESE_SURNAME_LATIN_CHINESE_GIVEN_NAME_LATIN = "/api2/json/chineseNameCandidates/{chineseSurnameLatin}/{chineseGivenNameLatin}"
    API2_JSON_CHINESE_NAME_CANDIDATES_BATCH = "/api2/json/chineseNameCandidatesBatch"
    API2_JSON_CHINESE_NAME_GENDER_CANDIDATES_CHINESE_SURNAME_LATIN_CHINESE_GIVEN_NAME_LATIN_KNOWN_GENDER = "/api2/json/chineseNameGenderCandidates/{chineseSurnameLatin}/{chineseGivenNameLatin}/{knownGender}"
    API2_JSON_CHINESE_NAME_CANDIDATES_GENDER_BATCH = "/api2/json/chineseNameCandidatesGenderBatch"
    API2_JSON_PARSE_JAPANESE_NAME_JAPANESE_NAME = "/api2/json/parseJapaneseName/{japaneseName}"
    API2_JSON_PARSE_JAPANESE_NAME_BATCH = "/api2/json/parseJapaneseNameBatch"
    API2_JSON_JAPANESE_NAME_KANJI_CANDIDATES_JAPANESE_SURNAME_LATIN_JAPANESE_GIVEN_NAME_LATIN = "/api2/json/japaneseNameKanjiCandidates/{japaneseSurnameLatin}/{japaneseGivenNameLatin}"
    API2_JSON_JAPANESE_NAME_KANJI_CANDIDATES_JAPANESE_SURNAME_LATIN_JAPANESE_GIVEN_NAME_LATIN_KNOWN_GENDER = "/api2/json/japaneseNameKanjiCandidates/{japaneseSurnameLatin}/{japaneseGivenNameLatin}/{knownGender}"
    API2_JSON_JAPANESE_NAME_LATIN_CANDIDATES_JAPANESE_SURNAME_KANJI_JAPANESE_GIVEN_NAME_KANJI = "/api2/json/japaneseNameLatinCandidates/{japaneseSurnameKanji}/{japaneseGivenNameKanji}"
    API2_JSON_JAPANESE_NAME_KANJI_CANDIDATES_BATCH = "/api2/json/japaneseNameKanjiCandidatesBatch"
    API2_JSON_JAPANESE_NAME_GENDER_KANJI_CANDIDATES_BATCH = "/api2/json/japaneseNameGenderKanjiCandidatesBatch"
    API2_JSON_JAPANESE_NAME_LATIN_CANDIDATES_BATCH = "/api2/json/japaneseNameLatinCandidatesBatch"
    API2_JSON_JAPANESE_NAME_MATCH_JAPANESE_SURNAME_LATIN_JAPANESE_GIVEN_NAME_LATIN_JAPANESE_NAME = "/api2/json/japaneseNameMatch/{japaneseSurnameLatin}/{japaneseGivenNameLatin}/{japaneseName}"
    API2_JSON_JAPANESE_NAME_MATCH_FEEDBACK_LOOP_JAPANESE_SURNAME_LATIN_JAPANESE_GIVEN_NAME_LATIN_JAPANESE_NAME = "/api2/json/japaneseNameMatchFeedbackLoop/{japaneseSurnameLatin}/{japaneseGivenNameLatin}/{japaneseName}"
    API2_JSON_JAPANESE_NAME_MATCH_BATCH = "/api2/json/japaneseNameMatchBatch"
    API2_JSON_GENDER_JAPANESE_NAME_JAPANESE_SURNAME_JAPANESE_GIVEN_NAME = "/api2/json/genderJapaneseName/{japaneseSurname}/{japaneseGivenName}"
    API2_JSON_GENDER_JAPANESE_NAME_BATCH = "/api2/json/genderJapaneseNameBatch"
    API2_JSON_GENDER_JAPANESE_NAME_FULL_JAPANESE_NAME = "/api2/json/genderJapaneseNameFull/{japaneseName}"
    API2_JSON_GENDER_JAPANESE_NAME_FULL_BATCH = "/api2/json/genderJapaneseNameFullBatch"
    API2_JSON_PHONE_CODE_FIRST_NAME_LAST_NAME_PHONE_NUMBER = "/api2/json/phoneCode/{firstName}/{lastName}/{phoneNumber}"
    API2_JSON_PHONE_CODE_GEO_FIRST_NAME_LAST_NAME_PHONE_NUMBER_COUNTRY_ISO2 = "/api2/json/phoneCodeGeo/{firstName}/{lastName}/{phoneNumber}/{countryIso2}"
    API2_JSON_PHONE_CODE_GEO_FEEDBACK_LOOP_FIRST_NAME_LAST_NAME_PHONE_NUMBER_PHONE_NUMBER_E164_COUNTRY_ISO2 = "/api2/json/phoneCodeGeoFeedbackLoop/{firstName}/{lastName}/{phoneNumber}/{phoneNumberE164}/{countryIso2}"
    API2_JSON_PHONE_CODE_BATCH = "/api2/json/phoneCodeBatch"
    API2_JSON_PHONE_CODE_GEO_BATCH = "/api2/json/phoneCodeGeoBatch"
    API2_JSON_PARSE_NAME_NAME_FULL = "/api2/json/parseName/{nameFull}"