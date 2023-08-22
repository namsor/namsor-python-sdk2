<a id="__pageTop"></a>
# openapi_client.apis.tags.indian_api.IndianApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**caste_indian_batch**](#caste_indian_batch) | **post** /api2/json/casteIndianBatch | [USES 10 UNITS PER NAME] Infer the likely Indian name caste of up to 100 personal Indian Hindu names. 
[**castegroup_indian**](#castegroup_indian) | **get** /api2/json/castegroupIndian/{subDivisionIso31662}/{firstName}/{lastName} | [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of a first / last name.
[**castegroup_indian_batch**](#castegroup_indian_batch) | **post** /api2/json/castegroupIndianBatch | [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of up to 100 personal first / last names. 
[**castegroup_indian_full**](#castegroup_indian_full) | **get** /api2/json/castegroupIndianFull/{subDivisionIso31662}/{personalNameFull} | [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of a personal full name.
[**castegroup_indian_full_batch**](#castegroup_indian_full_batch) | **post** /api2/json/castegroupIndianFullBatch | [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of up to 100 personal full names. 
[**castegroup_indian_hindu**](#castegroup_indian_hindu) | **get** /api2/json/casteIndian/{subDivisionIso31662}/{firstName}/{lastName} | [USES 10 UNITS PER NAME] Infer the likely Indian name caste of a personal Hindu name.
[**religion**](#religion) | **get** /api2/json/religionIndianFull/{subDivisionIso31662}/{personalNameFull} | [USES 10 UNITS PER NAME] Infer the likely religion of a personal Indian full name, provided the Indian state or Union territory (NB/ this can be inferred using the subclassification endpoint).
[**religion1**](#religion1) | **get** /api2/json/religionIndian/{subDivisionIso31662}/{firstName}/{lastName} | [USES 10 UNITS PER NAME] Infer the likely religion of a personal Indian first/last name, provided the Indian state or Union territory (NB/ this can be inferred using the subclassification endpoint).
[**religion_indian_batch**](#religion_indian_batch) | **post** /api2/json/religionIndianBatch | [USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal first/last Indian names, provided the subclassification at State or Union territory level (NB/ can be inferred using the subclassification endpoint).
[**religion_indian_full_batch**](#religion_indian_full_batch) | **post** /api2/json/religionIndianFullBatch | [USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal full Indian names, provided the subclassification at State or Union territory level (NB/ can be inferred using the subclassification endpoint).
[**subclassification_indian**](#subclassification_indian) | **get** /api2/json/subclassificationIndian/{firstName}/{lastName} | [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.
[**subclassification_indian_batch**](#subclassification_indian_batch) | **post** /api2/json/subclassificationIndianBatch | [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.
[**subclassification_indian_full**](#subclassification_indian_full) | **get** /api2/json/subclassificationIndianFull/{fullName} | [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.
[**subclassification_indian_full_batch**](#subclassification_indian_full_batch) | **post** /api2/json/subclassificationIndianFullBatch | [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.

# **caste_indian_batch**
<a id="caste_indian_batch"></a>
> BatchFirstLastNameCasteOut caste_indian_batch()

[USES 10 UNITS PER NAME] Infer the likely Indian name caste of up to 100 personal Indian Hindu names. 

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.batch_first_last_name_caste_out import BatchFirstLastNameCasteOut
from openapi_client.model.batch_first_last_name_geo_subdivision_in import BatchFirstLastNameGeoSubdivisionIn
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only optional values
    body = BatchFirstLastNameGeoSubdivisionIn(
        personal_names=[
            FirstLastNameGeoSubdivisionIn(
                id="id_example",
                first_name="first_name_example",
                last_name="last_name_example",
                country_iso2="country_iso2_example",
                subdivision_iso="subdivision_iso_example",
            )
        ],
    )
    try:
        # [USES 10 UNITS PER NAME] Infer the likely Indian name caste of up to 100 personal Indian Hindu names. 
        api_response = api_instance.caste_indian_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->caste_indian_batch: %s\n" % e)
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
[**BatchFirstLastNameGeoSubdivisionIn**](../../models/BatchFirstLastNameGeoSubdivisionIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#caste_indian_batch.ApiResponseFor200) | A list of castegroup-coded names.
401 | [ApiResponseFor401](#caste_indian_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#caste_indian_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#caste_indian_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### caste_indian_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchFirstLastNameCasteOut**](../../models/BatchFirstLastNameCasteOut.md) |  | 


#### caste_indian_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### caste_indian_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### caste_indian_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **castegroup_indian**
<a id="castegroup_indian"></a>
> FirstLastNameCastegroupOut castegroup_indian(sub_division_iso31662first_namelast_name)

[USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of a first / last name.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.first_last_name_castegroup_out import FirstLastNameCastegroupOut
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'subDivisionIso31662': "subDivisionIso31662_example",
        'firstName': "firstName_example",
        'lastName': "lastName_example",
    }
    try:
        # [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of a first / last name.
        api_response = api_instance.castegroup_indian(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->castegroup_indian: %s\n" % e)
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
subDivisionIso31662 | SubDivisionIso31662Schema | | 
firstName | FirstNameSchema | | 
lastName | LastNameSchema | | 

# SubDivisionIso31662Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FirstNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#castegroup_indian.ApiResponseFor200) | A castegroup-coded name.
401 | [ApiResponseFor401](#castegroup_indian.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#castegroup_indian.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### castegroup_indian.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FirstLastNameCastegroupOut**](../../models/FirstLastNameCastegroupOut.md) |  | 


#### castegroup_indian.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### castegroup_indian.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **castegroup_indian_batch**
<a id="castegroup_indian_batch"></a>
> BatchFirstLastNameCastegroupOut castegroup_indian_batch()

[USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of up to 100 personal first / last names. 

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.batch_first_last_name_castegroup_out import BatchFirstLastNameCastegroupOut
from openapi_client.model.batch_first_last_name_subdivision_in import BatchFirstLastNameSubdivisionIn
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only optional values
    body = BatchFirstLastNameSubdivisionIn(
        personal_names=[
            FirstLastNameSubdivisionIn(
                id="id_example",
                first_name="first_name_example",
                last_name="last_name_example",
                subdivision_iso="subdivision_iso_example",
            )
        ],
    )
    try:
        # [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of up to 100 personal first / last names. 
        api_response = api_instance.castegroup_indian_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->castegroup_indian_batch: %s\n" % e)
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
[**BatchFirstLastNameSubdivisionIn**](../../models/BatchFirstLastNameSubdivisionIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#castegroup_indian_batch.ApiResponseFor200) | A list of castegroup-coded names.
401 | [ApiResponseFor401](#castegroup_indian_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#castegroup_indian_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#castegroup_indian_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### castegroup_indian_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchFirstLastNameCastegroupOut**](../../models/BatchFirstLastNameCastegroupOut.md) |  | 


#### castegroup_indian_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### castegroup_indian_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### castegroup_indian_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **castegroup_indian_full**
<a id="castegroup_indian_full"></a>
> PersonalNameCastegroupOut castegroup_indian_full(sub_division_iso31662personal_name_full)

[USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of a personal full name.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.personal_name_castegroup_out import PersonalNameCastegroupOut
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'subDivisionIso31662': "subDivisionIso31662_example",
        'personalNameFull': "personalNameFull_example",
    }
    try:
        # [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of a personal full name.
        api_response = api_instance.castegroup_indian_full(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->castegroup_indian_full: %s\n" % e)
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
subDivisionIso31662 | SubDivisionIso31662Schema | | 
personalNameFull | PersonalNameFullSchema | | 

# SubDivisionIso31662Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PersonalNameFullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#castegroup_indian_full.ApiResponseFor200) | A castegroup-coded name.
401 | [ApiResponseFor401](#castegroup_indian_full.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#castegroup_indian_full.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### castegroup_indian_full.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PersonalNameCastegroupOut**](../../models/PersonalNameCastegroupOut.md) |  | 


#### castegroup_indian_full.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### castegroup_indian_full.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **castegroup_indian_full_batch**
<a id="castegroup_indian_full_batch"></a>
> BatchPersonalNameCastegroupOut castegroup_indian_full_batch()

[USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of up to 100 personal full names. 

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.batch_personal_name_castegroup_out import BatchPersonalNameCastegroupOut
from openapi_client.model.batch_personal_name_subdivision_in import BatchPersonalNameSubdivisionIn
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only optional values
    body = BatchPersonalNameSubdivisionIn(
        personal_names=[
            PersonalNameSubdivisionIn(
                id="id_example",
                name="name_example",
                subdivision_iso="subdivision_iso_example",
            )
        ],
    )
    try:
        # [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of up to 100 personal full names. 
        api_response = api_instance.castegroup_indian_full_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->castegroup_indian_full_batch: %s\n" % e)
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
[**BatchPersonalNameSubdivisionIn**](../../models/BatchPersonalNameSubdivisionIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#castegroup_indian_full_batch.ApiResponseFor200) | A list of castegroup-coded names.
401 | [ApiResponseFor401](#castegroup_indian_full_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#castegroup_indian_full_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#castegroup_indian_full_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### castegroup_indian_full_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchPersonalNameCastegroupOut**](../../models/BatchPersonalNameCastegroupOut.md) |  | 


#### castegroup_indian_full_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### castegroup_indian_full_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### castegroup_indian_full_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **castegroup_indian_hindu**
<a id="castegroup_indian_hindu"></a>
> FirstLastNameCasteOut castegroup_indian_hindu(sub_division_iso31662first_namelast_name)

[USES 10 UNITS PER NAME] Infer the likely Indian name caste of a personal Hindu name.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.first_last_name_caste_out import FirstLastNameCasteOut
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'subDivisionIso31662': "subDivisionIso31662_example",
        'firstName': "firstName_example",
        'lastName': "lastName_example",
    }
    try:
        # [USES 10 UNITS PER NAME] Infer the likely Indian name caste of a personal Hindu name.
        api_response = api_instance.castegroup_indian_hindu(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->castegroup_indian_hindu: %s\n" % e)
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
subDivisionIso31662 | SubDivisionIso31662Schema | | 
firstName | FirstNameSchema | | 
lastName | LastNameSchema | | 

# SubDivisionIso31662Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FirstNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#castegroup_indian_hindu.ApiResponseFor200) | A caste-coded name.
401 | [ApiResponseFor401](#castegroup_indian_hindu.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#castegroup_indian_hindu.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### castegroup_indian_hindu.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FirstLastNameCasteOut**](../../models/FirstLastNameCasteOut.md) |  | 


#### castegroup_indian_hindu.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### castegroup_indian_hindu.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **religion**
<a id="religion"></a>
> PersonalNameReligionedOut religion(sub_division_iso31662personal_name_full)

[USES 10 UNITS PER NAME] Infer the likely religion of a personal Indian full name, provided the Indian state or Union territory (NB/ this can be inferred using the subclassification endpoint).

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.personal_name_religioned_out import PersonalNameReligionedOut
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'subDivisionIso31662': "subDivisionIso31662_example",
        'personalNameFull': "personalNameFull_example",
    }
    try:
        # [USES 10 UNITS PER NAME] Infer the likely religion of a personal Indian full name, provided the Indian state or Union territory (NB/ this can be inferred using the subclassification endpoint).
        api_response = api_instance.religion(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->religion: %s\n" % e)
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
subDivisionIso31662 | SubDivisionIso31662Schema | | 
personalNameFull | PersonalNameFullSchema | | 

# SubDivisionIso31662Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PersonalNameFullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#religion.ApiResponseFor200) | A religion-coded name.
401 | [ApiResponseFor401](#religion.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#religion.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### religion.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PersonalNameReligionedOut**](../../models/PersonalNameReligionedOut.md) |  | 


#### religion.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### religion.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **religion1**
<a id="religion1"></a>
> FirstLastNameReligionedOut religion1(sub_division_iso31662first_namelast_name)

[USES 10 UNITS PER NAME] Infer the likely religion of a personal Indian first/last name, provided the Indian state or Union territory (NB/ this can be inferred using the subclassification endpoint).

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.first_last_name_religioned_out import FirstLastNameReligionedOut
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'subDivisionIso31662': "subDivisionIso31662_example",
        'firstName': "firstName_example",
        'lastName': "lastName_example",
    }
    try:
        # [USES 10 UNITS PER NAME] Infer the likely religion of a personal Indian first/last name, provided the Indian state or Union territory (NB/ this can be inferred using the subclassification endpoint).
        api_response = api_instance.religion1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->religion1: %s\n" % e)
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
subDivisionIso31662 | SubDivisionIso31662Schema | | 
firstName | FirstNameSchema | | 
lastName | LastNameSchema | | 

# SubDivisionIso31662Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FirstNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#religion1.ApiResponseFor200) | A religion-coded name.
401 | [ApiResponseFor401](#religion1.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#religion1.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### religion1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FirstLastNameReligionedOut**](../../models/FirstLastNameReligionedOut.md) |  | 


#### religion1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### religion1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **religion_indian_batch**
<a id="religion_indian_batch"></a>
> BatchFirstLastNameReligionedOut religion_indian_batch()

[USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal first/last Indian names, provided the subclassification at State or Union territory level (NB/ can be inferred using the subclassification endpoint).

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.batch_first_last_name_religioned_out import BatchFirstLastNameReligionedOut
from openapi_client.model.batch_first_last_name_subdivision_in import BatchFirstLastNameSubdivisionIn
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only optional values
    body = BatchFirstLastNameSubdivisionIn(
        personal_names=[
            FirstLastNameSubdivisionIn(
                id="id_example",
                first_name="first_name_example",
                last_name="last_name_example",
                subdivision_iso="subdivision_iso_example",
            )
        ],
    )
    try:
        # [USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal first/last Indian names, provided the subclassification at State or Union territory level (NB/ can be inferred using the subclassification endpoint).
        api_response = api_instance.religion_indian_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->religion_indian_batch: %s\n" % e)
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
[**BatchFirstLastNameSubdivisionIn**](../../models/BatchFirstLastNameSubdivisionIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#religion_indian_batch.ApiResponseFor200) | A list of religion-coded names.
401 | [ApiResponseFor401](#religion_indian_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#religion_indian_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#religion_indian_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### religion_indian_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchFirstLastNameReligionedOut**](../../models/BatchFirstLastNameReligionedOut.md) |  | 


#### religion_indian_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### religion_indian_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### religion_indian_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **religion_indian_full_batch**
<a id="religion_indian_full_batch"></a>
> BatchPersonalNameReligionedOut religion_indian_full_batch()

[USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal full Indian names, provided the subclassification at State or Union territory level (NB/ can be inferred using the subclassification endpoint).

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.batch_personal_name_religioned_out import BatchPersonalNameReligionedOut
from openapi_client.model.batch_personal_name_subdivision_in import BatchPersonalNameSubdivisionIn
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only optional values
    body = BatchPersonalNameSubdivisionIn(
        personal_names=[
            PersonalNameSubdivisionIn(
                id="id_example",
                name="name_example",
                subdivision_iso="subdivision_iso_example",
            )
        ],
    )
    try:
        # [USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal full Indian names, provided the subclassification at State or Union territory level (NB/ can be inferred using the subclassification endpoint).
        api_response = api_instance.religion_indian_full_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->religion_indian_full_batch: %s\n" % e)
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
[**BatchPersonalNameSubdivisionIn**](../../models/BatchPersonalNameSubdivisionIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#religion_indian_full_batch.ApiResponseFor200) | A list of religion-coded names.
401 | [ApiResponseFor401](#religion_indian_full_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#religion_indian_full_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#religion_indian_full_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### religion_indian_full_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchPersonalNameReligionedOut**](../../models/BatchPersonalNameReligionedOut.md) |  | 


#### religion_indian_full_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### religion_indian_full_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### religion_indian_full_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **subclassification_indian**
<a id="subclassification_indian"></a>
> FirstLastNameGeoSubclassificationOut subclassification_indian(first_namelast_name)

[USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.first_last_name_geo_subclassification_out import FirstLastNameGeoSubclassificationOut
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'firstName': "firstName_example",
        'lastName': "lastName_example",
    }
    try:
        # [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.
        api_response = api_instance.subclassification_indian(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->subclassification_indian: %s\n" % e)
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
firstName | FirstNameSchema | | 
lastName | LastNameSchema | | 

# FirstNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#subclassification_indian.ApiResponseFor200) | A classified name at a sub-country level.
401 | [ApiResponseFor401](#subclassification_indian.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#subclassification_indian.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### subclassification_indian.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FirstLastNameGeoSubclassificationOut**](../../models/FirstLastNameGeoSubclassificationOut.md) |  | 


#### subclassification_indian.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### subclassification_indian.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **subclassification_indian_batch**
<a id="subclassification_indian_batch"></a>
> BatchFirstLastNameGeoSubclassificationOut subclassification_indian_batch()

[USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.batch_first_last_name_geo_subclassification_out import BatchFirstLastNameGeoSubclassificationOut
from openapi_client.model.batch_first_last_name_geo_in import BatchFirstLastNameGeoIn
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only optional values
    body = BatchFirstLastNameGeoIn(
        personal_names=[
            FirstLastNameGeoIn(
                id="id_example",
                first_name="first_name_example",
                last_name="last_name_example",
                country_iso2="country_iso2_example",
            )
        ],
    )
    try:
        # [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.
        api_response = api_instance.subclassification_indian_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->subclassification_indian_batch: %s\n" % e)
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
[**BatchFirstLastNameGeoIn**](../../models/BatchFirstLastNameGeoIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#subclassification_indian_batch.ApiResponseFor200) | A list of classified names at a subcountry level.
401 | [ApiResponseFor401](#subclassification_indian_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#subclassification_indian_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#subclassification_indian_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### subclassification_indian_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchFirstLastNameGeoSubclassificationOut**](../../models/BatchFirstLastNameGeoSubclassificationOut.md) |  | 


#### subclassification_indian_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### subclassification_indian_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### subclassification_indian_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **subclassification_indian_full**
<a id="subclassification_indian_full"></a>
> PersonalNameGeoSubclassificationOut subclassification_indian_full(full_name)

[USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.personal_name_geo_subclassification_out import PersonalNameGeoSubclassificationOut
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fullName': "fullName_example",
    }
    try:
        # [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.
        api_response = api_instance.subclassification_indian_full(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->subclassification_indian_full: %s\n" % e)
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
fullName | FullNameSchema | | 

# FullNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#subclassification_indian_full.ApiResponseFor200) | A classified name at a sub-country level.
401 | [ApiResponseFor401](#subclassification_indian_full.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#subclassification_indian_full.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### subclassification_indian_full.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PersonalNameGeoSubclassificationOut**](../../models/PersonalNameGeoSubclassificationOut.md) |  | 


#### subclassification_indian_full.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### subclassification_indian_full.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **subclassification_indian_full_batch**
<a id="subclassification_indian_full_batch"></a>
> BatchPersonalNameGeoSubclassificationOut subclassification_indian_full_batch()

[USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import indian_api
from openapi_client.model.batch_personal_name_geo_subclassification_out import BatchPersonalNameGeoSubclassificationOut
from openapi_client.model.batch_personal_name_geo_in import BatchPersonalNameGeoIn
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
    api_instance = indian_api.IndianApi(api_client)

    # example passing only optional values
    body = BatchPersonalNameGeoIn(
        personal_names=[
            PersonalNameGeoIn(
                id="id_example",
                name="name_example",
                country_iso2="country_iso2_example",
            )
        ],
    )
    try:
        # [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.
        api_response = api_instance.subclassification_indian_full_batch(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IndianApi->subclassification_indian_full_batch: %s\n" % e)
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
[**BatchPersonalNameGeoIn**](../../models/BatchPersonalNameGeoIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#subclassification_indian_full_batch.ApiResponseFor200) | A list of classified names at a subcountry level.
401 | [ApiResponseFor401](#subclassification_indian_full_batch.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#subclassification_indian_full_batch.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#subclassification_indian_full_batch.ApiResponseFor400) | Bad request (ex. too many names)

#### subclassification_indian_full_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchPersonalNameGeoSubclassificationOut**](../../models/BatchPersonalNameGeoSubclassificationOut.md) |  | 


#### subclassification_indian_full_batch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### subclassification_indian_full_batch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### subclassification_indian_full_batch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

