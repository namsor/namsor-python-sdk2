# openapi_client.ChineseApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chinese_name_candidates**](ChineseApi.md#chinese_name_candidates) | **GET** /api2/json/chineseNameCandidates/{chineseSurnameLatin}/{chineseGivenNameLatin} | Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming
[**chinese_name_candidates_batch**](ChineseApi.md#chinese_name_candidates_batch) | **POST** /api2/json/chineseNameCandidatesBatch | Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname), ex. Wang Xiaoming
[**chinese_name_candidates_gender_batch**](ChineseApi.md#chinese_name_candidates_gender_batch) | **POST** /api2/json/chineseNameCandidatesGenderBatch | Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname) ex. Wang Xiaoming.
[**chinese_name_gender_candidates**](ChineseApi.md#chinese_name_gender_candidates) | **GET** /api2/json/chineseNameGenderCandidates/{chineseSurnameLatin}/{chineseGivenNameLatin}/{knownGender} | Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming - having a known gender (&#39;male&#39; or &#39;female&#39;)
[**chinese_name_match**](ChineseApi.md#chinese_name_match) | **GET** /api2/json/chineseNameMatch/{chineseSurnameLatin}/{chineseGivenNameLatin}/{chineseName} | Return a score for matching Chinese name ex. 王晓明 with a romanized name ex. Wang Xiaoming
[**chinese_name_match_batch**](ChineseApi.md#chinese_name_match_batch) | **POST** /api2/json/chineseNameMatchBatch | Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname), ex. Wang Xiaoming
[**gender_chinese_name**](ChineseApi.md#gender_chinese_name) | **GET** /api2/json/genderChineseName/{chineseName} | Infer the likely gender of a Chinese full name ex. 王晓明
[**gender_chinese_name_batch**](ChineseApi.md#gender_chinese_name_batch) | **POST** /api2/json/genderChineseNameBatch | Infer the likely gender of up to 100 full names ex. 王晓明
[**gender_chinese_name_pinyin**](ChineseApi.md#gender_chinese_name_pinyin) | **GET** /api2/json/genderChineseNamePinyin/{chineseSurnameLatin}/{chineseGivenNameLatin} | Infer the likely gender of a Chinese name in LATIN (Pinyin).
[**gender_chinese_name_pinyin_batch**](ChineseApi.md#gender_chinese_name_pinyin_batch) | **POST** /api2/json/genderChineseNamePinyinBatch | Infer the likely gender of up to 100 Chinese names in LATIN (Pinyin).
[**parse_chinese_name**](ChineseApi.md#parse_chinese_name) | **GET** /api2/json/parseChineseName/{chineseName} | Infer the likely first/last name structure of a name, ex. 王晓明 -&gt; 王(surname) 晓明(given name)
[**parse_chinese_name_batch**](ChineseApi.md#parse_chinese_name_batch) | **POST** /api2/json/parseChineseNameBatch | Infer the likely first/last name structure of a name, ex. 王晓明 -&gt; 王(surname) 晓明(given name).
[**pinyin_chinese_name**](ChineseApi.md#pinyin_chinese_name) | **GET** /api2/json/pinyinChineseName/{chineseName} | Romanize the Chinese name to Pinyin, ex. 王晓明 -&gt; Wang (surname) Xiaoming (given name)
[**pinyin_chinese_name_batch**](ChineseApi.md#pinyin_chinese_name_batch) | **POST** /api2/json/pinyinChineseNameBatch | Romanize a list of Chinese name to Pinyin, ex. 王晓明 -&gt; Wang (surname) Xiaoming (given name).


# **chinese_name_candidates**
> NameMatchCandidatesOut chinese_name_candidates(chinese_surname_latin, chinese_given_name_latin)

Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
chinese_surname_latin = 'chinese_surname_latin_example' # str | 
chinese_given_name_latin = 'chinese_given_name_latin_example' # str | 

try:
    # Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming
    api_response = api_instance.chinese_name_candidates(chinese_surname_latin, chinese_given_name_latin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->chinese_name_candidates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chinese_surname_latin** | **str**|  | 
 **chinese_given_name_latin** | **str**|  | 

### Return type

[**NameMatchCandidatesOut**](NameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chinese_name_candidates_batch**
> BatchNameMatchCandidatesOut chinese_name_candidates_batch(batch_first_last_name_in=batch_first_last_name_in)

Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname), ex. Wang Xiaoming

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
batch_first_last_name_in = openapi_client.BatchFirstLastNameIn() # BatchFirstLastNameIn | A list of personal Chinese names in LATIN, firstName = chineseGivenName; lastName=chineseSurname (optional)

try:
    # Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname), ex. Wang Xiaoming
    api_response = api_instance.chinese_name_candidates_batch(batch_first_last_name_in=batch_first_last_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->chinese_name_candidates_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_first_last_name_in** | [**BatchFirstLastNameIn**](BatchFirstLastNameIn.md)| A list of personal Chinese names in LATIN, firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname | [optional] 

### Return type

[**BatchNameMatchCandidatesOut**](BatchNameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chinese_name_candidates_gender_batch**
> BatchNameMatchCandidatesOut chinese_name_candidates_gender_batch(batch_first_last_name_gender_in=batch_first_last_name_gender_in)

Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname) ex. Wang Xiaoming.

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
batch_first_last_name_gender_in = openapi_client.BatchFirstLastNameGenderIn() # BatchFirstLastNameGenderIn | A list of personal Chinese names in LATIN, firstName = chineseGivenName; lastName=chineseSurname (optional)

try:
    # Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname) ex. Wang Xiaoming.
    api_response = api_instance.chinese_name_candidates_gender_batch(batch_first_last_name_gender_in=batch_first_last_name_gender_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->chinese_name_candidates_gender_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_first_last_name_gender_in** | [**BatchFirstLastNameGenderIn**](BatchFirstLastNameGenderIn.md)| A list of personal Chinese names in LATIN, firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname | [optional] 

### Return type

[**BatchNameMatchCandidatesOut**](BatchNameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chinese_name_gender_candidates**
> NameMatchCandidatesOut chinese_name_gender_candidates(chinese_surname_latin, chinese_given_name_latin, known_gender)

Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming - having a known gender ('male' or 'female')

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
chinese_surname_latin = 'chinese_surname_latin_example' # str | 
chinese_given_name_latin = 'chinese_given_name_latin_example' # str | 
known_gender = 'known_gender_example' # str | 

try:
    # Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming - having a known gender ('male' or 'female')
    api_response = api_instance.chinese_name_gender_candidates(chinese_surname_latin, chinese_given_name_latin, known_gender)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->chinese_name_gender_candidates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chinese_surname_latin** | **str**|  | 
 **chinese_given_name_latin** | **str**|  | 
 **known_gender** | **str**|  | 

### Return type

[**NameMatchCandidatesOut**](NameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chinese_name_match**
> NameMatchedOut chinese_name_match(chinese_surname_latin, chinese_given_name_latin, chinese_name)

Return a score for matching Chinese name ex. 王晓明 with a romanized name ex. Wang Xiaoming

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
chinese_surname_latin = 'chinese_surname_latin_example' # str | 
chinese_given_name_latin = 'chinese_given_name_latin_example' # str | 
chinese_name = 'chinese_name_example' # str | 

try:
    # Return a score for matching Chinese name ex. 王晓明 with a romanized name ex. Wang Xiaoming
    api_response = api_instance.chinese_name_match(chinese_surname_latin, chinese_given_name_latin, chinese_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->chinese_name_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chinese_surname_latin** | **str**|  | 
 **chinese_given_name_latin** | **str**|  | 
 **chinese_name** | **str**|  | 

### Return type

[**NameMatchedOut**](NameMatchedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chinese_name_match_batch**
> BatchNameMatchedOut chinese_name_match_batch(batch_match_personal_first_last_name_in=batch_match_personal_first_last_name_in)

Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname), ex. Wang Xiaoming

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
batch_match_personal_first_last_name_in = openapi_client.BatchMatchPersonalFirstLastNameIn() # BatchMatchPersonalFirstLastNameIn | A list of personal Chinese names in LATIN, firstName = chineseGivenName; lastName=chineseSurname (optional)

try:
    # Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname), ex. Wang Xiaoming
    api_response = api_instance.chinese_name_match_batch(batch_match_personal_first_last_name_in=batch_match_personal_first_last_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->chinese_name_match_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_match_personal_first_last_name_in** | [**BatchMatchPersonalFirstLastNameIn**](BatchMatchPersonalFirstLastNameIn.md)| A list of personal Chinese names in LATIN, firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname | [optional] 

### Return type

[**BatchNameMatchedOut**](BatchNameMatchedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_chinese_name**
> PersonalNameGenderedOut gender_chinese_name(chinese_name)

Infer the likely gender of a Chinese full name ex. 王晓明

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
chinese_name = 'chinese_name_example' # str | 

try:
    # Infer the likely gender of a Chinese full name ex. 王晓明
    api_response = api_instance.gender_chinese_name(chinese_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->gender_chinese_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chinese_name** | **str**|  | 

### Return type

[**PersonalNameGenderedOut**](PersonalNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_chinese_name_batch**
> BatchPersonalNameGenderedOut gender_chinese_name_batch(batch_personal_name_in=batch_personal_name_in)

Infer the likely gender of up to 100 full names ex. 王晓明

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
batch_personal_name_in = openapi_client.BatchPersonalNameIn() # BatchPersonalNameIn | A list of personal names, with a country ISO2 code (optional)

try:
    # Infer the likely gender of up to 100 full names ex. 王晓明
    api_response = api_instance.gender_chinese_name_batch(batch_personal_name_in=batch_personal_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->gender_chinese_name_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_personal_name_in** | [**BatchPersonalNameIn**](BatchPersonalNameIn.md)| A list of personal names, with a country ISO2 code | [optional] 

### Return type

[**BatchPersonalNameGenderedOut**](BatchPersonalNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_chinese_name_pinyin**
> FirstLastNameGenderedOut gender_chinese_name_pinyin(chinese_surname_latin, chinese_given_name_latin)

Infer the likely gender of a Chinese name in LATIN (Pinyin).

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
chinese_surname_latin = 'chinese_surname_latin_example' # str | 
chinese_given_name_latin = 'chinese_given_name_latin_example' # str | 

try:
    # Infer the likely gender of a Chinese name in LATIN (Pinyin).
    api_response = api_instance.gender_chinese_name_pinyin(chinese_surname_latin, chinese_given_name_latin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->gender_chinese_name_pinyin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chinese_surname_latin** | **str**|  | 
 **chinese_given_name_latin** | **str**|  | 

### Return type

[**FirstLastNameGenderedOut**](FirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_chinese_name_pinyin_batch**
> BatchFirstLastNameGenderedOut gender_chinese_name_pinyin_batch(batch_first_last_name_in=batch_first_last_name_in)

Infer the likely gender of up to 100 Chinese names in LATIN (Pinyin).

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
batch_first_last_name_in = openapi_client.BatchFirstLastNameIn() # BatchFirstLastNameIn | A list of names, with country code. (optional)

try:
    # Infer the likely gender of up to 100 Chinese names in LATIN (Pinyin).
    api_response = api_instance.gender_chinese_name_pinyin_batch(batch_first_last_name_in=batch_first_last_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->gender_chinese_name_pinyin_batch: %s\n" % e)
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

# **parse_chinese_name**
> PersonalNameParsedOut parse_chinese_name(chinese_name)

Infer the likely first/last name structure of a name, ex. 王晓明 -> 王(surname) 晓明(given name)

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
chinese_name = 'chinese_name_example' # str | 

try:
    # Infer the likely first/last name structure of a name, ex. 王晓明 -> 王(surname) 晓明(given name)
    api_response = api_instance.parse_chinese_name(chinese_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->parse_chinese_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chinese_name** | **str**|  | 

### Return type

[**PersonalNameParsedOut**](PersonalNameParsedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_chinese_name_batch**
> BatchPersonalNameParsedOut parse_chinese_name_batch(batch_personal_name_in=batch_personal_name_in)

Infer the likely first/last name structure of a name, ex. 王晓明 -> 王(surname) 晓明(given name).

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
batch_personal_name_in = openapi_client.BatchPersonalNameIn() # BatchPersonalNameIn | A list of personal names (optional)

try:
    # Infer the likely first/last name structure of a name, ex. 王晓明 -> 王(surname) 晓明(given name).
    api_response = api_instance.parse_chinese_name_batch(batch_personal_name_in=batch_personal_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->parse_chinese_name_batch: %s\n" % e)
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

# **pinyin_chinese_name**
> PersonalNameParsedOut pinyin_chinese_name(chinese_name)

Romanize the Chinese name to Pinyin, ex. 王晓明 -> Wang (surname) Xiaoming (given name)

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
chinese_name = 'chinese_name_example' # str | 

try:
    # Romanize the Chinese name to Pinyin, ex. 王晓明 -> Wang (surname) Xiaoming (given name)
    api_response = api_instance.pinyin_chinese_name(chinese_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->pinyin_chinese_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chinese_name** | **str**|  | 

### Return type

[**PersonalNameParsedOut**](PersonalNameParsedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pinyin_chinese_name_batch**
> BatchPersonalNameParsedOut pinyin_chinese_name_batch(batch_personal_name_in=batch_personal_name_in)

Romanize a list of Chinese name to Pinyin, ex. 王晓明 -> Wang (surname) Xiaoming (given name).

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
api_instance = openapi_client.ChineseApi(openapi_client.ApiClient(configuration))
batch_personal_name_in = openapi_client.BatchPersonalNameIn() # BatchPersonalNameIn | A list of Chinese names (optional)

try:
    # Romanize a list of Chinese name to Pinyin, ex. 王晓明 -> Wang (surname) Xiaoming (given name).
    api_response = api_instance.pinyin_chinese_name_batch(batch_personal_name_in=batch_personal_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->pinyin_chinese_name_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_personal_name_in** | [**BatchPersonalNameIn**](BatchPersonalNameIn.md)| A list of Chinese names | [optional] 

### Return type

[**BatchPersonalNameParsedOut**](BatchPersonalNameParsedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

