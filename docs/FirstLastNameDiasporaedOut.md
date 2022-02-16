# FirstLastNameDiasporaedOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**first_name** | **str** | The first name (also known as given name) | [optional] 
**last_name** | **str** | The last name (also known as family name, or surname) | [optional] 
**score** | **float** | Compatibility to NamSor_v1 Diaspora score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**ethnicity_alt** | **str** | The second best alternative ethnicity | [optional] 
**ethnicity** | **str** | The most likely ethnicity | [optional] 
**lifted** | **bool** | Indicates if the output ethnicity is based on machine learning only, or further lifted as a known fact by a country-specific rule. Let us know if you believe ethnicity is incorrect on a specific case where lifted is true. | [optional] 
**country_iso2** | **str** | From input data, the countryIso2 of geographic context (US,CA etc.) | [optional] 
**ethnicities_top** | **list[str]** | List most likely ethnicities (top 10) | [optional] 
**probability_calibrated** | **float** | The calibrated probability for ethnicity to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**probability_alt_calibrated** | **float** | The calibrated probability for ethnicity OR ethnicityAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


