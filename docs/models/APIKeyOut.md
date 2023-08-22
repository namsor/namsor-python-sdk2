# openapi_client.model.api_key_out.APIKeyOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**apiKey** | str,  | str,  | The user API Key. | [optional] 
**userId** | str,  | str,  | The user identifier. | [optional] 
**admin** | bool,  | BoolClass,  | The API Key has admin role. | [optional] 
**vetted** | bool,  | BoolClass,  | The API Key is vetted (assumed truthful) for machine learning. | [optional] 
**learnable** | bool,  | BoolClass,  | The API Key is learnable (without assuming truthfulness) for machine learning. Set learnable&#x3D;false and anonymized&#x3D;true for highest privacy (ie. to forget data as it&#x27;s processed). | [optional] 
**anonymized** | bool,  | BoolClass,  | The API Key is anonymized (using SHA-252 digest for logging). Set learnable&#x3D;false and anonymized&#x3D;true for highest privacy (ie. to forget data as it&#x27;s processed). | [optional] 
**partner** | bool,  | BoolClass,  | The API Key has partner role. | [optional] 
**striped** | bool,  | BoolClass,  | The API Key is associated to a valid Stripe account. | [optional] 
**corporate** | bool,  | BoolClass,  | The API Key has role corporate (ex SWIFT payments instead of Stripe payments). | [optional] 
**disabled** | bool,  | BoolClass,  | The API Key is temporarily or permanently disabled. | [optional] 
**explainable** | bool,  | BoolClass,  | The API Key supports the AI explainability option (may require a specific license). | [optional] 
**ipAddress** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

