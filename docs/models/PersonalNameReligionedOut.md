# openapi_client.model.personal_name_religioned_out.PersonalNameReligionedOut

religious-coded names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | religious-coded names | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**script** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**explanation** | str,  | str,  |  | [optional] 
**name** | str,  | str,  | The input name. | [optional] 
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] value must be a 64 bit float
**religion** | str,  | str,  | Most likely religion | [optional] 
**religionAlt** | str,  | str,  | Second best alternative : religion  | [optional] 
**[religionsTop](#religionsTop)** | list, tuple,  | tuple,  | List countries (top 10) | [optional] 
**probabilityCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for country to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**probabilityAltCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for country OR countryAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# religionsTop

List countries (top 10)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List countries (top 10) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List countries (top 10) | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

