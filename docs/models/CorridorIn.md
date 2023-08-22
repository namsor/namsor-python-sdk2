# openapi_client.model.corridor_in.CorridorIn

Represent any transnational interaction between names (ex. remittance, communication, cross-border investment, airline travel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represent any transnational interaction between names (ex. remittance, communication, cross-border investment, airline travel | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**firstLastNameGeoFrom** | [**FirstLastNameGeoIn**](FirstLastNameGeoIn.md) | [**FirstLastNameGeoIn**](FirstLastNameGeoIn.md) |  | [optional] 
**firstLastNameGeoTo** | [**FirstLastNameGeoIn**](FirstLastNameGeoIn.md) | [**FirstLastNameGeoIn**](FirstLastNameGeoIn.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

