# coding: utf-8

# flake8: noqa
"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. By default, enpoints use 1 unit per name (ex. Gender), but Ethnicity classification uses 10 to 20 units per name depending on taxonomy. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.18
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
from openapi_client.models.api_plan_subscription_out import APIPlanSubscriptionOut
from openapi_client.models.api_service_out import APIServiceOut
from openapi_client.models.api_services_out import APIServicesOut
from openapi_client.models.api_usage_aggregated_out import APIUsageAggregatedOut
from openapi_client.models.api_usage_history_out import APIUsageHistoryOut
from openapi_client.models.batch_corridor_in import BatchCorridorIn
from openapi_client.models.batch_corridor_out import BatchCorridorOut
from openapi_client.models.batch_first_last_name_diasporaed_out import BatchFirstLastNameDiasporaedOut
from openapi_client.models.batch_first_last_name_gender_in import BatchFirstLastNameGenderIn
from openapi_client.models.batch_first_last_name_gendered_out import BatchFirstLastNameGenderedOut
from openapi_client.models.batch_first_last_name_geo_in import BatchFirstLastNameGeoIn
from openapi_client.models.batch_first_last_name_geo_subclassification_out import BatchFirstLastNameGeoSubclassificationOut
from openapi_client.models.batch_first_last_name_geo_zipped_in import BatchFirstLastNameGeoZippedIn
from openapi_client.models.batch_first_last_name_in import BatchFirstLastNameIn
from openapi_client.models.batch_first_last_name_origined_out import BatchFirstLastNameOriginedOut
from openapi_client.models.batch_first_last_name_phone_coded_out import BatchFirstLastNamePhoneCodedOut
from openapi_client.models.batch_first_last_name_phone_number_geo_in import BatchFirstLastNamePhoneNumberGeoIn
from openapi_client.models.batch_first_last_name_phone_number_in import BatchFirstLastNamePhoneNumberIn
from openapi_client.models.batch_first_last_name_us_race_ethnicity_out import BatchFirstLastNameUSRaceEthnicityOut
from openapi_client.models.batch_match_personal_first_last_name_in import BatchMatchPersonalFirstLastNameIn
from openapi_client.models.batch_name_geo_in import BatchNameGeoIn
from openapi_client.models.batch_name_in import BatchNameIn
from openapi_client.models.batch_name_match_candidates_out import BatchNameMatchCandidatesOut
from openapi_client.models.batch_name_matched_out import BatchNameMatchedOut
from openapi_client.models.batch_personal_name_gendered_out import BatchPersonalNameGenderedOut
from openapi_client.models.batch_personal_name_geo_in import BatchPersonalNameGeoIn
from openapi_client.models.batch_personal_name_geo_out import BatchPersonalNameGeoOut
from openapi_client.models.batch_personal_name_in import BatchPersonalNameIn
from openapi_client.models.batch_personal_name_parsed_out import BatchPersonalNameParsedOut
from openapi_client.models.batch_proper_noun_categorized_out import BatchProperNounCategorizedOut
from openapi_client.models.corridor_in import CorridorIn
from openapi_client.models.corridor_out import CorridorOut
from openapi_client.models.feedback_loop_out import FeedbackLoopOut
from openapi_client.models.first_last_name_diasporaed_out import FirstLastNameDiasporaedOut
from openapi_client.models.first_last_name_gender_in import FirstLastNameGenderIn
from openapi_client.models.first_last_name_gendered_out import FirstLastNameGenderedOut
from openapi_client.models.first_last_name_geo_in import FirstLastNameGeoIn
from openapi_client.models.first_last_name_geo_subclassification_out import FirstLastNameGeoSubclassificationOut
from openapi_client.models.first_last_name_geo_zipped_in import FirstLastNameGeoZippedIn
from openapi_client.models.first_last_name_in import FirstLastNameIn
from openapi_client.models.first_last_name_origined_out import FirstLastNameOriginedOut
from openapi_client.models.first_last_name_out import FirstLastNameOut
from openapi_client.models.first_last_name_phone_coded_out import FirstLastNamePhoneCodedOut
from openapi_client.models.first_last_name_phone_number_geo_in import FirstLastNamePhoneNumberGeoIn
from openapi_client.models.first_last_name_phone_number_in import FirstLastNamePhoneNumberIn
from openapi_client.models.first_last_name_us_race_ethnicity_out import FirstLastNameUSRaceEthnicityOut
from openapi_client.models.match_personal_first_last_name_in import MatchPersonalFirstLastNameIn
from openapi_client.models.name_geo_in import NameGeoIn
from openapi_client.models.name_in import NameIn
from openapi_client.models.name_match_candidate_out import NameMatchCandidateOut
from openapi_client.models.name_match_candidates_out import NameMatchCandidatesOut
from openapi_client.models.name_matched_out import NameMatchedOut
from openapi_client.models.personal_name_gendered_out import PersonalNameGenderedOut
from openapi_client.models.personal_name_geo_in import PersonalNameGeoIn
from openapi_client.models.personal_name_geo_out import PersonalNameGeoOut
from openapi_client.models.personal_name_in import PersonalNameIn
from openapi_client.models.personal_name_parsed_out import PersonalNameParsedOut
from openapi_client.models.proper_noun_categorized_out import ProperNounCategorizedOut
from openapi_client.models.software_version_out import SoftwareVersionOut
