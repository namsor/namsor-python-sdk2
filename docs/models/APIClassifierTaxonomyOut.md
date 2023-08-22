# openapi_client.model.api_classifier_taxonomy_out.APIClassifierTaxonomyOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**classifierName** | str,  | str,  | Name of the classifier as per apiStatus (corresponds also to the name of the service in apiServices) | [optional] 
**[taxonomyClasses](#taxonomyClasses)** | list, tuple,  | tuple,  | The taxonomy classes this classifier classifies to | [optional] 
**[classifyingScripts](#classifyingScripts)** | list, tuple,  | tuple,  | The scripts / alphabets this classifiers classifies to | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# taxonomyClasses

The taxonomy classes this classifier classifies to

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The taxonomy classes this classifier classifies to | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The taxonomy classes this classifier classifies to | 

# classifyingScripts

The scripts / alphabets this classifiers classifies to

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The scripts / alphabets this classifiers classifies to | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The scripts / alphabets this classifiers classifies to | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

