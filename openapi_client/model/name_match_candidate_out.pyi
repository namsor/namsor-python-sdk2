# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. By default, enpoints use 1 unit per name (ex. Gender), but Ethnicity classification uses 10 to 20 units per name depending on taxonomy. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    The version of the OpenAPI document: 2.0.27
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class NameMatchCandidateOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The ordered list of name matching candidates
    """


    class MetaOapg:
        
        class properties:
            candidateName = schemas.StrSchema
            probability = schemas.Float64Schema
            predScoreGivenName = schemas.Float64Schema
            predScoreFamilyName = schemas.Float64Schema
            __annotations__ = {
                "candidateName": candidateName,
                "probability": probability,
                "predScoreGivenName": predScoreGivenName,
                "predScoreFamilyName": predScoreFamilyName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["candidateName"]) -> MetaOapg.properties.candidateName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["probability"]) -> MetaOapg.properties.probability: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["predScoreGivenName"]) -> MetaOapg.properties.predScoreGivenName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["predScoreFamilyName"]) -> MetaOapg.properties.predScoreFamilyName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["candidateName", "probability", "predScoreGivenName", "predScoreFamilyName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["candidateName"]) -> typing.Union[MetaOapg.properties.candidateName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["probability"]) -> typing.Union[MetaOapg.properties.probability, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["predScoreGivenName"]) -> typing.Union[MetaOapg.properties.predScoreGivenName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["predScoreFamilyName"]) -> typing.Union[MetaOapg.properties.predScoreFamilyName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["candidateName", "probability", "predScoreGivenName", "predScoreFamilyName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        candidateName: typing.Union[MetaOapg.properties.candidateName, str, schemas.Unset] = schemas.unset,
        probability: typing.Union[MetaOapg.properties.probability, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        predScoreGivenName: typing.Union[MetaOapg.properties.predScoreGivenName, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        predScoreFamilyName: typing.Union[MetaOapg.properties.predScoreFamilyName, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NameMatchCandidateOut':
        return super().__new__(
            cls,
            *_args,
            candidateName=candidateName,
            probability=probability,
            predScoreGivenName=predScoreGivenName,
            predScoreFamilyName=predScoreFamilyName,
            _configuration=_configuration,
            **kwargs,
        )