# openapi_client.model.corridor_out.CorridorOut

Represent multiple classifications for corridor sender and receiver (gender, country, origin, diaspora)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represent multiple classifications for corridor sender and receiver (gender, country, origin, diaspora) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**FirstLastNameGenderedOut** | [**FirstLastNameGenderedOut**](FirstLastNameGenderedOut.md) | [**FirstLastNameGenderedOut**](FirstLastNameGenderedOut.md) |  | [optional] 
**FirstLastNameOriginedOut** | [**FirstLastNameOriginedOut**](FirstLastNameOriginedOut.md) | [**FirstLastNameOriginedOut**](FirstLastNameOriginedOut.md) |  | [optional] 
**FirstLastNameDiasporaedOut** | [**FirstLastNameDiasporaedOut**](FirstLastNameDiasporaedOut.md) | [**FirstLastNameDiasporaedOut**](FirstLastNameDiasporaedOut.md) |  | [optional] 
**script** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

