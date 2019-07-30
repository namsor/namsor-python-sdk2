# openapi_client.PersonalApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**country**](PersonalApi.md#country) | **GET** /api2/json/country/{personalNameFull} | [USES 10 UNITS] Infer the likely country of residence of a personal full name, or one surname. Assumes names as they are in the country of residence OR the country of origin.
[**country_batch**](PersonalApi.md#country_batch) | **POST** /api2/json/countryBatch | [USES 10 UNITS] Infer the likely country of residence of up to 100 personal full names, or surnames. Assumes names as they are in the country of residence OR the country of origin.
[**diaspora**](PersonalApi.md#diaspora) | **GET** /api2/json/diaspora/{countryIso2}/{firstName}/{lastName} | [USES 20 UNITS] Infer the likely ethnicity/diaspora of a personal name, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)
[**diaspora_batch**](PersonalApi.md#diaspora_batch) | **POST** /api2/json/diasporaBatch | [USES 20 UNITS] Infer the likely ethnicity/diaspora of up to 100 personal names, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)
[**gender**](PersonalApi.md#gender) | **GET** /api2/json/gender/{firstName}/{lastName} | Infer the likely gender of a name.
[**gender_batch**](PersonalApi.md#gender_batch) | **POST** /api2/json/genderBatch | Infer the likely gender of up to 100 names, detecting automatically the cultural context.
[**gender_full**](PersonalApi.md#gender_full) | **GET** /api2/json/genderFull/{fullName} | Infer the likely gender of a full name, ex. John H. Smith
[**gender_full_batch**](PersonalApi.md#gender_full_batch) | **POST** /api2/json/genderFullBatch | Infer the likely gender of up to 100 full names, detecting automatically the cultural context.
[**gender_full_geo**](PersonalApi.md#gender_full_geo) | **GET** /api2/json/genderFullGeo/{fullName}/{countryIso2} | Infer the likely gender of a full name, given a local context (ISO2 country code).
[**gender_full_geo_batch**](PersonalApi.md#gender_full_geo_batch) | **POST** /api2/json/genderFullGeoBatch | Infer the likely gender of up to 100 full names, with a given cultural context (country ISO2 code).
[**gender_geo**](PersonalApi.md#gender_geo) | **GET** /api2/json/genderGeo/{firstName}/{lastName}/{countryIso2} | Infer the likely gender of a name, given a local context (ISO2 country code).
[**gender_geo_batch**](PersonalApi.md#gender_geo_batch) | **POST** /api2/json/genderGeoBatch | Infer the likely gender of up to 100 names, each given a local context (ISO2 country code).
[**origin**](PersonalApi.md#origin) | **GET** /api2/json/origin/{firstName}/{lastName} | [USES 10 UNITS] Infer the likely country of origin of a personal name. Assumes names as they are in the country of origin. For US, CA, AU, NZ and other melting-pots : use &#39;diaspora&#39; instead.
[**origin_batch**](PersonalApi.md#origin_batch) | **POST** /api2/json/originBatch | [USES 10 UNITS] Infer the likely country of origin of up to 100 names, detecting automatically the cultural context.
[**parse_name**](PersonalApi.md#parse_name) | **GET** /api2/json/parseName/{nameFull} | Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. 
[**parse_name_batch**](PersonalApi.md#parse_name_batch) | **POST** /api2/json/parseNameBatch | Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John.
[**parse_name_geo**](PersonalApi.md#parse_name_geo) | **GET** /api2/json/parseName/{nameFull}/{countryIso2} | Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. For better accuracy, provide a geographic context.
[**parse_name_geo_batch**](PersonalApi.md#parse_name_geo_batch) | **POST** /api2/json/parseNameGeoBatch | Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. Giving a local context improves precision. 
[**parsed_gender_batch**](PersonalApi.md#parsed_gender_batch) | **POST** /api2/json/parsedGenderBatch | Infer the likely gender of up to 100 fully parsed names, detecting automatically the cultural context.
[**parsed_gender_geo_batch**](PersonalApi.md#parsed_gender_geo_batch) | **POST** /api2/json/parsedGenderGeoBatch | Infer the likely gender of up to 100 fully parsed names, detecting automatically the cultural context.
[**us_race_ethnicity**](PersonalApi.md#us_race_ethnicity) | **GET** /api2/json/usRaceEthnicity/{firstName}/{lastName} | [USES 10 UNITS] Infer a US resident&#39;s likely race/ethnicity according to US Census taxonomy W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino).
[**us_race_ethnicity_batch**](PersonalApi.md#us_race_ethnicity_batch) | **POST** /api2/json/usRaceEthnicityBatch | [USES 10 UNITS] Infer up-to 100 US resident&#39;s likely race/ethnicity according to US Census taxonomy.
[**us_race_ethnicity_zip5**](PersonalApi.md#us_race_ethnicity_zip5) | **GET** /api2/json/usRaceEthnicityZIP5/{firstName}/{lastName}/{zip5Code} | [USES 10 UNITS] Infer a US resident&#39;s likely race/ethnicity according to US Census taxonomy, using (optional) ZIP5 code info. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino).
[**us_zip_race_ethnicity_batch**](PersonalApi.md#us_zip_race_ethnicity_batch) | **POST** /api2/json/usZipRaceEthnicityBatch | [USES 10 UNITS] Infer up-to 100 US resident&#39;s likely race/ethnicity according to US Census taxonomy, with (optional) ZIP code.


# **country**
> PersonalNameGeoOut country(personal_name_full)

[USES 10 UNITS] Infer the likely country of residence of a personal full name, or one surname. Assumes names as they are in the country of residence OR the country of origin.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
personal_name_full = 'personal_name_full_example' # str | 

try:
    # [USES 10 UNITS] Infer the likely country of residence of a personal full name, or one surname. Assumes names as they are in the country of residence OR the country of origin.
    api_response = api_instance.country(personal_name_full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personal_name_full** | **str**|  | 

### Return type

[**PersonalNameGeoOut**](PersonalNameGeoOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **country_batch**
> BatchPersonalNameGeoOut country_batch(batch_personal_name_in=batch_personal_name_in)

[USES 10 UNITS] Infer the likely country of residence of up to 100 personal full names, or surnames. Assumes names as they are in the country of residence OR the country of origin.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_personal_name_in = openapi_client.BatchPersonalNameIn() # BatchPersonalNameIn | A list of personal names (optional)

try:
    # [USES 10 UNITS] Infer the likely country of residence of up to 100 personal full names, or surnames. Assumes names as they are in the country of residence OR the country of origin.
    api_response = api_instance.country_batch(batch_personal_name_in=batch_personal_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->country_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_personal_name_in** | [**BatchPersonalNameIn**](BatchPersonalNameIn.md)| A list of personal names | [optional] 

### Return type

[**BatchPersonalNameGeoOut**](BatchPersonalNameGeoOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diaspora**
> FirstLastNameDiasporaedOut diaspora(country_iso2, first_name, last_name)

[USES 20 UNITS] Infer the likely ethnicity/diaspora of a personal name, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
country_iso2 = 'country_iso2_example' # str | 
first_name = 'first_name_example' # str | 
last_name = 'last_name_example' # str | 

try:
    # [USES 20 UNITS] Infer the likely ethnicity/diaspora of a personal name, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)
    api_response = api_instance.diaspora(country_iso2, first_name, last_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->diaspora: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_iso2** | **str**|  | 
 **first_name** | **str**|  | 
 **last_name** | **str**|  | 

### Return type

[**FirstLastNameDiasporaedOut**](FirstLastNameDiasporaedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diaspora_batch**
> BatchFirstLastNameDiasporaedOut diaspora_batch(batch_first_last_name_geo_in=batch_first_last_name_geo_in)

[USES 20 UNITS] Infer the likely ethnicity/diaspora of up to 100 personal names, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_first_last_name_geo_in = openapi_client.BatchFirstLastNameGeoIn() # BatchFirstLastNameGeoIn | A list of personal names (optional)

try:
    # [USES 20 UNITS] Infer the likely ethnicity/diaspora of up to 100 personal names, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)
    api_response = api_instance.diaspora_batch(batch_first_last_name_geo_in=batch_first_last_name_geo_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->diaspora_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_first_last_name_geo_in** | [**BatchFirstLastNameGeoIn**](BatchFirstLastNameGeoIn.md)| A list of personal names | [optional] 

### Return type

[**BatchFirstLastNameDiasporaedOut**](BatchFirstLastNameDiasporaedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender**
> FirstLastNameGenderedOut gender(first_name, last_name)

Infer the likely gender of a name.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
first_name = 'first_name_example' # str | 
last_name = 'last_name_example' # str | 

try:
    # Infer the likely gender of a name.
    api_response = api_instance.gender(first_name, last_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->gender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**|  | 
 **last_name** | **str**|  | 

### Return type

[**FirstLastNameGenderedOut**](FirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_batch**
> BatchFirstLastNameGenderedOut gender_batch(batch_first_last_name_in=batch_first_last_name_in)

Infer the likely gender of up to 100 names, detecting automatically the cultural context.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_first_last_name_in = openapi_client.BatchFirstLastNameIn() # BatchFirstLastNameIn | A list of personal names (optional)

try:
    # Infer the likely gender of up to 100 names, detecting automatically the cultural context.
    api_response = api_instance.gender_batch(batch_first_last_name_in=batch_first_last_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->gender_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_first_last_name_in** | [**BatchFirstLastNameIn**](BatchFirstLastNameIn.md)| A list of personal names | [optional] 

### Return type

[**BatchFirstLastNameGenderedOut**](BatchFirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_full**
> FirstLastNameGenderedOut gender_full(full_name)

Infer the likely gender of a full name, ex. John H. Smith

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
full_name = 'full_name_example' # str | 

try:
    # Infer the likely gender of a full name, ex. John H. Smith
    api_response = api_instance.gender_full(full_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->gender_full: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_name** | **str**|  | 

### Return type

[**FirstLastNameGenderedOut**](FirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_full_batch**
> BatchPersonalNameGenderedOut gender_full_batch(batch_personal_name_in=batch_personal_name_in)

Infer the likely gender of up to 100 full names, detecting automatically the cultural context.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_personal_name_in = openapi_client.BatchPersonalNameIn() # BatchPersonalNameIn | A list of personal names (optional)

try:
    # Infer the likely gender of up to 100 full names, detecting automatically the cultural context.
    api_response = api_instance.gender_full_batch(batch_personal_name_in=batch_personal_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->gender_full_batch: %s\n" % e)
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

# **gender_full_geo**
> FirstLastNameGenderedOut gender_full_geo(full_name, country_iso2)

Infer the likely gender of a full name, given a local context (ISO2 country code).

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
full_name = 'full_name_example' # str | 
country_iso2 = 'country_iso2_example' # str | 

try:
    # Infer the likely gender of a full name, given a local context (ISO2 country code).
    api_response = api_instance.gender_full_geo(full_name, country_iso2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->gender_full_geo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_name** | **str**|  | 
 **country_iso2** | **str**|  | 

### Return type

[**FirstLastNameGenderedOut**](FirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_full_geo_batch**
> BatchPersonalNameGenderedOut gender_full_geo_batch(batch_personal_name_geo_in=batch_personal_name_geo_in)

Infer the likely gender of up to 100 full names, with a given cultural context (country ISO2 code).

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_personal_name_geo_in = openapi_client.BatchPersonalNameGeoIn() # BatchPersonalNameGeoIn | A list of personal names, with a country ISO2 code (optional)

try:
    # Infer the likely gender of up to 100 full names, with a given cultural context (country ISO2 code).
    api_response = api_instance.gender_full_geo_batch(batch_personal_name_geo_in=batch_personal_name_geo_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->gender_full_geo_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_personal_name_geo_in** | [**BatchPersonalNameGeoIn**](BatchPersonalNameGeoIn.md)| A list of personal names, with a country ISO2 code | [optional] 

### Return type

[**BatchPersonalNameGenderedOut**](BatchPersonalNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_geo**
> FirstLastNameGenderedOut gender_geo(first_name, last_name, country_iso2)

Infer the likely gender of a name, given a local context (ISO2 country code).

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**|  | 
 **last_name** | **str**|  | 
 **country_iso2** | **str**|  | 

### Return type

[**FirstLastNameGenderedOut**](FirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gender_geo_batch**
> BatchFirstLastNameGenderedOut gender_geo_batch(batch_first_last_name_geo_in=batch_first_last_name_geo_in)

Infer the likely gender of up to 100 names, each given a local context (ISO2 country code).

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_first_last_name_geo_in = openapi_client.BatchFirstLastNameGeoIn() # BatchFirstLastNameGeoIn | A list of names, with country code. (optional)

try:
    # Infer the likely gender of up to 100 names, each given a local context (ISO2 country code).
    api_response = api_instance.gender_geo_batch(batch_first_last_name_geo_in=batch_first_last_name_geo_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->gender_geo_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_first_last_name_geo_in** | [**BatchFirstLastNameGeoIn**](BatchFirstLastNameGeoIn.md)| A list of names, with country code. | [optional] 

### Return type

[**BatchFirstLastNameGenderedOut**](BatchFirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **origin**
> FirstLastNameOriginedOut origin(first_name, last_name)

[USES 10 UNITS] Infer the likely country of origin of a personal name. Assumes names as they are in the country of origin. For US, CA, AU, NZ and other melting-pots : use 'diaspora' instead.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
first_name = 'first_name_example' # str | 
last_name = 'last_name_example' # str | 

try:
    # [USES 10 UNITS] Infer the likely country of origin of a personal name. Assumes names as they are in the country of origin. For US, CA, AU, NZ and other melting-pots : use 'diaspora' instead.
    api_response = api_instance.origin(first_name, last_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->origin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**|  | 
 **last_name** | **str**|  | 

### Return type

[**FirstLastNameOriginedOut**](FirstLastNameOriginedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **origin_batch**
> BatchFirstLastNameOriginedOut origin_batch(batch_first_last_name_in=batch_first_last_name_in)

[USES 10 UNITS] Infer the likely country of origin of up to 100 names, detecting automatically the cultural context.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_first_last_name_in = openapi_client.BatchFirstLastNameIn() # BatchFirstLastNameIn | A list of personal names (optional)

try:
    # [USES 10 UNITS] Infer the likely country of origin of up to 100 names, detecting automatically the cultural context.
    api_response = api_instance.origin_batch(batch_first_last_name_in=batch_first_last_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->origin_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_first_last_name_in** | [**BatchFirstLastNameIn**](BatchFirstLastNameIn.md)| A list of personal names | [optional] 

### Return type

[**BatchFirstLastNameOriginedOut**](BatchFirstLastNameOriginedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_name**
> PersonalNameParsedOut parse_name(name_full)

Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. 

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
name_full = 'name_full_example' # str | 

try:
    # Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. 
    api_response = api_instance.parse_name(name_full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->parse_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_full** | **str**|  | 

### Return type

[**PersonalNameParsedOut**](PersonalNameParsedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_name_batch**
> BatchPersonalNameParsedOut parse_name_batch(batch_personal_name_in=batch_personal_name_in)

Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_personal_name_in = openapi_client.BatchPersonalNameIn() # BatchPersonalNameIn | A list of personal names (optional)

try:
    # Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John.
    api_response = api_instance.parse_name_batch(batch_personal_name_in=batch_personal_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->parse_name_batch: %s\n" % e)
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

# **parse_name_geo**
> PersonalNameParsedOut parse_name_geo(name_full, country_iso2)

Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. For better accuracy, provide a geographic context.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
name_full = 'name_full_example' # str | 
country_iso2 = 'country_iso2_example' # str | 

try:
    # Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. For better accuracy, provide a geographic context.
    api_response = api_instance.parse_name_geo(name_full, country_iso2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->parse_name_geo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_full** | **str**|  | 
 **country_iso2** | **str**|  | 

### Return type

[**PersonalNameParsedOut**](PersonalNameParsedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_name_geo_batch**
> BatchPersonalNameParsedOut parse_name_geo_batch(batch_personal_name_geo_in=batch_personal_name_geo_in)

Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. Giving a local context improves precision. 

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_personal_name_geo_in = openapi_client.BatchPersonalNameGeoIn() # BatchPersonalNameGeoIn | A list of personal names (optional)

try:
    # Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. Giving a local context improves precision. 
    api_response = api_instance.parse_name_geo_batch(batch_personal_name_geo_in=batch_personal_name_geo_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->parse_name_geo_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_personal_name_geo_in** | [**BatchPersonalNameGeoIn**](BatchPersonalNameGeoIn.md)| A list of personal names | [optional] 

### Return type

[**BatchPersonalNameParsedOut**](BatchPersonalNameParsedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parsed_gender_batch**
> BatchFirstLastNameGenderedOut parsed_gender_batch(batch_parsed_full_name_in=batch_parsed_full_name_in)

Infer the likely gender of up to 100 fully parsed names, detecting automatically the cultural context.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_parsed_full_name_in = openapi_client.BatchParsedFullNameIn() # BatchParsedFullNameIn | A list of personal names (optional)

try:
    # Infer the likely gender of up to 100 fully parsed names, detecting automatically the cultural context.
    api_response = api_instance.parsed_gender_batch(batch_parsed_full_name_in=batch_parsed_full_name_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->parsed_gender_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_parsed_full_name_in** | [**BatchParsedFullNameIn**](BatchParsedFullNameIn.md)| A list of personal names | [optional] 

### Return type

[**BatchFirstLastNameGenderedOut**](BatchFirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parsed_gender_geo_batch**
> BatchFirstLastNameGenderedOut parsed_gender_geo_batch(batch_parsed_full_name_geo_in=batch_parsed_full_name_geo_in)

Infer the likely gender of up to 100 fully parsed names, detecting automatically the cultural context.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_parsed_full_name_geo_in = openapi_client.BatchParsedFullNameGeoIn() # BatchParsedFullNameGeoIn | A list of personal names (optional)

try:
    # Infer the likely gender of up to 100 fully parsed names, detecting automatically the cultural context.
    api_response = api_instance.parsed_gender_geo_batch(batch_parsed_full_name_geo_in=batch_parsed_full_name_geo_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->parsed_gender_geo_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_parsed_full_name_geo_in** | [**BatchParsedFullNameGeoIn**](BatchParsedFullNameGeoIn.md)| A list of personal names | [optional] 

### Return type

[**BatchFirstLastNameGenderedOut**](BatchFirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **us_race_ethnicity**
> FirstLastNameUSRaceEthnicityOut us_race_ethnicity(first_name, last_name)

[USES 10 UNITS] Infer a US resident's likely race/ethnicity according to US Census taxonomy W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino).

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
first_name = 'first_name_example' # str | 
last_name = 'last_name_example' # str | 

try:
    # [USES 10 UNITS] Infer a US resident's likely race/ethnicity according to US Census taxonomy W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino).
    api_response = api_instance.us_race_ethnicity(first_name, last_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->us_race_ethnicity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**|  | 
 **last_name** | **str**|  | 

### Return type

[**FirstLastNameUSRaceEthnicityOut**](FirstLastNameUSRaceEthnicityOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **us_race_ethnicity_batch**
> BatchFirstLastNameUSRaceEthnicityOut us_race_ethnicity_batch(batch_first_last_name_geo_in=batch_first_last_name_geo_in)

[USES 10 UNITS] Infer up-to 100 US resident's likely race/ethnicity according to US Census taxonomy.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_first_last_name_geo_in = openapi_client.BatchFirstLastNameGeoIn() # BatchFirstLastNameGeoIn | A list of personal names (optional)

try:
    # [USES 10 UNITS] Infer up-to 100 US resident's likely race/ethnicity according to US Census taxonomy.
    api_response = api_instance.us_race_ethnicity_batch(batch_first_last_name_geo_in=batch_first_last_name_geo_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->us_race_ethnicity_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_first_last_name_geo_in** | [**BatchFirstLastNameGeoIn**](BatchFirstLastNameGeoIn.md)| A list of personal names | [optional] 

### Return type

[**BatchFirstLastNameUSRaceEthnicityOut**](BatchFirstLastNameUSRaceEthnicityOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **us_race_ethnicity_zip5**
> FirstLastNameUSRaceEthnicityOut us_race_ethnicity_zip5(first_name, last_name, zip5_code)

[USES 10 UNITS] Infer a US resident's likely race/ethnicity according to US Census taxonomy, using (optional) ZIP5 code info. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino).

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
first_name = 'first_name_example' # str | 
last_name = 'last_name_example' # str | 
zip5_code = 'zip5_code_example' # str | 

try:
    # [USES 10 UNITS] Infer a US resident's likely race/ethnicity according to US Census taxonomy, using (optional) ZIP5 code info. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino).
    api_response = api_instance.us_race_ethnicity_zip5(first_name, last_name, zip5_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->us_race_ethnicity_zip5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**|  | 
 **last_name** | **str**|  | 
 **zip5_code** | **str**|  | 

### Return type

[**FirstLastNameUSRaceEthnicityOut**](FirstLastNameUSRaceEthnicityOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **us_zip_race_ethnicity_batch**
> BatchFirstLastNameUSRaceEthnicityOut us_zip_race_ethnicity_batch(batch_first_last_name_geo_zipped_in=batch_first_last_name_geo_zipped_in)

[USES 10 UNITS] Infer up-to 100 US resident's likely race/ethnicity according to US Census taxonomy, with (optional) ZIP code.

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
api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
batch_first_last_name_geo_zipped_in = openapi_client.BatchFirstLastNameGeoZippedIn() # BatchFirstLastNameGeoZippedIn | A list of personal names (optional)

try:
    # [USES 10 UNITS] Infer up-to 100 US resident's likely race/ethnicity according to US Census taxonomy, with (optional) ZIP code.
    api_response = api_instance.us_zip_race_ethnicity_batch(batch_first_last_name_geo_zipped_in=batch_first_last_name_geo_zipped_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalApi->us_zip_race_ethnicity_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_first_last_name_geo_zipped_in** | [**BatchFirstLastNameGeoZippedIn**](BatchFirstLastNameGeoZippedIn.md)| A list of personal names | [optional] 

### Return type

[**BatchFirstLastNameUSRaceEthnicityOut**](BatchFirstLastNameUSRaceEthnicityOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

