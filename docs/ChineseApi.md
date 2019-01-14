# openapi_client.ChineseApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chinese_name_candidates**](ChineseApi.md#chinese_name_candidates) | **GET** /api2/json/chineseNameCandidates/{chineseSurnameLatin}/{chineseGivenNameLatin} | Identify Chinese name candidates, based on the romanized name.
[**chinese_name_candidates_batch**](ChineseApi.md#chinese_name_candidates_batch) | **POST** /api2/json/chineseNameCandidatesBatch | Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname).
[**chinese_name_candidates_gender_batch**](ChineseApi.md#chinese_name_candidates_gender_batch) | **POST** /api2/json/chineseNameCandidatesGenderBatch | Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname).
[**chinese_name_gender_candidates**](ChineseApi.md#chinese_name_gender_candidates) | **GET** /api2/json/chineseNameGenderCandidates/{chineseSurnameLatin}/{chineseGivenNameLatin}/{knownGender} | Identify Chinese name candidates, based on the romanized name - having a known gender (&#39;male&#39; or &#39;female&#39;)


# **chinese_name_candidates**
> RomanizedNameOut chinese_name_candidates(chinese_surname_latin, chinese_given_name_latin)

Identify Chinese name candidates, based on the romanized name.

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
    # Identify Chinese name candidates, based on the romanized name.
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

[**RomanizedNameOut**](RomanizedNameOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chinese_name_candidates_batch**
> BatchNameMatchCandidatesOut chinese_name_candidates_batch(batch_first_last_name_in=batch_first_last_name_in)

Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname).

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
    # Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname).
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
> BatchNameMatchCandidatesOut chinese_name_candidates_gender_batch(batch_first_last_name_in=batch_first_last_name_in)

Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname).

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
    # Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname).
    api_response = api_instance.chinese_name_candidates_gender_batch(batch_first_last_name_in=batch_first_last_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChineseApi->chinese_name_candidates_gender_batch: %s\n" % e)
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

# **chinese_name_gender_candidates**
> RomanizedNameOut chinese_name_gender_candidates(chinese_surname_latin, chinese_given_name_latin, known_gender)

Identify Chinese name candidates, based on the romanized name - having a known gender ('male' or 'female')

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
    # Identify Chinese name candidates, based on the romanized name - having a known gender ('male' or 'female')
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

[**RomanizedNameOut**](RomanizedNameOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

