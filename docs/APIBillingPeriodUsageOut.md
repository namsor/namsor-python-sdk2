# APIBillingPeriodUsageOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | User API Key. | [optional] 
**subscription_started** | **int** | Datetime when the user subscribed to the plan. | [optional] 
**period_started** | **int** | Datetime when the the plan&#39;s current period started. | [optional] 
**period_ended** | **int** | Datetime when the the plan&#39;s current period endend. | [optional] 
**stripe_current_period_end** | **int** | Datetime when the the plan&#39;s current period endend (in Stripe). Internal and Stripe periodicity should ~coincide. | [optional] 
**stripe_current_period_start** | **int** | Datetime when the the plan&#39;s current period started (in Stripe). Internal and Stripe periodicity should ~coincide. | [optional] 
**billing_status** | **str** | Current period billing status ex OPEN. | [optional] 
**usage** | **int** | Current period usage in units (NB some API endpoints use more than one unit). | [optional] 
**soft_limit** | **int** | Current period soft limit (reaching the limit sends an email notification). | [optional] 
**hard_limit** | **int** | Current period hard limit (reaching the limit sends an email notification and blocks the API Key). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


