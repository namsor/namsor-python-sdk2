# coding: utf-8

# flake8: noqa
"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.11
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from openapi_client.models.api_billing_period_usage_out import APIBillingPeriodUsageOut
from openapi_client.models.api_classifier_out import APIClassifierOut
from openapi_client.models.api_classifier_taxonomy_out import APIClassifierTaxonomyOut
from openapi_client.models.api_classifiers_status_out import APIClassifiersStatusOut
from openapi_client.models.api_counter_v2_out import APICounterV2Out
from openapi_client.models.api_key_out import APIKeyOut
from openapi_client.models.api_period_usage_out import APIPeriodUsageOut
from openapi_client.models.api_plan_out import APIPlanOut
from openapi_client.models.api_plan_subscription_out import APIPlanSubscriptionOut
from openapi_client.models.api_plans_out import APIPlansOut
from openapi_client.models.api_service_out import APIServiceOut
from openapi_client.models.api_services_out import APIServicesOut
from openapi_client.models.api_usage_aggregated_out import APIUsageAggregatedOut
from openapi_client.models.batch_first_last_name_diasporaed_out import BatchFirstLastNameDiasporaedOut
from openapi_client.models.batch_first_last_name_gender_in import BatchFirstLastNameGenderIn
from openapi_client.models.batch_first_last_name_gendered_out import BatchFirstLastNameGenderedOut
from openapi_client.models.batch_first_last_name_geo_in import BatchFirstLastNameGeoIn
from openapi_client.models.batch_first_last_name_geo_zipped_in import BatchFirstLastNameGeoZippedIn
from openapi_client.models.batch_first_last_name_in import BatchFirstLastNameIn
from openapi_client.models.batch_first_last_name_origined_out import BatchFirstLastNameOriginedOut
from openapi_client.models.batch_first_last_name_phone_coded_out import BatchFirstLastNamePhoneCodedOut
from openapi_client.models.batch_first_last_name_phone_number_geo_in import BatchFirstLastNamePhoneNumberGeoIn
from openapi_client.models.batch_first_last_name_phone_number_in import BatchFirstLastNamePhoneNumberIn
from openapi_client.models.batch_first_last_name_us_race_ethnicity_out import BatchFirstLastNameUSRaceEthnicityOut
from openapi_client.models.batch_match_personal_first_last_name_in import BatchMatchPersonalFirstLastNameIn
from openapi_client.models.batch_name_match_candidates_out import BatchNameMatchCandidatesOut
from openapi_client.models.batch_name_matched_out import BatchNameMatchedOut
from openapi_client.models.batch_parsed_full_name_geo_in import BatchParsedFullNameGeoIn
from openapi_client.models.batch_parsed_full_name_in import BatchParsedFullNameIn
from openapi_client.models.batch_personal_name_gendered_out import BatchPersonalNameGenderedOut
from openapi_client.models.batch_personal_name_geo_in import BatchPersonalNameGeoIn
from openapi_client.models.batch_personal_name_geo_out import BatchPersonalNameGeoOut
from openapi_client.models.batch_personal_name_in import BatchPersonalNameIn
from openapi_client.models.batch_personal_name_parsed_out import BatchPersonalNameParsedOut
from openapi_client.models.billing_history_out import BillingHistoryOut
from openapi_client.models.billing_info_in_out import BillingInfoInOut
from openapi_client.models.cache_metrics_out import CacheMetricsOut
from openapi_client.models.classifier_metrics_out import ClassifierMetricsOut
from openapi_client.models.currencies_out import CurrenciesOut
from openapi_client.models.deploy_ui_out import DeployUIOut
from openapi_client.models.expected_class_metrics_out import ExpectedClassMetricsOut
from openapi_client.models.feedback_loop_out import FeedbackLoopOut
from openapi_client.models.first_last_name_diasporaed_out import FirstLastNameDiasporaedOut
from openapi_client.models.first_last_name_gender_in import FirstLastNameGenderIn
from openapi_client.models.first_last_name_gendered_out import FirstLastNameGenderedOut
from openapi_client.models.first_last_name_geo_in import FirstLastNameGeoIn
from openapi_client.models.first_last_name_geo_zipped_in import FirstLastNameGeoZippedIn
from openapi_client.models.first_last_name_in import FirstLastNameIn
from openapi_client.models.first_last_name_origined_out import FirstLastNameOriginedOut
from openapi_client.models.first_last_name_out import FirstLastNameOut
from openapi_client.models.first_last_name_phone_coded_out import FirstLastNamePhoneCodedOut
from openapi_client.models.first_last_name_phone_number_geo_in import FirstLastNamePhoneNumberGeoIn
from openapi_client.models.first_last_name_phone_number_in import FirstLastNamePhoneNumberIn
from openapi_client.models.first_last_name_us_race_ethnicity_out import FirstLastNameUSRaceEthnicityOut
from openapi_client.models.inline_object import InlineObject
from openapi_client.models.invoice_item_out import InvoiceItemOut
from openapi_client.models.invoice_out import InvoiceOut
from openapi_client.models.match_personal_first_last_name_in import MatchPersonalFirstLastNameIn
from openapi_client.models.nam_sor_counter_out import NamSorCounterOut
from openapi_client.models.name_match_candidate_out import NameMatchCandidateOut
from openapi_client.models.name_match_candidates_out import NameMatchCandidatesOut
from openapi_client.models.name_matched_out import NameMatchedOut
from openapi_client.models.parsed_full_name_geo_in import ParsedFullNameGeoIn
from openapi_client.models.parsed_full_name_in import ParsedFullNameIn
from openapi_client.models.personal_name_gendered_out import PersonalNameGenderedOut
from openapi_client.models.personal_name_geo_in import PersonalNameGeoIn
from openapi_client.models.personal_name_geo_out import PersonalNameGeoOut
from openapi_client.models.personal_name_in import PersonalNameIn
from openapi_client.models.personal_name_parsed_out import PersonalNameParsedOut
from openapi_client.models.proper_noun_categorized_out import ProperNounCategorizedOut
from openapi_client.models.romanized_name_out import RomanizedNameOut
from openapi_client.models.software_version_out import SoftwareVersionOut
from openapi_client.models.source_detailed_metrics_out import SourceDetailedMetricsOut
from openapi_client.models.source_metrics_out import SourceMetricsOut
from openapi_client.models.stripe_card_out import StripeCardOut
from openapi_client.models.stripe_customer_out import StripeCustomerOut
from openapi_client.models.system_metrics_out import SystemMetricsOut
from openapi_client.models.user_info_out import UserInfoOut
