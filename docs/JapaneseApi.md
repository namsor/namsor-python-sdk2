# openapi_client.JapaneseApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gender_japanese_name_full**](JapaneseApi.md#gender_japanese_name_full) | **GET** /api2/json/genderJapaneseNameFull/{japaneseName} | Infer the likely gender of a Japanese full name ex. 王晓明
[**gender_japanese_name_full_batch**](JapaneseApi.md#gender_japanese_name_full_batch) | **POST** /api2/json/genderJapaneseNameFullBatch | Infer the likely gender of up to 100 full names
[**gender_japanese_name_pinyin**](JapaneseApi.md#gender_japanese_name_pinyin) | **GET** /api2/json/genderJapaneseName/{japaneseSurname}/{japaneseGivenName} | Infer the likely gender of a Japanese name in LATIN (Pinyin).
[**gender_japanese_name_pinyin_batch**](JapaneseApi.md#gender_japanese_name_pinyin_batch) | **POST** /api2/json/genderJapaneseNameBatch | Infer the likely gender of up to 100 Japanese names in LATIN (Pinyin).
[**japanese_name_gender_kanji_candidates_batch**](JapaneseApi.md#japanese_name_gender_kanji_candidates_batch) | **POST** /api2/json/japaneseNameGenderKanjiCandidatesBatch | Identify japanese name candidates in KANJI, based on the romanized name (firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname) with KNOWN gender, ex. Yamamoto Sanae
[**japanese_name_kanji_candidates**](JapaneseApi.md#japanese_name_kanji_candidates) | **GET** /api2/json/japaneseNameKanjiCandidates/{japaneseSurnameLatin}/{japaneseGivenNameLatin} | Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae
[**japanese_name_kanji_candidates1**](JapaneseApi.md#japanese_name_kanji_candidates1) | **GET** /api2/json/japaneseNameKanjiCandidates/{japaneseSurnameLatin}/{japaneseGivenNameLatin}/{knownGender} | Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae - and a known gender.
[**japanese_name_kanji_candidates_batch**](JapaneseApi.md#japanese_name_kanji_candidates_batch) | **POST** /api2/json/japaneseNameKanjiCandidatesBatch | Identify japanese name candidates in KANJI, based on the romanized name (firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname), ex. Yamamoto Sanae
[**japanese_name_latin_candidates**](JapaneseApi.md#japanese_name_latin_candidates) | **GET** /api2/json/japaneseNameLatinCandidates/{japaneseSurnameKanji}/{japaneseGivenNameKanji} | Romanize japanese name, based on the name in Kanji.
[**japanese_name_latin_candidates_batch**](JapaneseApi.md#japanese_name_latin_candidates_batch) | **POST** /api2/json/japaneseNameLatinCandidatesBatch | Romanize japanese names, based on the name in KANJI
[**japanese_name_match**](JapaneseApi.md#japanese_name_match) | **GET** /api2/json/japaneseNameMatch/{japaneseSurnameLatin}/{japaneseGivenNameLatin}/{japaneseName} | Return a score for matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae
[**japanese_name_match_batch**](JapaneseApi.md#japanese_name_match_batch) | **POST** /api2/json/japaneseNameMatchBatch | Return a score for matching a list of Japanese names in KANJI ex. 山本 早苗 with romanized names ex. Yamamoto Sanae
[**japanese_name_match_feedback_loop**](JapaneseApi.md#japanese_name_match_feedback_loop) | **GET** /api2/json/japaneseNameMatchFeedbackLoop/{japaneseSurnameLatin}/{japaneseGivenNameLatin}/{japaneseName} | [CREDITS 1 UNIT] Feedback loop to better perform matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae
[**parse_japanese_name**](JapaneseApi.md#parse_japanese_name) | **GET** /api2/json/parseJapaneseName/{japaneseName} | Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae
[**parse_japanese_name_batch**](JapaneseApi.md#parse_japanese_name_batch) | **POST** /api2/json/parseJapaneseNameBatch | Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae 


# **gender_japanese_name_full**
> PersonalNameGenderedOut gender_japanese_name_full(japanese_name)

Infer the likely gender of a Japanese full name ex. 王晓明

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
japanese_name = 'japanese_name_example' # str | 

try:
    # Infer the likely gender of a Japanese full name ex. 王晓明
    api_response = api_instance.gender_japanese_name_full(japanese_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->gender_japanese_name_full: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **japanese_name** | **str**|  | 

### Return type

[**PersonalNameGenderedOut**](PersonalNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_japanese_name_full_batch**
> BatchPersonalNameGenderedOut gender_japanese_name_full_batch(batch_personal_name_in=batch_personal_name_in)

Infer the likely gender of up to 100 full names

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
batch_personal_name_in = openapi_client.BatchPersonalNameIn() # BatchPersonalNameIn | A list of personal names (optional)

try:
    # Infer the likely gender of up to 100 full names
    api_response = api_instance.gender_japanese_name_full_batch(batch_personal_name_in=batch_personal_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->gender_japanese_name_full_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_personal_name_in** | [**BatchPersonalNameIn**](BatchPersonalNameIn.md)| A list of personal names | [optional] 

### Return type

[**BatchPersonalNameGenderedOut**](BatchPersonalNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_japanese_name_pinyin**
> FirstLastNameGenderedOut gender_japanese_name_pinyin(japanese_surname, japanese_given_name)

Infer the likely gender of a Japanese name in LATIN (Pinyin).

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
japanese_surname = 'japanese_surname_example' # str | 
japanese_given_name = 'japanese_given_name_example' # str | 

try:
    # Infer the likely gender of a Japanese name in LATIN (Pinyin).
    api_response = api_instance.gender_japanese_name_pinyin(japanese_surname, japanese_given_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->gender_japanese_name_pinyin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **japanese_surname** | **str**|  | 
 **japanese_given_name** | **str**|  | 

### Return type

[**FirstLastNameGenderedOut**](FirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_japanese_name_pinyin_batch**
> BatchFirstLastNameGenderedOut gender_japanese_name_pinyin_batch(batch_first_last_name_in=batch_first_last_name_in)

Infer the likely gender of up to 100 Japanese names in LATIN (Pinyin).

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
batch_first_last_name_in = openapi_client.BatchFirstLastNameIn() # BatchFirstLastNameIn | A list of names, with country code. (optional)

try:
    # Infer the likely gender of up to 100 Japanese names in LATIN (Pinyin).
    api_response = api_instance.gender_japanese_name_pinyin_batch(batch_first_last_name_in=batch_first_last_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->gender_japanese_name_pinyin_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_first_last_name_in** | [**BatchFirstLastNameIn**](BatchFirstLastNameIn.md)| A list of names, with country code. | [optional] 

### Return type

[**BatchFirstLastNameGenderedOut**](BatchFirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **japanese_name_gender_kanji_candidates_batch**
> BatchNameMatchCandidatesOut japanese_name_gender_kanji_candidates_batch(batch_first_last_name_gender_in=batch_first_last_name_gender_in)

Identify japanese name candidates in KANJI, based on the romanized name (firstName = japaneseGivenName; lastName=japaneseSurname) with KNOWN gender, ex. Yamamoto Sanae

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
batch_first_last_name_gender_in = openapi_client.BatchFirstLastNameGenderIn() # BatchFirstLastNameGenderIn | A list of personal japanese names in LATIN, firstName = japaneseGivenName; lastName=japaneseSurname and known gender (optional)

try:
    # Identify japanese name candidates in KANJI, based on the romanized name (firstName = japaneseGivenName; lastName=japaneseSurname) with KNOWN gender, ex. Yamamoto Sanae
    api_response = api_instance.japanese_name_gender_kanji_candidates_batch(batch_first_last_name_gender_in=batch_first_last_name_gender_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->japanese_name_gender_kanji_candidates_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_first_last_name_gender_in** | [**BatchFirstLastNameGenderIn**](BatchFirstLastNameGenderIn.md)| A list of personal japanese names in LATIN, firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname and known gender | [optional] 

### Return type

[**BatchNameMatchCandidatesOut**](BatchNameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **japanese_name_kanji_candidates**
> NameMatchCandidatesOut japanese_name_kanji_candidates(japanese_surname_latin, japanese_given_name_latin)

Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
japanese_surname_latin = 'japanese_surname_latin_example' # str | 
japanese_given_name_latin = 'japanese_given_name_latin_example' # str | 

try:
    # Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae
    api_response = api_instance.japanese_name_kanji_candidates(japanese_surname_latin, japanese_given_name_latin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->japanese_name_kanji_candidates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **japanese_surname_latin** | **str**|  | 
 **japanese_given_name_latin** | **str**|  | 

### Return type

[**NameMatchCandidatesOut**](NameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **japanese_name_kanji_candidates1**
> NameMatchCandidatesOut japanese_name_kanji_candidates1(japanese_surname_latin, japanese_given_name_latin, known_gender)

Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae - and a known gender.

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
japanese_surname_latin = 'japanese_surname_latin_example' # str | 
japanese_given_name_latin = 'japanese_given_name_latin_example' # str | 
known_gender = 'known_gender_example' # str | 

try:
    # Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae - and a known gender.
    api_response = api_instance.japanese_name_kanji_candidates1(japanese_surname_latin, japanese_given_name_latin, known_gender)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->japanese_name_kanji_candidates1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **japanese_surname_latin** | **str**|  | 
 **japanese_given_name_latin** | **str**|  | 
 **known_gender** | **str**|  | 

### Return type

[**NameMatchCandidatesOut**](NameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **japanese_name_kanji_candidates_batch**
> BatchNameMatchCandidatesOut japanese_name_kanji_candidates_batch(batch_first_last_name_in=batch_first_last_name_in)

Identify japanese name candidates in KANJI, based on the romanized name (firstName = japaneseGivenName; lastName=japaneseSurname), ex. Yamamoto Sanae

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
batch_first_last_name_in = openapi_client.BatchFirstLastNameIn() # BatchFirstLastNameIn | A list of personal japanese names in LATIN, firstName = japaneseGivenName; lastName=japaneseSurname (optional)

try:
    # Identify japanese name candidates in KANJI, based on the romanized name (firstName = japaneseGivenName; lastName=japaneseSurname), ex. Yamamoto Sanae
    api_response = api_instance.japanese_name_kanji_candidates_batch(batch_first_last_name_in=batch_first_last_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->japanese_name_kanji_candidates_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_first_last_name_in** | [**BatchFirstLastNameIn**](BatchFirstLastNameIn.md)| A list of personal japanese names in LATIN, firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname | [optional] 

### Return type

[**BatchNameMatchCandidatesOut**](BatchNameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **japanese_name_latin_candidates**
> NameMatchCandidatesOut japanese_name_latin_candidates(japanese_surname_kanji, japanese_given_name_kanji)

Romanize japanese name, based on the name in Kanji.

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
japanese_surname_kanji = 'japanese_surname_kanji_example' # str | 
japanese_given_name_kanji = 'japanese_given_name_kanji_example' # str | 

try:
    # Romanize japanese name, based on the name in Kanji.
    api_response = api_instance.japanese_name_latin_candidates(japanese_surname_kanji, japanese_given_name_kanji)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->japanese_name_latin_candidates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **japanese_surname_kanji** | **str**|  | 
 **japanese_given_name_kanji** | **str**|  | 

### Return type

[**NameMatchCandidatesOut**](NameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **japanese_name_latin_candidates_batch**
> BatchNameMatchCandidatesOut japanese_name_latin_candidates_batch(batch_first_last_name_in=batch_first_last_name_in)

Romanize japanese names, based on the name in KANJI

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
batch_first_last_name_in = openapi_client.BatchFirstLastNameIn() # BatchFirstLastNameIn | A list of personal japanese names in KANJI, firstName = japaneseGivenName; lastName=japaneseSurname (optional)

try:
    # Romanize japanese names, based on the name in KANJI
    api_response = api_instance.japanese_name_latin_candidates_batch(batch_first_last_name_in=batch_first_last_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->japanese_name_latin_candidates_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_first_last_name_in** | [**BatchFirstLastNameIn**](BatchFirstLastNameIn.md)| A list of personal japanese names in KANJI, firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname | [optional] 

### Return type

[**BatchNameMatchCandidatesOut**](BatchNameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **japanese_name_match**
> NameMatchedOut japanese_name_match(japanese_surname_latin, japanese_given_name_latin, japanese_name)

Return a score for matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
japanese_surname_latin = 'japanese_surname_latin_example' # str | 
japanese_given_name_latin = 'japanese_given_name_latin_example' # str | 
japanese_name = 'japanese_name_example' # str | 

try:
    # Return a score for matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae
    api_response = api_instance.japanese_name_match(japanese_surname_latin, japanese_given_name_latin, japanese_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->japanese_name_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **japanese_surname_latin** | **str**|  | 
 **japanese_given_name_latin** | **str**|  | 
 **japanese_name** | **str**|  | 

### Return type

[**NameMatchedOut**](NameMatchedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **japanese_name_match_batch**
> BatchNameMatchedOut japanese_name_match_batch(batch_match_personal_first_last_name_in=batch_match_personal_first_last_name_in)

Return a score for matching a list of Japanese names in KANJI ex. 山本 早苗 with romanized names ex. Yamamoto Sanae

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
batch_match_personal_first_last_name_in = openapi_client.BatchMatchPersonalFirstLastNameIn() # BatchMatchPersonalFirstLastNameIn | A list of personal Japanese names in LATIN, firstName = japaneseGivenName; lastName=japaneseSurname (optional)

try:
    # Return a score for matching a list of Japanese names in KANJI ex. 山本 早苗 with romanized names ex. Yamamoto Sanae
    api_response = api_instance.japanese_name_match_batch(batch_match_personal_first_last_name_in=batch_match_personal_first_last_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->japanese_name_match_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_match_personal_first_last_name_in** | [**BatchMatchPersonalFirstLastNameIn**](BatchMatchPersonalFirstLastNameIn.md)| A list of personal Japanese names in LATIN, firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname | [optional] 

### Return type

[**BatchNameMatchedOut**](BatchNameMatchedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **japanese_name_match_feedback_loop**
> FeedbackLoopOut japanese_name_match_feedback_loop(japanese_surname_latin, japanese_given_name_latin, japanese_name)

[CREDITS 1 UNIT] Feedback loop to better perform matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
japanese_surname_latin = 'japanese_surname_latin_example' # str | 
japanese_given_name_latin = 'japanese_given_name_latin_example' # str | 
japanese_name = 'japanese_name_example' # str | 

try:
    # [CREDITS 1 UNIT] Feedback loop to better perform matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae
    api_response = api_instance.japanese_name_match_feedback_loop(japanese_surname_latin, japanese_given_name_latin, japanese_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->japanese_name_match_feedback_loop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **japanese_surname_latin** | **str**|  | 
 **japanese_given_name_latin** | **str**|  | 
 **japanese_name** | **str**|  | 

### Return type

[**FeedbackLoopOut**](FeedbackLoopOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_japanese_name**
> PersonalNameParsedOut parse_japanese_name(japanese_name)

Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
japanese_name = 'japanese_name_example' # str | 

try:
    # Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae
    api_response = api_instance.parse_japanese_name(japanese_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->parse_japanese_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **japanese_name** | **str**|  | 

### Return type

[**PersonalNameParsedOut**](PersonalNameParsedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_japanese_name_batch**
> BatchPersonalNameParsedOut parse_japanese_name_batch(batch_personal_name_in=batch_personal_name_in)

Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae 

### Example

* Api Key Authentication (api_key): 
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
api_instance = openapi_client.JapaneseApi(openapi_client.ApiClient(configuration))
batch_personal_name_in = openapi_client.BatchPersonalNameIn() # BatchPersonalNameIn | A list of personal names (optional)

try:
    # Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae 
    api_response = api_instance.parse_japanese_name_batch(batch_personal_name_in=batch_personal_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JapaneseApi->parse_japanese_name_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_personal_name_in** | [**BatchPersonalNameIn**](BatchPersonalNameIn.md)| A list of personal names | [optional] 

### Return type

[**BatchPersonalNameParsedOut**](BatchPersonalNameParsedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

