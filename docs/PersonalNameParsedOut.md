# PersonalNameParsedOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**name** | **str** | The input name | [optional] 
**name_parser_type** | **str** | Name parsing is addressed as a classification problem, for example FN1LN1 means a first then last name order. | [optional] 
**name_parser_type_alt** | **str** | Second best alternative parsing. Name parsing is addressed as a classification problem, for example FN1LN1 means a first then last name order. | [optional] 
**first_last_name** | [**FirstLastNameOut**](FirstLastNameOut.md) |  | [optional] 
**score** | **float** | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


