# openapi_client.model.api_service_out.APIServiceOut

List of API Services

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List of API Services | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**serviceName** | str,  | str,  | A service name corresponds to classifier name in apiStatus (ex. personalname_gender or personalfullname_gender) | [optional] 
**serviceGroup** | str,  | str,  | Groups together classifiers providing a similar service (ex. gender groups personalname_gender and personalfullname_gender) | [optional] 
**costInUnits** | decimal.Decimal, int,  | decimal.Decimal,  | Indicates how many units per call this service costs (ex. the number of units per name) | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

