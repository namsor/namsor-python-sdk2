# openapi_client.model.api_classifiers_status_out.APIClassifiersStatusOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**softwareVersion** | [**SoftwareVersionOut**](SoftwareVersionOut.md) | [**SoftwareVersionOut**](SoftwareVersionOut.md) |  | [optional] 
**[classifiers](#classifiers)** | list, tuple,  | tuple,  | The list of classifiers and versions. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# classifiers

The list of classifiers and versions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of classifiers and versions. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**APIClassifierOut**](APIClassifierOut.md) | [**APIClassifierOut**](APIClassifierOut.md) | [**APIClassifierOut**](APIClassifierOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

