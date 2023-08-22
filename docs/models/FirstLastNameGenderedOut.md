# openapi_client.model.first_last_name_gendered_out.FirstLastNameGenderedOut

Represents the output of inferring the LIKELY gender from a personal name.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents the output of inferring the LIKELY gender from a personal name. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**script** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**explanation** | str,  | str,  |  | [optional] 
**firstName** | str,  | str,  | The first name (also known as given name) | [optional] 
**lastName** | str,  | str,  | The last name (also known as family name, or surname) | [optional] 
**likelyGender** | str,  | str,  | Most likely gender | [optional] must be one of ["male", "female", "unknown", ] 
**genderScale** | decimal.Decimal, int, float,  | decimal.Decimal,  | Compatibility to NamSor_v1 Gender Scale M[-1..U..+1]F value. | [optional] value must be a 64 bit float
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  | Compatibility to NamSor_v1 Gender score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] value must be a 64 bit float
**probabilityCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for inferred gender to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

