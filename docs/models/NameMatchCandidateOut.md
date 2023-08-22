# openapi_client.model.name_match_candidate_out.NameMatchCandidateOut

The ordered list of name matching candidates

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The ordered list of name matching candidates | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**candidateName** | str,  | str,  | The name matching candidate name | [optional] 
**probability** | decimal.Decimal, int, float,  | decimal.Decimal,  | The name matching estimated probability. | [optional] value must be a 64 bit float
**predScoreGivenName** | decimal.Decimal, int, float,  | decimal.Decimal,  | The given name prediction score. | [optional] value must be a 64 bit float
**predScoreFamilyName** | decimal.Decimal, int, float,  | decimal.Decimal,  | The family name prediction score. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

