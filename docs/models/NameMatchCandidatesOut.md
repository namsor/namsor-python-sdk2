# openapi_client.model.name_match_candidates_out.NameMatchCandidatesOut

Classified matched names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Classified matched names | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**script** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**explanation** | str,  | str,  |  | [optional] 
**firstName** | str,  | str,  | The first name (also known as given name) | [optional] 
**lastName** | str,  | str,  | The last name (also known as family name, or surname) | [optional] 
**orderOption** | str,  | str,  | The option for ordering | [optional] 
**[matchCandidates](#matchCandidates)** | list, tuple,  | tuple,  | The ordered list of name matching candidates | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# matchCandidates

The ordered list of name matching candidates

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The ordered list of name matching candidates | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NameMatchCandidateOut**](NameMatchCandidateOut.md) | [**NameMatchCandidateOut**](NameMatchCandidateOut.md) | [**NameMatchCandidateOut**](NameMatchCandidateOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

