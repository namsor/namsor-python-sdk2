# APIPlanSubscriptionOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | User API Key. | [optional] 
**plan_started** | **int** | Datetime when the user subscribed to the current plan. | [optional] 
**prior_plan_started** | **int** | Datetime when the user subscribed to the prior plan. | [optional] 
**plan_ended** | **int** | Datetime when the user ended the plan. | [optional] 
**tax_rate** | **float** | Applicable tax rate for the plan. | [optional] 
**plan_name** | **str** | Current plan name. | [optional] 
**plan_base_fees_key** | **str** | Current plan key (as in Stripe product). | [optional] 
**plan_status** | **str** | Plan status. | [optional] 
**plan_quota** | **int** | Current plan quota in quantity of units (NB: some API use several units per name). | [optional] 
**price_usd** | **float** | Current plan monthly price expressed in USD (includes a free quota). | [optional] 
**price_overage_usd** | **float** | Current plan price for overages expressed in USD (extra price per unit above the free quota). | [optional] 
**price** | **float** | Current plan price for overages expressed in Currency (extra price per unit above the free quota). | [optional] 
**price_overage** | **float** | Current plan price for overages expressed in Currency (extra price per unit above the free quota). | [optional] 
**currency** | **str** | Current plan Currency for prices. | [optional] 
**currency_factor** | **float** | For USD, GBP, EUR - the factor is 1. | [optional] 
**stripe_customer_id** | **str** | Stripe customer identifier. | [optional] 
**stripe_status** | **str** | Stripe status ex active. | [optional] 
**stripe_subscription** | **str** | Stripe subscription identifier. | [optional] 
**user_id** | **str** | Internal user identifier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


