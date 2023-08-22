# openapi_client.model.api_billing_period_usage_out.APIBillingPeriodUsageOut

The current billing period.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The current billing period. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**apiKey** | str,  | str,  | User API Key. | [optional] 
**subscriptionStarted** | decimal.Decimal, int,  | decimal.Decimal,  | Datetime when the user subscribed to the plan. | [optional] value must be a 64 bit integer
**periodStarted** | decimal.Decimal, int,  | decimal.Decimal,  | Datetime when the the plan&#x27;s current period started. | [optional] value must be a 64 bit integer
**periodEnded** | decimal.Decimal, int,  | decimal.Decimal,  | Datetime when the the plan&#x27;s current period endend. | [optional] value must be a 64 bit integer
**stripeCurrentPeriodEnd** | decimal.Decimal, int,  | decimal.Decimal,  | Datetime when the the plan&#x27;s current period endend (in Stripe). Internal and Stripe periodicity should ~coincide. | [optional] value must be a 64 bit integer
**stripeCurrentPeriodStart** | decimal.Decimal, int,  | decimal.Decimal,  | Datetime when the the plan&#x27;s current period started (in Stripe). Internal and Stripe periodicity should ~coincide. | [optional] value must be a 64 bit integer
**billingStatus** | str,  | str,  | Current period billing status ex OPEN. | [optional] 
**usage** | decimal.Decimal, int,  | decimal.Decimal,  | Current period usage in units (NB some API endpoints use more than one unit). | [optional] value must be a 64 bit integer
**softLimit** | decimal.Decimal, int,  | decimal.Decimal,  | Current period soft limit (reaching the limit sends an email notification). | [optional] value must be a 64 bit integer
**hardLimit** | decimal.Decimal, int,  | decimal.Decimal,  | Current period hard limit (reaching the limit sends an email notification and blocks the API Key). | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

