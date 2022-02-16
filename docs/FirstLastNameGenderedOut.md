# FirstLastNameGenderedOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**first_name** | **str** | The first name (also known as given name) | [optional] 
**last_name** | **str** | The last name (also known as family name, or surname) | [optional] 
**likely_gender** | **str** | Most likely gender | [optional] 
**gender_scale** | **float** | Compatibility to NamSor_v1 Gender Scale M[-1..U..+1]F value. | [optional] 
**score** | **float** | Compatibility to NamSor_v1 Gender score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**probability_calibrated** | **float** | The calibrated probability for inferred gender to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


