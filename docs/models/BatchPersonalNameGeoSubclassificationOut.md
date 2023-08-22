# openapi_client.model.batch_personal_name_geo_subclassification_out.BatchPersonalNameGeoSubclassificationOut

Represents the output of inferring the LIKELY country subclassification (regional names).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents the output of inferring the LIKELY country subclassification (regional names). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[personalNames](#personalNames)** | list, tuple,  | tuple,  | Classified names at sub country level (region or state) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# personalNames

Classified names at sub country level (region or state)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Classified names at sub country level (region or state) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PersonalNameGeoSubclassificationOut**](PersonalNameGeoSubclassificationOut.md) | [**PersonalNameGeoSubclassificationOut**](PersonalNameGeoSubclassificationOut.md) | [**PersonalNameGeoSubclassificationOut**](PersonalNameGeoSubclassificationOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

