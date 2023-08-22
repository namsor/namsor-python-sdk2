# openapi_client.model.personal_name_geo_out.PersonalNameGeoOut

Classified geo names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Classified geo names | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**script** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**explanation** | str,  | str,  |  | [optional] 
**name** | str,  | str,  | The input name. | [optional] 
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] value must be a 64 bit float
**country** | str,  | str,  | Most likely country  | [optional] 
**countryAlt** | str,  | str,  | Second best alternative : country  | [optional] 
**region** | str,  | str,  | Most likely region (based on country ISO2 code) | [optional] 
**topRegion** | str,  | str,  | Most likely top region (based on country ISO2 code) | [optional] 
**subRegion** | str,  | str,  | Most likely sub region (based on country ISO2 code) | [optional] 
**[countriesTop](#countriesTop)** | list, tuple,  | tuple,  | List countries (top 10) | [optional] 
**probabilityCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for country to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**probabilityAltCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for country OR countryAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**[religionStats](#religionStats)** | list, tuple,  | tuple,  | Geographic religious statistics, assuming country is correctly predicted. | [optional] 
**[religionStatsAlt](#religionStatsAlt)** | list, tuple,  | tuple,  | Geographic religious statistics, assuming country OR best alternative is correctly predicted. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# countriesTop

List countries (top 10)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List countries (top 10) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List countries (top 10) | 

# religionStats

Geographic religious statistics, assuming country is correctly predicted.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Geographic religious statistics, assuming country is correctly predicted. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReligionStatOut**](ReligionStatOut.md) | [**ReligionStatOut**](ReligionStatOut.md) | [**ReligionStatOut**](ReligionStatOut.md) |  | 

# religionStatsAlt

Geographic religious statistics, assuming country OR best alternative is correctly predicted.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Geographic religious statistics, assuming country OR best alternative is correctly predicted. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReligionStatOut**](ReligionStatOut.md) | [**ReligionStatOut**](ReligionStatOut.md) | [**ReligionStatOut**](ReligionStatOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

