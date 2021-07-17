# APIUsageAggregatedOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_unit** | **str** | Time unit is DAY, WEEK or MONTH depending on prior usage | [optional] 
**period_start** | **int** | Start datetime of the reporting period | [optional] 
**period_end** | **int** | End datetime of the reporting period | [optional] 
**total_usage** | **int** | Total usage in the current period | [optional] 
**history_truncated** | **bool** | If the history was truncaded due to data limit | [optional] 
**data** | **list[list[int]]** | Data points : usage per DAY, WEEK or MONTH and per apiService | [optional] 
**col_headers** | **list[str]** | apiServices as column headers  | [optional] 
**row_headers** | **list[str]** | dates as row headers  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


