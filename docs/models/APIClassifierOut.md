# openapi_client.model.api_classifier_out.APIClassifierOut

The list of classifiers and versions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The list of classifiers and versions. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**classifierName** | str,  | str,  | The classifier name | [optional] 
**serving** | bool,  | BoolClass,  | True if the classifier is serving requests (has reached minimal learning, is not shutting down) | [optional] 
**learning** | bool,  | BoolClass,  | True if the classifier is learning | [optional] 
**shuttingDown** | bool,  | BoolClass,  | True if the classifier is shutting down | [optional] 
**probabilityCalibrated** | bool,  | BoolClass,  | True if the classifier has finished the initial learning and calibrated probabilities (meanwhile, during initial learning, probabilities will be equal to -1) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

