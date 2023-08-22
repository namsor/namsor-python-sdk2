# openapi_client.model.first_last_name_us_race_ethnicity_out.FirstLastNameUSRaceEthnicityOut

Represents the output of inferring the LIKELY US 'race/ethnicity' from a personal name, given US country of residence and (optionally) a ZIP5 code.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents the output of inferring the LIKELY US &#x27;race/ethnicity&#x27; from a personal name, given US country of residence and (optionally) a ZIP5 code. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**script** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**explanation** | str,  | str,  |  | [optional] 
**firstName** | str,  | str,  | The first name (also known as given name) | [optional] 
**lastName** | str,  | str,  | The last name (also known as family name, or surname) | [optional] 
**raceEthnicityAlt** | str,  | str,  | Second most likely US &#x27;race&#x27;/ethnicity | [optional] must be one of ["W_NL", "HL", "A", "B_NL", "AI_AN", "PI", ] 
**raceEthnicity** | str,  | str,  | Most likely US &#x27;race&#x27;/ethnicity | [optional] must be one of ["W_NL", "HL", "A", "B_NL", "AI_AN", "PI", ] 
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] value must be a 64 bit float
**[raceEthnicitiesTop](#raceEthnicitiesTop)** | list, tuple,  | tuple,  | List &#x27;race&#x27;/ethnicities | [optional] 
**probabilityCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for raceEthnicity to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**probabilityAltCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for raceEthnicity OR raceEthnicityAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# raceEthnicitiesTop

List 'race'/ethnicities

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List &#x27;race&#x27;/ethnicities | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List &#x27;race&#x27;/ethnicities | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

