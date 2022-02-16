# PersonalNameGeoOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | The input name. | [optional] 
**score** | **float** | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**country** | **str** | Most likely country  | [optional] 
**country_alt** | **str** | Second best alternative : country  | [optional] 
**region** | **str** | Most likely region (based on country ISO2 code) | [optional] 
**top_region** | **str** | Most likely top region (based on country ISO2 code) | [optional] 
**sub_region** | **str** | Most likely sub region (based on country ISO2 code) | [optional] 
**countries_top** | **list[str]** | List countries (top 10) | [optional] 
**probability_calibrated** | **float** | The calibrated probability for country to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**probability_alt_calibrated** | **float** | The calibrated probability for country OR countryAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


