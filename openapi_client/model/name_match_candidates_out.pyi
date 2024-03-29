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


class NameMatchCandidatesOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Classified matched names
    """


    class MetaOapg:
        
        class properties:
            script = schemas.StrSchema
            id = schemas.StrSchema
            explanation = schemas.StrSchema
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            orderOption = schemas.StrSchema
            
            
            class matchCandidates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NameMatchCandidateOut']:
                        return NameMatchCandidateOut
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NameMatchCandidateOut'], typing.List['NameMatchCandidateOut']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'matchCandidates':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NameMatchCandidateOut':
                    return super().__getitem__(i)
            __annotations__ = {
                "script": script,
                "id": id,
                "explanation": explanation,
                "firstName": firstName,
                "lastName": lastName,
                "orderOption": orderOption,
                "matchCandidates": matchCandidates,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["script"]) -> MetaOapg.properties.script: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["explanation"]) -> MetaOapg.properties.explanation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderOption"]) -> MetaOapg.properties.orderOption: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matchCandidates"]) -> MetaOapg.properties.matchCandidates: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["script", "id", "explanation", "firstName", "lastName", "orderOption", "matchCandidates", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["script"]) -> typing.Union[MetaOapg.properties.script, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["explanation"]) -> typing.Union[MetaOapg.properties.explanation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderOption"]) -> typing.Union[MetaOapg.properties.orderOption, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matchCandidates"]) -> typing.Union[MetaOapg.properties.matchCandidates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["script", "id", "explanation", "firstName", "lastName", "orderOption", "matchCandidates", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        script: typing.Union[MetaOapg.properties.script, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        explanation: typing.Union[MetaOapg.properties.explanation, str, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        orderOption: typing.Union[MetaOapg.properties.orderOption, str, schemas.Unset] = schemas.unset,
        matchCandidates: typing.Union[MetaOapg.properties.matchCandidates, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NameMatchCandidatesOut':
        return super().__new__(
            cls,
            *_args,
            script=script,
            id=id,
            explanation=explanation,
            firstName=firstName,
            lastName=lastName,
            orderOption=orderOption,
            matchCandidates=matchCandidates,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.name_match_candidate_out import NameMatchCandidateOut
