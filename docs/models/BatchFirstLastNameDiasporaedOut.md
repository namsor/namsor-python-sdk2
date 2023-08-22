# openapi_client.model.batch_first_last_name_diasporaed_out.BatchFirstLastNameDiasporaedOut

Represents the output of inferring the LIKELY ethnicity from a personal name, given an country of residence.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents the output of inferring the LIKELY ethnicity from a personal name, given an country of residence. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[personalNames](#personalNames)** | list, tuple,  | tuple,  | Classified diaspora names | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# personalNames

Classified diaspora names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Classified diaspora names | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FirstLastNameDiasporaedOut**](FirstLastNameDiasporaedOut.md) | [**FirstLastNameDiasporaedOut**](FirstLastNameDiasporaedOut.md) | [**FirstLastNameDiasporaedOut**](FirstLastNameDiasporaedOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

