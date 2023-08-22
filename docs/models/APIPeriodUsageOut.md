# openapi_client.model.api_period_usage_out.APIPeriodUsageOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**subscription** | [**APIPlanSubscriptionOut**](APIPlanSubscriptionOut.md) | [**APIPlanSubscriptionOut**](APIPlanSubscriptionOut.md) |  | [optional] 
**billingPeriod** | [**APIBillingPeriodUsageOut**](APIBillingPeriodUsageOut.md) | [**APIBillingPeriodUsageOut**](APIBillingPeriodUsageOut.md) |  | [optional] 
**overageExclTax** | decimal.Decimal, int, float,  | decimal.Decimal,  | Overage amount including any tax. | [optional] value must be a 64 bit float
**overageInclTax** | decimal.Decimal, int, float,  | decimal.Decimal,  | Overage amount including tax (if applicable). | [optional] value must be a 64 bit float
**overageCurrency** | str,  | str,  | Currency of the overage amount. | [optional] 
**overageQuantity** | decimal.Decimal, int,  | decimal.Decimal,  | Quantity above monthly quota of the current subscritpion, in units. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

