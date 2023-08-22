# openapi_client.model.api_counter_v2_out.APICounterV2Out

Detailed usage as reported by the deduplicating API counter.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Detailed usage as reported by the deduplicating API counter. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**apiKey** | [**APIKeyOut**](APIKeyOut.md) | [**APIKeyOut**](APIKeyOut.md) |  | [optional] 
**apiService** | str,  | str,  | The apiService corresponds to the classifier name. | [optional] 
**hostAddress** | str,  | str,  | The processing hostAddress. | [optional] 
**createdDateTime** | decimal.Decimal, int,  | decimal.Decimal,  | The create datetime of the counter. | [optional] value must be a 64 bit integer
**totalUsage** | decimal.Decimal, int,  | decimal.Decimal,  | The usage of the counter. | [optional] value must be a 64 bit integer
**lastFlushedDateTime** | decimal.Decimal, int,  | decimal.Decimal,  | The flush datetime of the counter. | [optional] value must be a 64 bit integer
**lastUsedDateTime** | decimal.Decimal, int,  | decimal.Decimal,  | The last usage datetime of the counter. | [optional] value must be a 64 bit integer
**[serviceFeaturesUsage](#serviceFeaturesUsage)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Usage of special features, such as Chinese, Japanese. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# serviceFeaturesUsage

Usage of special features, such as Chinese, Japanese.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Usage of special features, such as Chinese, Japanese. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | decimal.Decimal, int,  | decimal.Decimal,  | any string name can be used but the value must be the correct type Usage of special features, such as Chinese, Japanese. | [optional] value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

