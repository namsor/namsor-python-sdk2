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


class CorridorIn(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represent any transnational interaction between names (ex. remittance, communication, cross-border investment, airline travel
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def firstLastNameGeoFrom() -> typing.Type['FirstLastNameGeoIn']:
                return FirstLastNameGeoIn
        
            @staticmethod
            def firstLastNameGeoTo() -> typing.Type['FirstLastNameGeoIn']:
                return FirstLastNameGeoIn
            __annotations__ = {
                "id": id,
                "firstLastNameGeoFrom": firstLastNameGeoFrom,
                "firstLastNameGeoTo": firstLastNameGeoTo,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstLastNameGeoFrom"]) -> 'FirstLastNameGeoIn': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstLastNameGeoTo"]) -> 'FirstLastNameGeoIn': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "firstLastNameGeoFrom", "firstLastNameGeoTo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstLastNameGeoFrom"]) -> typing.Union['FirstLastNameGeoIn', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstLastNameGeoTo"]) -> typing.Union['FirstLastNameGeoIn', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "firstLastNameGeoFrom", "firstLastNameGeoTo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        firstLastNameGeoFrom: typing.Union['FirstLastNameGeoIn', schemas.Unset] = schemas.unset,
        firstLastNameGeoTo: typing.Union['FirstLastNameGeoIn', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CorridorIn':
        return super().__new__(
            cls,
            *_args,
            id=id,
            firstLastNameGeoFrom=firstLastNameGeoFrom,
            firstLastNameGeoTo=firstLastNameGeoTo,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.first_last_name_geo_in import FirstLastNameGeoIn