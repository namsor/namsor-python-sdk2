# openapi_client.model.batch_first_last_name_gendered_out.BatchFirstLastNameGenderedOut

Represents the output of inferring the LIKELY gender from a list of personal names.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents the output of inferring the LIKELY gender from a list of personal names. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[personalNames](#personalNames)** | list, tuple,  | tuple,  | Classified genderized names | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# personalNames

Classified genderized names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Classified genderized names | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FirstLastNameGenderedOut**](FirstLastNameGenderedOut.md) | [**FirstLastNameGenderedOut**](FirstLastNameGenderedOut.md) | [**FirstLastNameGenderedOut**](FirstLastNameGenderedOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

