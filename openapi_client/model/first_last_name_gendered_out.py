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


class FirstLastNameGenderedOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents the output of inferring the LIKELY gender from a personal name.
    """


    class MetaOapg:
        
        class properties:
            script = schemas.StrSchema
            id = schemas.StrSchema
            explanation = schemas.StrSchema
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            
            
            class likelyGender(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "male": "MALE",
                        "female": "FEMALE",
                        "unknown": "UNKNOWN",
                    }
                
                @schemas.classproperty
                def MALE(cls):
                    return cls("male")
                
                @schemas.classproperty
                def FEMALE(cls):
                    return cls("female")
                
                @schemas.classproperty
                def UNKNOWN(cls):
                    return cls("unknown")
            
            
            class genderScale(
                schemas.Float64Schema
            ):
            
            
                class MetaOapg:
                    format = 'double'
                    inclusive_maximum = 1
                    inclusive_minimum = -1
            
            
            class score(
                schemas.Float64Schema
            ):
            
            
                class MetaOapg:
                    format = 'double'
                    inclusive_maximum = 100
                    inclusive_minimum = 0
            
            
            class probabilityCalibrated(
                schemas.Float64Schema
            ):
            
            
                class MetaOapg:
                    format = 'double'
                    inclusive_maximum = 1
                    inclusive_minimum = -1
            __annotations__ = {
                "script": script,
                "id": id,
                "explanation": explanation,
                "firstName": firstName,
                "lastName": lastName,
                "likelyGender": likelyGender,
                "genderScale": genderScale,
                "score": score,
                "probabilityCalibrated": probabilityCalibrated,
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
    def __getitem__(self, name: typing_extensions.Literal["likelyGender"]) -> MetaOapg.properties.likelyGender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["genderScale"]) -> MetaOapg.properties.genderScale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["probabilityCalibrated"]) -> MetaOapg.properties.probabilityCalibrated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["script", "id", "explanation", "firstName", "lastName", "likelyGender", "genderScale", "score", "probabilityCalibrated", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["likelyGender"]) -> typing.Union[MetaOapg.properties.likelyGender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["genderScale"]) -> typing.Union[MetaOapg.properties.genderScale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score"]) -> typing.Union[MetaOapg.properties.score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["probabilityCalibrated"]) -> typing.Union[MetaOapg.properties.probabilityCalibrated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["script", "id", "explanation", "firstName", "lastName", "likelyGender", "genderScale", "score", "probabilityCalibrated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        script: typing.Union[MetaOapg.properties.script, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        explanation: typing.Union[MetaOapg.properties.explanation, str, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        likelyGender: typing.Union[MetaOapg.properties.likelyGender, str, schemas.Unset] = schemas.unset,
        genderScale: typing.Union[MetaOapg.properties.genderScale, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        score: typing.Union[MetaOapg.properties.score, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        probabilityCalibrated: typing.Union[MetaOapg.properties.probabilityCalibrated, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FirstLastNameGenderedOut':
        return super().__new__(
            cls,
            *_args,
            script=script,
            id=id,
            explanation=explanation,
            firstName=firstName,
            lastName=lastName,
            likelyGender=likelyGender,
            genderScale=genderScale,
            score=score,
            probabilityCalibrated=probabilityCalibrated,
            _configuration=_configuration,
            **kwargs,
        )
