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


class RegionISO(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    List of countries and regions
    """


    class MetaOapg:
        
        class properties:
            countryName = schemas.StrSchema
            countryNumCode = schemas.StrSchema
            countryISO2 = schemas.StrSchema
            countryISO3 = schemas.StrSchema
            countryFIPS = schemas.StrSchema
            subregion = schemas.StrSchema
            region = schemas.StrSchema
            topregion = schemas.StrSchema
            __annotations__ = {
                "countryName": countryName,
                "countryNumCode": countryNumCode,
                "countryISO2": countryISO2,
                "countryISO3": countryISO3,
                "countryFIPS": countryFIPS,
                "subregion": subregion,
                "region": region,
                "topregion": topregion,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryName"]) -> MetaOapg.properties.countryName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryNumCode"]) -> MetaOapg.properties.countryNumCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryISO2"]) -> MetaOapg.properties.countryISO2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryISO3"]) -> MetaOapg.properties.countryISO3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryFIPS"]) -> MetaOapg.properties.countryFIPS: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subregion"]) -> MetaOapg.properties.subregion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topregion"]) -> MetaOapg.properties.topregion: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["countryName", "countryNumCode", "countryISO2", "countryISO3", "countryFIPS", "subregion", "region", "topregion", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryName"]) -> typing.Union[MetaOapg.properties.countryName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryNumCode"]) -> typing.Union[MetaOapg.properties.countryNumCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryISO2"]) -> typing.Union[MetaOapg.properties.countryISO2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryISO3"]) -> typing.Union[MetaOapg.properties.countryISO3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryFIPS"]) -> typing.Union[MetaOapg.properties.countryFIPS, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subregion"]) -> typing.Union[MetaOapg.properties.subregion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topregion"]) -> typing.Union[MetaOapg.properties.topregion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["countryName", "countryNumCode", "countryISO2", "countryISO3", "countryFIPS", "subregion", "region", "topregion", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        countryName: typing.Union[MetaOapg.properties.countryName, str, schemas.Unset] = schemas.unset,
        countryNumCode: typing.Union[MetaOapg.properties.countryNumCode, str, schemas.Unset] = schemas.unset,
        countryISO2: typing.Union[MetaOapg.properties.countryISO2, str, schemas.Unset] = schemas.unset,
        countryISO3: typing.Union[MetaOapg.properties.countryISO3, str, schemas.Unset] = schemas.unset,
        countryFIPS: typing.Union[MetaOapg.properties.countryFIPS, str, schemas.Unset] = schemas.unset,
        subregion: typing.Union[MetaOapg.properties.subregion, str, schemas.Unset] = schemas.unset,
        region: typing.Union[MetaOapg.properties.region, str, schemas.Unset] = schemas.unset,
        topregion: typing.Union[MetaOapg.properties.topregion, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RegionISO':
        return super().__new__(
            cls,
            *_args,
            countryName=countryName,
            countryNumCode=countryNumCode,
            countryISO2=countryISO2,
            countryISO3=countryISO3,
            countryFIPS=countryFIPS,
            subregion=subregion,
            region=region,
            topregion=topregion,
            _configuration=_configuration,
            **kwargs,
        )
