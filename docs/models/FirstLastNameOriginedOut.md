# openapi_client.model.first_last_name_origined_out.FirstLastNameOriginedOut

Represents the output of inferring the LIKELY country of Origin from a personal name.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents the output of inferring the LIKELY country of Origin from a personal name. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**script** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**explanation** | str,  | str,  |  | [optional] 
**firstName** | str,  | str,  | The first name (also known as given name) | [optional] 
**lastName** | str,  | str,  | The last name (also known as family name, or surname) | [optional] 
**countryOrigin** | str,  | str,  | Most likely country of Origin | [optional] 
**countryOriginAlt** | str,  | str,  | Second best alternative : country of Origin | [optional] 
**[countriesOriginTop](#countriesOriginTop)** | list, tuple,  | tuple,  | List countries of Origin (top 10) | [optional] 
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  | Compatibility to NamSor_v1 Origin score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] value must be a 64 bit float
**regionOrigin** | str,  | str,  | Most likely region of Origin (based on countryOrigin ISO2 code) | [optional] 
**topRegionOrigin** | str,  | str,  | Most likely top region of Origin (based on countryOrigin ISO2 code) | [optional] 
**subRegionOrigin** | str,  | str,  | Most likely sub region of Origin (based on countryOrigin ISO2 code) | [optional] 
**probabilityCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for countryOrigin to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**probabilityAltCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for countryOrigin OR countryOriginAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**[religionStats](#religionStats)** | list, tuple,  | tuple,  | Geographic religious statistics, assuming country of origin is correctly predicted. | [optional] 
**[religionStatsAlt](#religionStatsAlt)** | list, tuple,  | tuple,  | Geographic religious statistics, assuming country of origin OR best alternative is correctly predicted. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# countriesOriginTop

List countries of Origin (top 10)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List countries of Origin (top 10) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List countries of Origin (top 10) | 

# religionStats

Geographic religious statistics, assuming country of origin is correctly predicted.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Geographic religious statistics, assuming country of origin is correctly predicted. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReligionStatOut**](ReligionStatOut.md) | [**ReligionStatOut**](ReligionStatOut.md) | [**ReligionStatOut**](ReligionStatOut.md) |  | 

# religionStatsAlt

Geographic religious statistics, assuming country of origin OR best alternative is correctly predicted.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Geographic religious statistics, assuming country of origin OR best alternative is correctly predicted. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReligionStatOut**](ReligionStatOut.md) | [**ReligionStatOut**](ReligionStatOut.md) | [**ReligionStatOut**](ReligionStatOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

