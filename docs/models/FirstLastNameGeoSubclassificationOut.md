# openapi_client.model.first_last_name_geo_subclassification_out.FirstLastNameGeoSubclassificationOut

Represents the geographic name origin at a country subclassification level (usually regional or state level).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents the geographic name origin at a country subclassification level (usually regional or state level). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**script** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**explanation** | str,  | str,  |  | [optional] 
**firstName** | str,  | str,  | The first name (also known as given name) | [optional] 
**lastName** | str,  | str,  | The last name (also known as family name, or surname) | [optional] 
**countryIso2** | str,  | str,  | The input country ISO2 code | [optional] 
**subClassification** | str,  | str,  | Most likely subclassification ISO_3166-2 code | [optional] 
**subClassificationAlt** | str,  | str,  | Second best alternative : subclassification ISO_3166-2 code | [optional] 
**[subclassificationTop](#subclassificationTop)** | list, tuple,  | tuple,  | List subclassification ISO_3166-2 codes (top 10) | [optional] 
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  | Compatibility to NamSor_v1 Origin score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] value must be a 64 bit float
**probabilityCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for subclassification to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**probabilityAltCalibrated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calibrated probability for subclassification OR subclassificationAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subclassificationTop

List subclassification ISO_3166-2 codes (top 10)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List subclassification ISO_3166-2 codes (top 10) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List subclassification ISO_3166-2 codes (top 10) | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

