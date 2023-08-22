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


class PersonalNameReligionedOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    religious-coded names
    """


    class MetaOapg:
        
        class properties:
            script = schemas.StrSchema
            id = schemas.StrSchema
            explanation = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class score(
                schemas.Float64Schema
            ):
                pass
            religion = schemas.StrSchema
            religionAlt = schemas.StrSchema
            
            
            class religionsTop(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'religionsTop':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class probabilityCalibrated(
                schemas.Float64Schema
            ):
                pass
            
            
            class probabilityAltCalibrated(
                schemas.Float64Schema
            ):
                pass
            __annotations__ = {
                "script": script,
                "id": id,
                "explanation": explanation,
                "name": name,
                "score": score,
                "religion": religion,
                "religionAlt": religionAlt,
                "religionsTop": religionsTop,
                "probabilityCalibrated": probabilityCalibrated,
                "probabilityAltCalibrated": probabilityAltCalibrated,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["script"]) -> MetaOapg.properties.script: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["explanation"]) -> MetaOapg.properties.explanation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["religion"]) -> MetaOapg.properties.religion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["religionAlt"]) -> MetaOapg.properties.religionAlt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["religionsTop"]) -> MetaOapg.properties.religionsTop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["probabilityCalibrated"]) -> MetaOapg.properties.probabilityCalibrated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["probabilityAltCalibrated"]) -> MetaOapg.properties.probabilityAltCalibrated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["script", "id", "explanation", "name", "score", "religion", "religionAlt", "religionsTop", "probabilityCalibrated", "probabilityAltCalibrated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["script"]) -> typing.Union[MetaOapg.properties.script, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["explanation"]) -> typing.Union[MetaOapg.properties.explanation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score"]) -> typing.Union[MetaOapg.properties.score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["religion"]) -> typing.Union[MetaOapg.properties.religion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["religionAlt"]) -> typing.Union[MetaOapg.properties.religionAlt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["religionsTop"]) -> typing.Union[MetaOapg.properties.religionsTop, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["probabilityCalibrated"]) -> typing.Union[MetaOapg.properties.probabilityCalibrated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["probabilityAltCalibrated"]) -> typing.Union[MetaOapg.properties.probabilityAltCalibrated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["script", "id", "explanation", "name", "score", "religion", "religionAlt", "religionsTop", "probabilityCalibrated", "probabilityAltCalibrated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        script: typing.Union[MetaOapg.properties.script, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        explanation: typing.Union[MetaOapg.properties.explanation, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        score: typing.Union[MetaOapg.properties.score, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        religion: typing.Union[MetaOapg.properties.religion, str, schemas.Unset] = schemas.unset,
        religionAlt: typing.Union[MetaOapg.properties.religionAlt, str, schemas.Unset] = schemas.unset,
        religionsTop: typing.Union[MetaOapg.properties.religionsTop, list, tuple, schemas.Unset] = schemas.unset,
        probabilityCalibrated: typing.Union[MetaOapg.properties.probabilityCalibrated, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        probabilityAltCalibrated: typing.Union[MetaOapg.properties.probabilityAltCalibrated, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonalNameReligionedOut':
        return super().__new__(
            cls,
            *_args,
            script=script,
            id=id,
            explanation=explanation,
            name=name,
            score=score,
            religion=religion,
            religionAlt=religionAlt,
            religionsTop=religionsTop,
            probabilityCalibrated=probabilityCalibrated,
            probabilityAltCalibrated=probabilityAltCalibrated,
            _configuration=_configuration,
            **kwargs,
        )
