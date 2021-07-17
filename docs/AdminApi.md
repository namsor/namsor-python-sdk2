# openapi_client.AdminApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anonymize**](AdminApi.md#anonymize) | **GET** /api2/json/anonymize/{source}/{anonymized} | Activate/deactivate anonymization for a source.
[**api_status**](AdminApi.md#api_status) | **GET** /api2/json/apiStatus | Prints the current status of the classifiers. A classifier name in apiStatus corresponds to a service name in apiServices.
[**api_usage**](AdminApi.md#api_usage) | **GET** /api2/json/apiUsage | Print current API usage.
[**api_usage_history**](AdminApi.md#api_usage_history) | **GET** /api2/json/apiUsageHistory | Print historical API usage.
[**api_usage_history_aggregate**](AdminApi.md#api_usage_history_aggregate) | **GET** /api2/json/apiUsageHistoryAggregate | Print historical API usage (in an aggregated view, by service, by day/hour/min).
[**available_services**](AdminApi.md#available_services) | **GET** /api2/json/apiServices | List of classification services and usage cost in Units per classification (default is 1&#x3D;ONE Unit). Some API endpoints (ex. Corridor) combine multiple classifiers.
[**disable**](AdminApi.md#disable) | **GET** /api2/json/disable/{source}/{disabled} | Activate/deactivate an API Key.
[**learnable**](AdminApi.md#learnable) | **GET** /api2/json/learnable/{source}/{learnable} | Activate/deactivate learning from a source.
[**software_version**](AdminApi.md#software_version) | **GET** /api2/json/softwareVersion | Get the current software version
[**taxonomy_classes**](AdminApi.md#taxonomy_classes) | **GET** /api2/json/taxonomyClasses/{classifierName} | Print the taxonomy classes valid for the given classifier.


# **anonymize**
> anonymize(source, anonymized)

Activate/deactivate anonymization for a source.

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
api_instance = openapi_client.AdminApi(openapi_client.ApiClient(configuration))
source = 'source_example' # str | 
anonymized = True # bool | 

try:
    # Activate/deactivate anonymization for a source.
    api_instance.anonymize(source, anonymized)
except ApiException as e:
    print("Exception when calling AdminApi->anonymize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  | 
 **anonymized** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_status**
> APIClassifiersStatusOut api_status()

Prints the current status of the classifiers. A classifier name in apiStatus corresponds to a service name in apiServices.

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
api_instance = openapi_client.AdminApi(openapi_client.ApiClient(configuration))

try:
    # Prints the current status of the classifiers. A classifier name in apiStatus corresponds to a service name in apiServices.
    api_response = api_instance.api_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->api_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIClassifiersStatusOut**](APIClassifiersStatusOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_usage**
> APIPeriodUsageOut api_usage()

Print current API usage.

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
api_instance = openapi_client.AdminApi(openapi_client.ApiClient(configuration))

try:
    # Print current API usage.
    api_response = api_instance.api_usage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->api_usage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIPeriodUsageOut**](APIPeriodUsageOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_usage_history**
> APIUsageHistoryOut api_usage_history()

Print historical API usage.

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
api_instance = openapi_client.AdminApi(openapi_client.ApiClient(configuration))

try:
    # Print historical API usage.
    api_response = api_instance.api_usage_history()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->api_usage_history: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIUsageHistoryOut**](APIUsageHistoryOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_usage_history_aggregate**
> APIUsageAggregatedOut api_usage_history_aggregate()

Print historical API usage (in an aggregated view, by service, by day/hour/min).

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
api_instance = openapi_client.AdminApi(openapi_client.ApiClient(configuration))

try:
    # Print historical API usage (in an aggregated view, by service, by day/hour/min).
    api_response = api_instance.api_usage_history_aggregate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->api_usage_history_aggregate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIUsageAggregatedOut**](APIUsageAggregatedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **available_services**
> APIServicesOut available_services()

List of classification services and usage cost in Units per classification (default is 1=ONE Unit). Some API endpoints (ex. Corridor) combine multiple classifiers.

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
api_instance = openapi_client.AdminApi(openapi_client.ApiClient(configuration))

try:
    # List of classification services and usage cost in Units per classification (default is 1=ONE Unit). Some API endpoints (ex. Corridor) combine multiple classifiers.
    api_response = api_instance.available_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->available_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIServicesOut**](APIServicesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable**
> disable(source, disabled)

Activate/deactivate an API Key.

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
api_instance = openapi_client.AdminApi(openapi_client.ApiClient(configuration))
source = 'source_example' # str | The API Key to set as enabled/disabled.
disabled = True # bool | 

try:
    # Activate/deactivate an API Key.
    api_instance.disable(source, disabled)
except ApiException as e:
    print("Exception when calling AdminApi->disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The API Key to set as enabled/disabled. | 
 **disabled** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learnable**
> learnable(source, learnable)

Activate/deactivate learning from a source.

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
api_instance = openapi_client.AdminApi(openapi_client.ApiClient(configuration))
source = 'source_example' # str | The API Key to set as learnable/non learnable.
learnable = True # bool | 

try:
    # Activate/deactivate learning from a source.
    api_instance.learnable(source, learnable)
except ApiException as e:
    print("Exception when calling AdminApi->learnable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The API Key to set as learnable/non learnable. | 
 **learnable** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_version**
> SoftwareVersionOut software_version()

Get the current software version

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
api_instance = openapi_client.AdminApi(openapi_client.ApiClient(configuration))

try:
    # Get the current software version
    api_response = api_instance.software_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->software_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SoftwareVersionOut**](SoftwareVersionOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taxonomy_classes**
> APIClassifierTaxonomyOut taxonomy_classes(classifier_name)

Print the taxonomy classes valid for the given classifier.

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
api_instance = openapi_client.AdminApi(openapi_client.ApiClient(configuration))
classifier_name = 'classifier_name_example' # str | 

try:
    # Print the taxonomy classes valid for the given classifier.
    api_response = api_instance.taxonomy_classes(classifier_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->taxonomy_classes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classifier_name** | **str**|  | 

### Return type

[**APIClassifierTaxonomyOut**](APIClassifierTaxonomyOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

