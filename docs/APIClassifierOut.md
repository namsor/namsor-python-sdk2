# APIClassifierOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classifier_name** | **str** | The classifier name | [optional] 
**serving** | **bool** | True if the classifier is serving requests (has reached minimal learning, is not shutting down) | [optional] 
**learning** | **bool** | True if the classifier is learning | [optional] 
**shutting_down** | **bool** | True if the classifier is shutting down | [optional] 
**probability_calibrated** | **bool** | True if the classifier has finished the initial learning and calibrated probabilities (meanwhile, during initial learning, probabilities will be equal to -1) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


