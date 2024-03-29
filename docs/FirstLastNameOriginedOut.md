# FirstLastNameOriginedOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**first_name** | **str** | The first name (also known as given name) | [optional] 
**last_name** | **str** | The last name (also known as family name, or surname) | [optional] 
**country_origin** | **str** | Most likely country of Origin | [optional] 
**country_origin_alt** | **str** | Second best alternative : country of Origin | [optional] 
**countries_origin_top** | **list[str]** | List countries of Origin (top 10) | [optional] 
**score** | **float** | Compatibility to NamSor_v1 Origin score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**region_origin** | **str** | Most likely region of Origin (based on countryOrigin ISO2 code) | [optional] 
**top_region_origin** | **str** | Most likely top region of Origin (based on countryOrigin ISO2 code) | [optional] 
**sub_region_origin** | **str** | Most likely sub region of Origin (based on countryOrigin ISO2 code) | [optional] 
**probability_calibrated** | **float** | The calibrated probability for countryOrigin to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**probability_alt_calibrated** | **float** | The calibrated probability for countryOrigin OR countryOriginAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**religion_stats** | [**list[ReligionStatOut]**](ReligionStatOut.md) | Geographic religious statistics, assuming country of origin is correctly predicted. | [optional] 
**religion_stats_alt** | [**list[ReligionStatOut]**](ReligionStatOut.md) | Geographic religious statistics, assuming country of origin OR best alternative is correctly predicted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


