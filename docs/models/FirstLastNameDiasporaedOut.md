# openapi_client.model.first_last_name_diasporaed_out.FirstLastNameDiasporaedOut

Represents the output of inferring the LIKELY ethnicity from a personal name, given an country of residence.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents the output of inferring the LIKELY ethnicity from a personal name, given an country of residence. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**script** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**explanation** | str,  | str,  |  | [optional] 
**firstName** | str,  | str,  | The first name (also known as given name) | [optional] 
**lastName** | str,  | str,  | The last name (also known as family name, or surname) | [optional] 
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  | Compatibility to NamSor_v1 Diaspora score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] value must be a 64 bit float
**ethnicityAlt** | str,  | str,  | The second best alternative ethnicity | [optional] 
**ethnicity** | str,  | str,  | The most likely ethnicity | [optional] 
**lifted** | bool,  | BoolClass,  | Indicates if the output ethnicity is based on machine learning only, or further lifted as a known fact by a country-specific rule. Let us know if you believe ethnicity is incorrect on a specific case where lifted is true. | [optional] 
**countryIso2** | str,  | str,  | From input data, the countryIso2 of geographic context (US,CA etc.) | [optional] 
**[ethnicitiesTop](#ethnicitiesTop)** | list, tuple,  | tuple,  | List most likely ethnicities (top 10) | [optional] 
**probabilityCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for ethnicity to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**probabilityAltCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for ethnicity OR ethnicityAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**[religionStats](#religionStats)** | list, tuple,  | tuple,  | Geographic religious statistics, assuming ethnicity is correctly predicted. | [optional] 
**[religionStatsAlt](#religionStatsAlt)** | list, tuple,  | tuple,  | Geographic religious statistics, assuming ethnicity OR best alternative is correctly predicted. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ethnicitiesTop

List most likely ethnicities (top 10)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List most likely ethnicities (top 10) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List most likely ethnicities (top 10) | 

# religionStats

Geographic religious statistics, assuming ethnicity is correctly predicted.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Geographic religious statistics, assuming ethnicity is correctly predicted. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReligionStatOut**](ReligionStatOut.md) | [**ReligionStatOut**](ReligionStatOut.md) | [**ReligionStatOut**](ReligionStatOut.md) |  | 

# religionStatsAlt

Geographic religious statistics, assuming ethnicity OR best alternative is correctly predicted.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Geographic religious statistics, assuming ethnicity OR best alternative is correctly predicted. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReligionStatOut**](ReligionStatOut.md) | [**ReligionStatOut**](ReligionStatOut.md) | [**ReligionStatOut**](ReligionStatOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

