# openapi_client.model.personal_name_parsed_out.PersonalNameParsedOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**script** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**explanation** | str,  | str,  |  | [optional] 
**name** | str,  | str,  | The input name | [optional] 
**nameParserType** | str,  | str,  | Name parsing is addressed as a classification problem, for example FN1LN1 means a first then last name order. | [optional] must be one of ["FN1LN1", "LN1FN1", "FN1LN2", "LN2FN1", "FN1LNx", "LNxFN1", "FN2LN1", "LN1FN2", "FN2LN2", "LN2FN2", "FN2LNx", "LNxFN2", "FNxLN1", "LN1FNx", "FNxLN2", "LN2FNx", "FNxLNx", "LNxFNx", ] 
**nameParserTypeAlt** | str,  | str,  | Second best alternative parsing. Name parsing is addressed as a classification problem, for example FN1LN1 means a first then last name order. | [optional] must be one of ["FN1LN1", "LN1FN1", "FN1LN2", "LN2FN1", "FN1LNx", "LNxFN1", "FN2LN1", "LN1FN2", "FN2LN2", "LN2FN2", "FN2LNx", "LNxFN2", "FNxLN1", "LN1FNx", "FNxLN2", "LN2FNx", "FNxLNx", "LNxFNx", ] 
**firstLastName** | [**FirstLastNameOut**](FirstLastNameOut.md) | [**FirstLastNameOut**](FirstLastNameOut.md) |  | [optional] 
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

