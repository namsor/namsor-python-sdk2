# PersonalNameGeoSubclassificationOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**name** | **str** | The input name | [optional] 
**country_iso2** | **str** | The input country ISO2 code | [optional] 
**sub_classification** | **str** | Most likely subclassification ISO_3166-2 code | [optional] 
**sub_classification_alt** | **str** | Second best alternative : subclassification ISO_3166-2 code | [optional] 
**subclassification_top** | **list[str]** | List subclassification ISO_3166-2 codes (top 10) | [optional] 
**score** | **float** | Compatibility to NamSor_v1 Origin score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**probability_calibrated** | **float** | The calibrated probability for subclassification to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**probability_alt_calibrated** | **float** | The calibrated probability for subclassification OR subclassificationAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


