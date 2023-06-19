# PersonalNameReligionedOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**name** | **str** | The input name. | [optional] 
**score** | **float** | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**religion** | **str** | Most likely religion | [optional] 
**religion_alt** | **str** | Second best alternative : religion  | [optional] 
**religions_top** | **list[str]** | List countries (top 10) | [optional] 
**probability_calibrated** | **float** | The calibrated probability for country to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**probability_alt_calibrated** | **float** | The calibrated probability for country OR countryAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


