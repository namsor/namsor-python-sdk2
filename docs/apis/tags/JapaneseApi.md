<a id="__pageTop"></a>
# openapi_client.apis.tags.japanese_api.JapaneseApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gender_japanese_name_full**](#gender_japanese_name_full) | **get** /api2/json/genderJapaneseNameFull/{japaneseName} | Infer the likely gender of a Japanese full name ex. 王晓明
[**gender_japanese_name_full_batch**](#gender_japanese_name_full_batch) | **post** /api2/json/genderJapaneseNameFullBatch | Infer the likely gender of up to 100 full names
[**gender_japanese_name_pinyin**](#gender_japanese_name_pinyin) | **get** /api2/json/genderJapaneseName/{japaneseSurname}/{japaneseGivenName} | Infer the likely gender of a Japanese name in LATIN (Pinyin).
[**gender_japanese_name_pinyin_batch**](#gender_japanese_name_pinyin_batch) | **post** /api2/json/genderJapaneseNameBatch | Infer the likely gender of up to 100 Japanese names in LATIN (Pinyin).
[**japanese_name_gender_kanji_candidates_batch**](#japanese_name_gender_kanji_candidates_batch) | **post** /api2/json/japaneseNameGenderKanjiCandidatesBatch | Identify japanese name candidates in KANJI, based on the romanized name (firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname) with KNOWN gender, ex. Yamamoto Sanae
[**japanese_name_kanji_candidates**](#japanese_name_kanji_candidates) | **get** /api2/json/japaneseNameKanjiCandidates/{japaneseSurnameLatin}/{japaneseGivenNameLatin} | Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae
[**japanese_name_kanji_candidates1**](#japanese_name_kanji_candidates1) | **get** /api2/json/japaneseNameKanjiCandidates/{japaneseSurnameLatin}/{japaneseGivenNameLatin}/{knownGender} | Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae - and a known gender.
[**japanese_name_kanji_candidates_batch**](#japanese_name_kanji_candidates_batch) | **post** /api2/json/japaneseNameKanjiCandidatesBatch | Identify japanese name candidates in KANJI, based on the romanized name (firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname), ex. Yamamoto Sanae
[**japanese_name_latin_candidates**](#japanese_name_latin_candidates) | **get** /api2/json/japaneseNameLatinCandidates/{japaneseSurnameKanji}/{japaneseGivenNameKanji} | Romanize japanese name, based on the name in Kanji.
[**japanese_name_latin_candidates_batch**](#japanese_name_latin_candidates_batch) | **post** /api2/json/japaneseNameLatinCandidatesBatch | Romanize japanese names, based on the name in KANJI
[**japanese_name_match**](#japanese_name_match) | **get** /api2/json/japaneseNameMatch/{japaneseSurnameLatin}/{japaneseGivenNameLatin}/{japaneseName} | Return a score for matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae
[**japanese_name_match_batch**](#japanese_name_match_batch) | **post** /api2/json/japaneseNameMatchBatch | Return a score for matching a list of Japanese names in KANJI ex. 山本 早苗 with romanized names ex. Yamamoto Sanae
[**japanese_name_match_feedback_loop**](#japanese_name_match_feedback_loop) | **get** /api2/json/japaneseNameMatchFeedbackLoop/{japaneseSurnameLatin}/{japaneseGivenNameLatin}/{japaneseName} | [CREDITS 1 UNIT] Feedback loop to better perform matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae
[**parse_japanese_name**](#parse_japanese_name) | **get** /api2/json/parseJapaneseName/{japaneseName} | Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae
[**parse_japanese_name_batch**](#parse_japanese_name_batch) | **post** /api2/json/parseJapaneseNameBatch | Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae 

# **gender_japanese_name_full**
<a id="gender_japanese_name_full"></a>
> PersonalNameGenderedOut gender_japanese_name_full(japanese_name)

Infer the likely gender of a Japanese full name ex. 王晓明

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.personal_name_gendered_out import PersonalNameGenderedOut
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'japaneseName': "japaneseName_example",
    }
    try:
        # Infer the likely gender of a Japanese full name ex. 王晓明
        api_response = api_instance.gender_japanese_name_full(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->gender_japanese_name_full: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
japaneseName | JapaneseNameSchema | | 

# JapaneseNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#gender_japanese_name_full.ApiResponseFor200) | A genderized name.
401 | [ApiResponseFor401](#gender_japanese_name_full.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#gender_japanese_name_full.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### gender_japanese_name_full.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PersonalNameGenderedOut**](../../models/PersonalNameGenderedOut.md) |  | 


#### gender_japanese_name_full.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### gender_japanese_name_full.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **gender_japanese_name_full_batch**
<a id="gender_japanese_name_full_batch"></a>
> BatchPersonalNameGenderedOut gender_japanese_name_full_batch()

Infer the likely gender of up to 100 full names

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.batch_personal_name_gendered_out import BatchPersonalNameGenderedOut
from openapi_client.model.batch_personal_name_in import BatchPersonalNameIn
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only optional values
    body = BatchPersonalNameIn(
        personal_names=[
            PersonalNameIn(
                id="id_example",
                name="name_example",
            )
        ],
    )
    try:
        # Infer the likely gender of up to 100 full names
        api_response = api_instance.gender_japanese_name_full_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->gender_japanese_name_full_batch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchPersonalNameIn**](../../models/BatchPersonalNameIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#gender_japanese_name_full_batch.ApiResponseFor200) | A list of genderized names.
401 | [ApiResponseFor401](#gender_japanese_name_full_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#gender_japanese_name_full_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#gender_japanese_name_full_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### gender_japanese_name_full_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchPersonalNameGenderedOut**](../../models/BatchPersonalNameGenderedOut.md) |  | 


#### gender_japanese_name_full_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### gender_japanese_name_full_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### gender_japanese_name_full_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **gender_japanese_name_pinyin**
<a id="gender_japanese_name_pinyin"></a>
> FirstLastNameGenderedOut gender_japanese_name_pinyin(japanese_surnamejapanese_given_name)

Infer the likely gender of a Japanese name in LATIN (Pinyin).

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.first_last_name_gendered_out import FirstLastNameGenderedOut
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'japaneseSurname': "japaneseSurname_example",
        'japaneseGivenName': "japaneseGivenName_example",
    }
    try:
        # Infer the likely gender of a Japanese name in LATIN (Pinyin).
        api_response = api_instance.gender_japanese_name_pinyin(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->gender_japanese_name_pinyin: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
japaneseSurname | JapaneseSurnameSchema | | 
japaneseGivenName | JapaneseGivenNameSchema | | 

# JapaneseSurnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JapaneseGivenNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#gender_japanese_name_pinyin.ApiResponseFor200) | A genderized name.
401 | [ApiResponseFor401](#gender_japanese_name_pinyin.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#gender_japanese_name_pinyin.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### gender_japanese_name_pinyin.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FirstLastNameGenderedOut**](../../models/FirstLastNameGenderedOut.md) |  | 


#### gender_japanese_name_pinyin.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### gender_japanese_name_pinyin.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **gender_japanese_name_pinyin_batch**
<a id="gender_japanese_name_pinyin_batch"></a>
> BatchFirstLastNameGenderedOut gender_japanese_name_pinyin_batch()

Infer the likely gender of up to 100 Japanese names in LATIN (Pinyin).

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.batch_first_last_name_in import BatchFirstLastNameIn
from openapi_client.model.batch_first_last_name_gendered_out import BatchFirstLastNameGenderedOut
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only optional values
    body = BatchFirstLastNameIn(
        personal_names=[
            FirstLastNameIn(
                id="id_example",
                first_name="first_name_example",
                last_name="last_name_example",
            )
        ],
    )
    try:
        # Infer the likely gender of up to 100 Japanese names in LATIN (Pinyin).
        api_response = api_instance.gender_japanese_name_pinyin_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->gender_japanese_name_pinyin_batch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchFirstLastNameIn**](../../models/BatchFirstLastNameIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#gender_japanese_name_pinyin_batch.ApiResponseFor200) | A list of genderized names.
401 | [ApiResponseFor401](#gender_japanese_name_pinyin_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#gender_japanese_name_pinyin_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#gender_japanese_name_pinyin_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### gender_japanese_name_pinyin_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchFirstLastNameGenderedOut**](../../models/BatchFirstLastNameGenderedOut.md) |  | 


#### gender_japanese_name_pinyin_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### gender_japanese_name_pinyin_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### gender_japanese_name_pinyin_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **japanese_name_gender_kanji_candidates_batch**
<a id="japanese_name_gender_kanji_candidates_batch"></a>
> BatchNameMatchCandidatesOut japanese_name_gender_kanji_candidates_batch()

Identify japanese name candidates in KANJI, based on the romanized name (firstName = japaneseGivenName; lastName=japaneseSurname) with KNOWN gender, ex. Yamamoto Sanae

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.batch_name_match_candidates_out import BatchNameMatchCandidatesOut
from openapi_client.model.batch_first_last_name_gender_in import BatchFirstLastNameGenderIn
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only optional values
    body = BatchFirstLastNameGenderIn(
        personal_names=[
            FirstLastNameGenderIn(
                id="id_example",
                first_name="first_name_example",
                last_name="last_name_example",
                gender="gender_example",
            )
        ],
    )
    try:
        # Identify japanese name candidates in KANJI, based on the romanized name (firstName = japaneseGivenName; lastName=japaneseSurname) with KNOWN gender, ex. Yamamoto Sanae
        api_response = api_instance.japanese_name_gender_kanji_candidates_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->japanese_name_gender_kanji_candidates_batch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchFirstLastNameGenderIn**](../../models/BatchFirstLastNameGenderIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#japanese_name_gender_kanji_candidates_batch.ApiResponseFor200) | A list of genderized names.
401 | [ApiResponseFor401](#japanese_name_gender_kanji_candidates_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#japanese_name_gender_kanji_candidates_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#japanese_name_gender_kanji_candidates_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### japanese_name_gender_kanji_candidates_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchNameMatchCandidatesOut**](../../models/BatchNameMatchCandidatesOut.md) |  | 


#### japanese_name_gender_kanji_candidates_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_gender_kanji_candidates_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_gender_kanji_candidates_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **japanese_name_kanji_candidates**
<a id="japanese_name_kanji_candidates"></a>
> NameMatchCandidatesOut japanese_name_kanji_candidates(japanese_surname_latinjapanese_given_name_latin)

Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.name_match_candidates_out import NameMatchCandidatesOut
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'japaneseSurnameLatin': "japaneseSurnameLatin_example",
        'japaneseGivenNameLatin': "japaneseGivenNameLatin_example",
    }
    try:
        # Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae
        api_response = api_instance.japanese_name_kanji_candidates(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->japanese_name_kanji_candidates: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
japaneseSurnameLatin | JapaneseSurnameLatinSchema | | 
japaneseGivenNameLatin | JapaneseGivenNameLatinSchema | | 

# JapaneseSurnameLatinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JapaneseGivenNameLatinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#japanese_name_kanji_candidates.ApiResponseFor200) | A romanized name.
401 | [ApiResponseFor401](#japanese_name_kanji_candidates.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#japanese_name_kanji_candidates.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### japanese_name_kanji_candidates.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NameMatchCandidatesOut**](../../models/NameMatchCandidatesOut.md) |  | 


#### japanese_name_kanji_candidates.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_kanji_candidates.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **japanese_name_kanji_candidates1**
<a id="japanese_name_kanji_candidates1"></a>
> NameMatchCandidatesOut japanese_name_kanji_candidates1(japanese_surname_latinjapanese_given_name_latinknown_gender)

Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae - and a known gender.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.name_match_candidates_out import NameMatchCandidatesOut
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'japaneseSurnameLatin': "japaneseSurnameLatin_example",
        'japaneseGivenNameLatin': "japaneseGivenNameLatin_example",
        'knownGender': "knownGender_example",
    }
    try:
        # Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae - and a known gender.
        api_response = api_instance.japanese_name_kanji_candidates1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->japanese_name_kanji_candidates1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
japaneseSurnameLatin | JapaneseSurnameLatinSchema | | 
japaneseGivenNameLatin | JapaneseGivenNameLatinSchema | | 
knownGender | KnownGenderSchema | | 

# JapaneseSurnameLatinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JapaneseGivenNameLatinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# KnownGenderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#japanese_name_kanji_candidates1.ApiResponseFor200) | A romanized name.
401 | [ApiResponseFor401](#japanese_name_kanji_candidates1.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#japanese_name_kanji_candidates1.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### japanese_name_kanji_candidates1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NameMatchCandidatesOut**](../../models/NameMatchCandidatesOut.md) |  | 


#### japanese_name_kanji_candidates1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_kanji_candidates1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **japanese_name_kanji_candidates_batch**
<a id="japanese_name_kanji_candidates_batch"></a>
> BatchNameMatchCandidatesOut japanese_name_kanji_candidates_batch()

Identify japanese name candidates in KANJI, based on the romanized name (firstName = japaneseGivenName; lastName=japaneseSurname), ex. Yamamoto Sanae

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.batch_first_last_name_in import BatchFirstLastNameIn
from openapi_client.model.batch_name_match_candidates_out import BatchNameMatchCandidatesOut
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only optional values
    body = BatchFirstLastNameIn(
        personal_names=[
            FirstLastNameIn(
                id="id_example",
                first_name="first_name_example",
                last_name="last_name_example",
            )
        ],
    )
    try:
        # Identify japanese name candidates in KANJI, based on the romanized name (firstName = japaneseGivenName; lastName=japaneseSurname), ex. Yamamoto Sanae
        api_response = api_instance.japanese_name_kanji_candidates_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->japanese_name_kanji_candidates_batch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchFirstLastNameIn**](../../models/BatchFirstLastNameIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#japanese_name_kanji_candidates_batch.ApiResponseFor200) | A list of genderized names.
401 | [ApiResponseFor401](#japanese_name_kanji_candidates_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#japanese_name_kanji_candidates_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#japanese_name_kanji_candidates_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### japanese_name_kanji_candidates_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchNameMatchCandidatesOut**](../../models/BatchNameMatchCandidatesOut.md) |  | 


#### japanese_name_kanji_candidates_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_kanji_candidates_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_kanji_candidates_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **japanese_name_latin_candidates**
<a id="japanese_name_latin_candidates"></a>
> NameMatchCandidatesOut japanese_name_latin_candidates(japanese_surname_kanjijapanese_given_name_kanji)

Romanize japanese name, based on the name in Kanji.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.name_match_candidates_out import NameMatchCandidatesOut
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'japaneseSurnameKanji': "japaneseSurnameKanji_example",
        'japaneseGivenNameKanji': "japaneseGivenNameKanji_example",
    }
    try:
        # Romanize japanese name, based on the name in Kanji.
        api_response = api_instance.japanese_name_latin_candidates(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->japanese_name_latin_candidates: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
japaneseSurnameKanji | JapaneseSurnameKanjiSchema | | 
japaneseGivenNameKanji | JapaneseGivenNameKanjiSchema | | 

# JapaneseSurnameKanjiSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JapaneseGivenNameKanjiSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#japanese_name_latin_candidates.ApiResponseFor200) | A romanized name.
401 | [ApiResponseFor401](#japanese_name_latin_candidates.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#japanese_name_latin_candidates.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### japanese_name_latin_candidates.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NameMatchCandidatesOut**](../../models/NameMatchCandidatesOut.md) |  | 


#### japanese_name_latin_candidates.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_latin_candidates.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **japanese_name_latin_candidates_batch**
<a id="japanese_name_latin_candidates_batch"></a>
> BatchNameMatchCandidatesOut japanese_name_latin_candidates_batch()

Romanize japanese names, based on the name in KANJI

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.batch_first_last_name_in import BatchFirstLastNameIn
from openapi_client.model.batch_name_match_candidates_out import BatchNameMatchCandidatesOut
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only optional values
    body = BatchFirstLastNameIn(
        personal_names=[
            FirstLastNameIn(
                id="id_example",
                first_name="first_name_example",
                last_name="last_name_example",
            )
        ],
    )
    try:
        # Romanize japanese names, based on the name in KANJI
        api_response = api_instance.japanese_name_latin_candidates_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->japanese_name_latin_candidates_batch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchFirstLastNameIn**](../../models/BatchFirstLastNameIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#japanese_name_latin_candidates_batch.ApiResponseFor200) | A list of genderized names.
401 | [ApiResponseFor401](#japanese_name_latin_candidates_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#japanese_name_latin_candidates_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#japanese_name_latin_candidates_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### japanese_name_latin_candidates_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchNameMatchCandidatesOut**](../../models/BatchNameMatchCandidatesOut.md) |  | 


#### japanese_name_latin_candidates_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_latin_candidates_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_latin_candidates_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **japanese_name_match**
<a id="japanese_name_match"></a>
> NameMatchedOut japanese_name_match(japanese_surname_latinjapanese_given_name_latinjapanese_name)

Return a score for matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.name_matched_out import NameMatchedOut
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'japaneseSurnameLatin': "japaneseSurnameLatin_example",
        'japaneseGivenNameLatin': "japaneseGivenNameLatin_example",
        'japaneseName': "japaneseName_example",
    }
    try:
        # Return a score for matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae
        api_response = api_instance.japanese_name_match(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->japanese_name_match: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
japaneseSurnameLatin | JapaneseSurnameLatinSchema | | 
japaneseGivenNameLatin | JapaneseGivenNameLatinSchema | | 
japaneseName | JapaneseNameSchema | | 

# JapaneseSurnameLatinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JapaneseGivenNameLatinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JapaneseNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#japanese_name_match.ApiResponseFor200) | A romanized name.
401 | [ApiResponseFor401](#japanese_name_match.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#japanese_name_match.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### japanese_name_match.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NameMatchedOut**](../../models/NameMatchedOut.md) |  | 


#### japanese_name_match.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_match.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **japanese_name_match_batch**
<a id="japanese_name_match_batch"></a>
> BatchNameMatchedOut japanese_name_match_batch()

Return a score for matching a list of Japanese names in KANJI ex. 山本 早苗 with romanized names ex. Yamamoto Sanae

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.batch_match_personal_first_last_name_in import BatchMatchPersonalFirstLastNameIn
from openapi_client.model.batch_name_matched_out import BatchNameMatchedOut
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only optional values
    body = BatchMatchPersonalFirstLastNameIn(
        personal_names=[
            MatchPersonalFirstLastNameIn(
                id="id_example",
                name1=FirstLastNameIn(
                    id="id_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                ),
                name2=PersonalNameIn(
                    id="id_example",
                    name="name_example",
                ),
            )
        ],
    )
    try:
        # Return a score for matching a list of Japanese names in KANJI ex. 山本 早苗 with romanized names ex. Yamamoto Sanae
        api_response = api_instance.japanese_name_match_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->japanese_name_match_batch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchMatchPersonalFirstLastNameIn**](../../models/BatchMatchPersonalFirstLastNameIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#japanese_name_match_batch.ApiResponseFor200) | A list of matched names.
401 | [ApiResponseFor401](#japanese_name_match_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#japanese_name_match_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#japanese_name_match_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### japanese_name_match_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchNameMatchedOut**](../../models/BatchNameMatchedOut.md) |  | 


#### japanese_name_match_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_match_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_match_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **japanese_name_match_feedback_loop**
<a id="japanese_name_match_feedback_loop"></a>
> FeedbackLoopOut japanese_name_match_feedback_loop(japanese_surname_latinjapanese_given_name_latinjapanese_name)

[CREDITS 1 UNIT] Feedback loop to better perform matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.feedback_loop_out import FeedbackLoopOut
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'japaneseSurnameLatin': "japaneseSurnameLatin_example",
        'japaneseGivenNameLatin': "japaneseGivenNameLatin_example",
        'japaneseName': "japaneseName_example",
    }
    try:
        # [CREDITS 1 UNIT] Feedback loop to better perform matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae
        api_response = api_instance.japanese_name_match_feedback_loop(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->japanese_name_match_feedback_loop: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
japaneseSurnameLatin | JapaneseSurnameLatinSchema | | 
japaneseGivenNameLatin | JapaneseGivenNameLatinSchema | | 
japaneseName | JapaneseNameSchema | | 

# JapaneseSurnameLatinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JapaneseGivenNameLatinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JapaneseNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#japanese_name_match_feedback_loop.ApiResponseFor200) | A romanized name.
401 | [ApiResponseFor401](#japanese_name_match_feedback_loop.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#japanese_name_match_feedback_loop.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### japanese_name_match_feedback_loop.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FeedbackLoopOut**](../../models/FeedbackLoopOut.md) |  | 


#### japanese_name_match_feedback_loop.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### japanese_name_match_feedback_loop.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **parse_japanese_name**
<a id="parse_japanese_name"></a>
> PersonalNameParsedOut parse_japanese_name(japanese_name)

Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.personal_name_parsed_out import PersonalNameParsedOut
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'japaneseName': "japaneseName_example",
    }
    try:
        # Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae
        api_response = api_instance.parse_japanese_name(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->parse_japanese_name: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
japaneseName | JapaneseNameSchema | | 

# JapaneseNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#parse_japanese_name.ApiResponseFor200) | A origined name.
401 | [ApiResponseFor401](#parse_japanese_name.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#parse_japanese_name.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### parse_japanese_name.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PersonalNameParsedOut**](../../models/PersonalNameParsedOut.md) |  | 


#### parse_japanese_name.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### parse_japanese_name.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **parse_japanese_name_batch**
<a id="parse_japanese_name_batch"></a>
> BatchPersonalNameParsedOut parse_japanese_name_batch()

Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae 

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import japanese_api
from openapi_client.model.batch_personal_name_parsed_out import BatchPersonalNameParsedOut
from openapi_client.model.batch_personal_name_in import BatchPersonalNameIn
from pprint import pprint
# Defining the host is optional and defaults to https://v2.namsor.com/NamSorAPIv2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.namsor.com/NamSorAPIv2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = japanese_api.JapaneseApi(api_client)

    # example passing only optional values
    body = BatchPersonalNameIn(
        personal_names=[
            PersonalNameIn(
                id="id_example",
                name="name_example",
            )
        ],
    )
    try:
        # Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae 
        api_response = api_instance.parse_japanese_name_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JapaneseApi->parse_japanese_name_batch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchPersonalNameIn**](../../models/BatchPersonalNameIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#parse_japanese_name_batch.ApiResponseFor200) | A list of parsed names.
401 | [ApiResponseFor401](#parse_japanese_name_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#parse_japanese_name_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#parse_japanese_name_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### parse_japanese_name_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchPersonalNameParsedOut**](../../models/BatchPersonalNameParsedOut.md) |  | 


#### parse_japanese_name_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### parse_japanese_name_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### parse_japanese_name_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

