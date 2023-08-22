# openapi_client.model.api_plan_subscription_out.APIPlanSubscriptionOut

The API Plan governing the subscription.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The API Plan governing the subscription. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**apiKey** | str,  | str,  | User API Key. | [optional] 
**planStarted** | decimal.Decimal, int,  | decimal.Decimal,  | Datetime when the user subscribed to the current plan. | [optional] value must be a 64 bit integer
**priorPlanStarted** | decimal.Decimal, int,  | decimal.Decimal,  | Datetime when the user subscribed to the prior plan. | [optional] value must be a 64 bit integer
**planEnded** | decimal.Decimal, int,  | decimal.Decimal,  | Datetime when the user ended the plan. | [optional] value must be a 64 bit integer
**taxRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable tax rate for the plan. | [optional] value must be a 64 bit float
**planName** | str,  | str,  | Current plan name. | [optional] 
**planBaseFeesKey** | str,  | str,  | Current plan key (as in Stripe product). | [optional] 
**planStatus** | str,  | str,  | Plan status. | [optional] 
**planQuota** | decimal.Decimal, int,  | decimal.Decimal,  | Current plan quota in quantity of units (NB: some API use several units per name). | [optional] value must be a 64 bit integer
**priceUSD** | decimal.Decimal, int, float,  | decimal.Decimal,  | Current plan monthly price expressed in USD (includes a free quota). | [optional] value must be a 64 bit float
**priceOverageUSD** | decimal.Decimal, int, float,  | decimal.Decimal,  | Current plan price for overages expressed in USD (extra price per unit above the free quota). | [optional] value must be a 64 bit float
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Current plan price for overages expressed in Currency (extra price per unit above the free quota). | [optional] value must be a 64 bit float
**priceOverage** | decimal.Decimal, int, float,  | decimal.Decimal,  | Current plan price for overages expressed in Currency (extra price per unit above the free quota). | [optional] value must be a 64 bit float
**currency** | str,  | str,  | Current plan Currency for prices. | [optional] 
**currencyFactor** | decimal.Decimal, int, float,  | decimal.Decimal,  | For USD, GBP, EUR - the factor is 1. | [optional] value must be a 64 bit float
**stripeCustomerId** | str,  | str,  | Stripe customer identifier. | [optional] 
**stripeStatus** | str,  | str,  | Stripe status ex active. | [optional] 
**stripeSubscription** | str,  | str,  | Stripe subscription identifier. | [optional] 
**userId** | str,  | str,  | Internal user identifier. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

