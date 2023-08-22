# openapi_client.model.first_last_name_phone_coded_out.FirstLastNamePhoneCodedOut

Represents the output of inferring the LIKELY country and phone code from a personal name and phone number.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents the output of inferring the LIKELY country and phone code from a personal name and phone number. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**script** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**explanation** | str,  | str,  |  | [optional] 
**firstName** | str,  | str,  | The first name (also known as given name) | [optional] 
**lastName** | str,  | str,  | The last name (also known as family name, or surname) | [optional] 
**internationalPhoneNumberVerified** | str,  | str,  | The normalized phone number, verified using libphonenumber. | [optional] 
**phoneCountryIso2Verified** | str,  | str,  | The phone ISO2 country code, verified using libphonenumber. | [optional] 
**phoneCountryCode** | decimal.Decimal, int,  | decimal.Decimal,  | The phone country code of the phone number, verified using libphonenumber. | [optional] value must be a 32 bit integer
**phoneCountryCodeAlt** | decimal.Decimal, int,  | decimal.Decimal,  | The best alternative phone country code of the phone number. | [optional] value must be a 32 bit integer
**phoneCountryIso2** | str,  | str,  | The likely country of the phone number. | [optional] 
**phoneCountryIso2Alt** | str,  | str,  | The best alternative country of the phone number. | [optional] 
**originCountryIso2** | str,  | str,  | The likely country of origin of the name. | [optional] 
**originCountryIso2Alt** | str,  | str,  | The best alternative country of origin of the name. | [optional] 
**phoneNumber** | str,  | str,  | The input phone number. | [optional] 
**verified** | bool,  | BoolClass,  | Indicates if the phone number could be positively verified using libphonenumber. | [optional] 
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] value must be a 64 bit float
**countryIso2** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

