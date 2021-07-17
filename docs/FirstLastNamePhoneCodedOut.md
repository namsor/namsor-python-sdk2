# FirstLastNamePhoneCodedOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**first_name** | **str** | The first name (also known as given name) | [optional] 
**last_name** | **str** | The last name (also known as family name, or surname) | [optional] 
**international_phone_number_verified** | **str** | The normalized phone number, verified using libphonenumber. | [optional] 
**phone_country_iso2_verified** | **str** | The phone ISO2 country code, verified using libphonenumber. | [optional] 
**phone_country_code** | **int** | The phone country code of the phone number, verified using libphonenumber. | [optional] 
**phone_country_code_alt** | **int** | The best alternative phone country code of the phone number. | [optional] 
**phone_country_iso2** | **str** | The likely country of the phone number. | [optional] 
**phone_country_iso2_alt** | **str** | The best alternative country of the phone number. | [optional] 
**origin_country_iso2** | **str** | The likely country of origin of the name. | [optional] 
**origin_country_iso2_alt** | **str** | The best alternative country of origin of the name. | [optional] 
**phone_number** | **str** | The input phone number. | [optional] 
**verified** | **bool** | Indicates if the phone number could be positively verified using libphonenumber. | [optional] 
**score** | **float** | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**country_iso2** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


