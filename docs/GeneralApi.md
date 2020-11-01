# openapi_client.GeneralApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**name_type**](GeneralApi.md#name_type) | **GET** /api2/json/nameType/{properNoun} | Infer the likely type of a proper noun (personal name, brand name, place name etc.)
[**name_type1**](GeneralApi.md#name_type1) | **GET** /api2/json/nameType/{properNoun}/{countryIso2} | Infer the likely type of a proper noun (personal name, brand name, place name etc.)


# **name_type**
> ProperNounCategorizedOut name_type(proper_noun)

Infer the likely type of a proper noun (personal name, brand name, place name etc.)

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
api_instance = openapi_client.GeneralApi(openapi_client.ApiClient(configuration))
proper_noun = 'proper_noun_example' # str | 

try:
    # Infer the likely type of a proper noun (personal name, brand name, place name etc.)
    api_response = api_instance.name_type(proper_noun)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralApi->name_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proper_noun** | **str**|  | 

### Return type

[**ProperNounCategorizedOut**](ProperNounCategorizedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **name_type1**
> ProperNounCategorizedOut name_type1(proper_noun, country_iso2)

Infer the likely type of a proper noun (personal name, brand name, place name etc.)

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
api_instance = openapi_client.GeneralApi(openapi_client.ApiClient(configuration))
proper_noun = 'proper_noun_example' # str | 
country_iso2 = 'country_iso2_example' # str | 

try:
    # Infer the likely type of a proper noun (personal name, brand name, place name etc.)
    api_response = api_instance.name_type1(proper_noun, country_iso2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralApi->name_type1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proper_noun** | **str**|  | 
 **country_iso2** | **str**|  | 

### Return type

[**ProperNounCategorizedOut**](ProperNounCategorizedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

