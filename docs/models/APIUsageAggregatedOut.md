# openapi_client.model.api_usage_aggregated_out.APIUsageAggregatedOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timeUnit** | str,  | str,  | Time unit is DAY, WEEK or MONTH depending on prior usage | [optional] 
**periodStart** | decimal.Decimal, int,  | decimal.Decimal,  | Start datetime of the reporting period | [optional] value must be a 64 bit integer
**periodEnd** | decimal.Decimal, int,  | decimal.Decimal,  | End datetime of the reporting period | [optional] value must be a 64 bit integer
**totalUsage** | decimal.Decimal, int,  | decimal.Decimal,  | Total usage in the current period | [optional] value must be a 64 bit integer
**historyTruncated** | bool,  | BoolClass,  | If the history was truncaded due to data limit | [optional] 
**[data](#data)** | list, tuple,  | tuple,  | Data points : usage per DAY, WEEK or MONTH and per apiService | [optional] 
**[colHeaders](#colHeaders)** | list, tuple,  | tuple,  | apiServices as column headers  | [optional] 
**[rowHeaders](#rowHeaders)** | list, tuple,  | tuple,  | dates as row headers  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

Data points : usage per DAY, WEEK or MONTH and per apiService

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Data points : usage per DAY, WEEK or MONTH and per apiService | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  | Data points : usage per DAY, WEEK or MONTH and per apiService | 

# items

Data points : usage per DAY, WEEK or MONTH and per apiService

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Data points : usage per DAY, WEEK or MONTH and per apiService | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | Data points : usage per DAY, WEEK or MONTH and per apiService | value must be a 32 bit integer

# colHeaders

apiServices as column headers 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | apiServices as column headers  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | apiServices as column headers  | 

# rowHeaders

dates as row headers 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | dates as row headers  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | dates as row headers  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

