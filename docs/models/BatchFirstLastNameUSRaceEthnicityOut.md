# openapi_client.model.batch_first_last_name_us_race_ethnicity_out.BatchFirstLastNameUSRaceEthnicityOut

Represents the output of inferring the LIKELY US 'race/ethnicity' from a personal name, given US country of residence and (optionally) a ZIP5 code.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents the output of inferring the LIKELY US &#x27;race/ethnicity&#x27; from a personal name, given US country of residence and (optionally) a ZIP5 code. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[personalNames](#personalNames)** | list, tuple,  | tuple,  | Classified US &#x27;race&#x27;/ethnicized names | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# personalNames

Classified US 'race'/ethnicized names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Classified US &#x27;race&#x27;/ethnicized names | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FirstLastNameUSRaceEthnicityOut**](FirstLastNameUSRaceEthnicityOut.md) | [**FirstLastNameUSRaceEthnicityOut**](FirstLastNameUSRaceEthnicityOut.md) | [**FirstLastNameUSRaceEthnicityOut**](FirstLastNameUSRaceEthnicityOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

