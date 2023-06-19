# APIKeyOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | The user API Key. | [optional] 
**user_id** | **str** | The user identifier. | [optional] 
**admin** | **bool** | The API Key has admin role. | [optional] 
**vetted** | **bool** | The API Key is vetted (assumed truthful) for machine learning. | [optional] 
**learnable** | **bool** | The API Key is learnable (without assuming truthfulness) for machine learning. Set learnable&#x3D;false and anonymized&#x3D;true for highest privacy (ie. to forget data as it&#39;s processed). | [optional] 
**anonymized** | **bool** | The API Key is anonymized (using SHA-252 digest for logging). Set learnable&#x3D;false and anonymized&#x3D;true for highest privacy (ie. to forget data as it&#39;s processed). | [optional] 
**partner** | **bool** | The API Key has partner role. | [optional] 
**striped** | **bool** | The API Key is associated to a valid Stripe account. | [optional] 
**corporate** | **bool** | The API Key has role corporate (ex SWIFT payments instead of Stripe payments). | [optional] 
**disabled** | **bool** | The API Key is temporarily or permanently disabled. | [optional] 
**explainable** | **bool** | The API Key supports the AI explainability option (may require a specific license). | [optional] 
**ip_address** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


