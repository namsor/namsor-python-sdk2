<a id="__pageTop"></a>
# openapi_client.apis.tags.admin_api.AdminApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anonymize**](#anonymize) | **get** /api2/json/anonymize/{source}/{anonymized}/{token} | Activate/deactivate anonymization for a source.
[**anonymize1**](#anonymize1) | **get** /api2/json/anonymize/{source}/{anonymized} | Activate/deactivate anonymization for a source.
[**api_key_info**](#api_key_info) | **get** /api2/json/apiKeyInfo | Read API Key info.
[**api_status**](#api_status) | **get** /api2/json/apiStatus | Prints the current status of the classifiers. A classifier name in apiStatus corresponds to a service name in apiServices.
[**api_usage**](#api_usage) | **get** /api2/json/apiUsage | Print current API usage.
[**api_usage_history**](#api_usage_history) | **get** /api2/json/apiUsageHistory | Print historical API usage.
[**api_usage_history_aggregate**](#api_usage_history_aggregate) | **get** /api2/json/apiUsageHistoryAggregate | Print historical API usage (in an aggregated view, by service, by day/hour/min).
[**available_services**](#available_services) | **get** /api2/json/apiServices | List of classification services and usage cost in Units per classification (default is 1&#x3D;ONE Unit). Some API endpoints (ex. Corridor) combine multiple classifiers.
[**disable**](#disable) | **get** /api2/json/disable/{source}/{disabled} | Activate/deactivate an API Key.
[**learnable**](#learnable) | **get** /api2/json/learnable/{source}/{learnable}/{token} | Activate/deactivate learning from a source.
[**learnable1**](#learnable1) | **get** /api2/json/learnable/{source}/{learnable} | Activate/deactivate learning from a source.
[**regions**](#regions) | **get** /api2/json/regions | Print basic source statistics.
[**software_version**](#software_version) | **get** /api2/json/softwareVersion | Get the current software version
[**taxonomy_classes**](#taxonomy_classes) | **get** /api2/json/taxonomyClasses/{classifierName} | Print the taxonomy classes valid for the given classifier.

# **anonymize**
<a id="anonymize"></a>
> APIKeyOut anonymize(sourceanonymizedtoken)

Activate/deactivate anonymization for a source.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
from openapi_client.model.api_key_out import APIKeyOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'source': "source_example",
        'anonymized': True,
        'token': "token_example",
    }
    try:
        # Activate/deactivate anonymization for a source.
        api_response = api_instance.anonymize(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->anonymize: %s\n" % e)
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
source | SourceSchema | | 
anonymized | AnonymizedSchema | | 
token | TokenSchema | | 

# SourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AnonymizedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#anonymize.ApiResponseFor200) | Anonymization of a source.
401 | [ApiResponseFor401](#anonymize.ApiResponseFor401) | Missing or incorrect API Key

#### anonymize.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIKeyOut**](../../models/APIKeyOut.md) |  | 


#### anonymize.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **anonymize1**
<a id="anonymize1"></a>
> anonymize1(sourceanonymized)

Activate/deactivate anonymization for a source.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'source': "source_example",
        'anonymized': True,
    }
    try:
        # Activate/deactivate anonymization for a source.
        api_response = api_instance.anonymize1(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->anonymize1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
source | SourceSchema | | 
anonymized | AnonymizedSchema | | 

# SourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AnonymizedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#anonymize1.ApiResponseFor200) | Anonymization of a source.
401 | [ApiResponseFor401](#anonymize1.ApiResponseFor401) | Missing or incorrect API Key

#### anonymize1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### anonymize1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_key_info**
<a id="api_key_info"></a>
> APIKeyOut api_key_info()

Read API Key info.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
from openapi_client.model.api_key_out import APIKeyOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Read API Key info.
        api_response = api_instance.api_key_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->api_key_info: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_key_info.ApiResponseFor200) | Read API Key (uncached, i.e. DB read)
401 | [ApiResponseFor401](#api_key_info.ApiResponseFor401) | Missing or incorrect API Key

#### api_key_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIKeyOut**](../../models/APIKeyOut.md) |  | 


#### api_key_info.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_status**
<a id="api_status"></a>
> APIClassifiersStatusOut api_status()

Prints the current status of the classifiers. A classifier name in apiStatus corresponds to a service name in apiServices.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
from openapi_client.model.api_classifiers_status_out import APIClassifiersStatusOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Prints the current status of the classifiers. A classifier name in apiStatus corresponds to a service name in apiServices.
        api_response = api_instance.api_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->api_status: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_status.ApiResponseFor200) | Available classifiers and status
401 | [ApiResponseFor401](#api_status.ApiResponseFor401) | Missing or incorrect token

#### api_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIClassifiersStatusOut**](../../models/APIClassifiersStatusOut.md) |  | 


#### api_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_usage**
<a id="api_usage"></a>
> APIPeriodUsageOut api_usage()

Print current API usage.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
from openapi_client.model.api_period_usage_out import APIPeriodUsageOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Print current API usage.
        api_response = api_instance.api_usage()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->api_usage: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_usage.ApiResponseFor200) | Print current API usage.
401 | [ApiResponseFor401](#api_usage.ApiResponseFor401) | Missing or incorrect API Key

#### api_usage.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIPeriodUsageOut**](../../models/APIPeriodUsageOut.md) |  | 


#### api_usage.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_usage_history**
<a id="api_usage_history"></a>
> APIUsageHistoryOut api_usage_history()

Print historical API usage.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
from openapi_client.model.api_usage_history_out import APIUsageHistoryOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Print historical API usage.
        api_response = api_instance.api_usage_history()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->api_usage_history: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_usage_history.ApiResponseFor200) | Print historical API usage (NB. new output format form v2.0.15)
401 | [ApiResponseFor401](#api_usage_history.ApiResponseFor401) | Missing or incorrect API Key

#### api_usage_history.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIUsageHistoryOut**](../../models/APIUsageHistoryOut.md) |  | 


#### api_usage_history.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_usage_history_aggregate**
<a id="api_usage_history_aggregate"></a>
> APIUsageAggregatedOut api_usage_history_aggregate()

Print historical API usage (in an aggregated view, by service, by day/hour/min).

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
from openapi_client.model.api_usage_aggregated_out import APIUsageAggregatedOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Print historical API usage (in an aggregated view, by service, by day/hour/min).
        api_response = api_instance.api_usage_history_aggregate()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->api_usage_history_aggregate: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_usage_history_aggregate.ApiResponseFor200) | Print historical API usage.
401 | [ApiResponseFor401](#api_usage_history_aggregate.ApiResponseFor401) | Missing or incorrect API Key

#### api_usage_history_aggregate.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIUsageAggregatedOut**](../../models/APIUsageAggregatedOut.md) |  | 


#### api_usage_history_aggregate.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **available_services**
<a id="available_services"></a>
> APIServicesOut available_services()

List of classification services and usage cost in Units per classification (default is 1=ONE Unit). Some API endpoints (ex. Corridor) combine multiple classifiers.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
from openapi_client.model.api_services_out import APIServicesOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List of classification services and usage cost in Units per classification (default is 1=ONE Unit). Some API endpoints (ex. Corridor) combine multiple classifiers.
        api_response = api_instance.available_services()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->available_services: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#available_services.ApiResponseFor200) | Available services
401 | [ApiResponseFor401](#available_services.ApiResponseFor401) | Missing or incorrect token

#### available_services.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIServicesOut**](../../models/APIServicesOut.md) |  | 


#### available_services.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **disable**
<a id="disable"></a>
> disable(sourcedisabled)

Activate/deactivate an API Key.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'source': "source_example",
        'disabled': True,
    }
    try:
        # Activate/deactivate an API Key.
        api_response = api_instance.disable(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->disable: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
source | SourceSchema | | 
disabled | DisabledSchema | | 

# SourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DisabledSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#disable.ApiResponseFor200) | Disabled the API Key.
401 | [ApiResponseFor401](#disable.ApiResponseFor401) | Missing or incorrect API Key

#### disable.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### disable.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **learnable**
<a id="learnable"></a>
> APIKeyOut learnable(sourcelearnabletoken)

Activate/deactivate learning from a source.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
from openapi_client.model.api_key_out import APIKeyOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'source': "source_example",
        'learnable': True,
        'token': "token_example",
    }
    try:
        # Activate/deactivate learning from a source.
        api_response = api_instance.learnable(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->learnable: %s\n" % e)
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
source | SourceSchema | | 
learnable | LearnableSchema | | 
token | TokenSchema | | 

# SourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LearnableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#learnable.ApiResponseFor200) | Set learning from source.
401 | [ApiResponseFor401](#learnable.ApiResponseFor401) | Missing or incorrect API Key

#### learnable.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIKeyOut**](../../models/APIKeyOut.md) |  | 


#### learnable.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **learnable1**
<a id="learnable1"></a>
> learnable1(sourcelearnable)

Activate/deactivate learning from a source.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'source': "source_example",
        'learnable': True,
    }
    try:
        # Activate/deactivate learning from a source.
        api_response = api_instance.learnable1(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->learnable1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
source | SourceSchema | | 
learnable | LearnableSchema | | 

# SourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LearnableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#learnable1.ApiResponseFor200) | Set learning from source.
401 | [ApiResponseFor401](#learnable1.ApiResponseFor401) | Missing or incorrect API Key

#### learnable1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### learnable1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **regions**
<a id="regions"></a>
> RegionOut regions()

Print basic source statistics.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
from openapi_client.model.region_out import RegionOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Print basic source statistics.
        api_response = api_instance.regions()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->regions: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#regions.ApiResponseFor200) | List of countries and regions.
401 | [ApiResponseFor401](#regions.ApiResponseFor401) | Missing or incorrect API Key

#### regions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RegionOut**](../../models/RegionOut.md) |  | 


#### regions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **software_version**
<a id="software_version"></a>
> SoftwareVersionOut software_version()

Get the current software version

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
from openapi_client.model.software_version_out import SoftwareVersionOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the current software version
        api_response = api_instance.software_version()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->software_version: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#software_version.ApiResponseFor200) | The current software version
401 | [ApiResponseFor401](#software_version.ApiResponseFor401) | Missing or incorrect token

#### software_version.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SoftwareVersionOut**](../../models/SoftwareVersionOut.md) |  | 


#### software_version.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **taxonomy_classes**
<a id="taxonomy_classes"></a>
> APIClassifierTaxonomyOut taxonomy_classes(classifier_name)

Print the taxonomy classes valid for the given classifier.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import admin_api
from openapi_client.model.api_classifier_taxonomy_out import APIClassifierTaxonomyOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'classifierName': "classifierName_example",
    }
    try:
        # Print the taxonomy classes valid for the given classifier.
        api_response = api_instance.taxonomy_classes(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminApi->taxonomy_classes: %s\n" % e)
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
classifierName | ClassifierNameSchema | | 

# ClassifierNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#taxonomy_classes.ApiResponseFor200) | Available plans
401 | [ApiResponseFor401](#taxonomy_classes.ApiResponseFor401) | Missing or incorrect token

#### taxonomy_classes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIClassifierTaxonomyOut**](../../models/APIClassifierTaxonomyOut.md) |  | 


#### taxonomy_classes.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

