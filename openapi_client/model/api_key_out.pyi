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


class APIKeyOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            apiKey = schemas.StrSchema
            userId = schemas.StrSchema
            admin = schemas.BoolSchema
            vetted = schemas.BoolSchema
            learnable = schemas.BoolSchema
            anonymized = schemas.BoolSchema
            partner = schemas.BoolSchema
            striped = schemas.BoolSchema
            corporate = schemas.BoolSchema
            disabled = schemas.BoolSchema
            explainable = schemas.BoolSchema
            ipAddress = schemas.StrSchema
            __annotations__ = {
                "apiKey": apiKey,
                "userId": userId,
                "admin": admin,
                "vetted": vetted,
                "learnable": learnable,
                "anonymized": anonymized,
                "partner": partner,
                "striped": striped,
                "corporate": corporate,
                "disabled": disabled,
                "explainable": explainable,
                "ipAddress": ipAddress,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiKey"]) -> MetaOapg.properties.apiKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["admin"]) -> MetaOapg.properties.admin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vetted"]) -> MetaOapg.properties.vetted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["learnable"]) -> MetaOapg.properties.learnable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anonymized"]) -> MetaOapg.properties.anonymized: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partner"]) -> MetaOapg.properties.partner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["striped"]) -> MetaOapg.properties.striped: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["corporate"]) -> MetaOapg.properties.corporate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disabled"]) -> MetaOapg.properties.disabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["explainable"]) -> MetaOapg.properties.explainable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipAddress"]) -> MetaOapg.properties.ipAddress: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["apiKey", "userId", "admin", "vetted", "learnable", "anonymized", "partner", "striped", "corporate", "disabled", "explainable", "ipAddress", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiKey"]) -> typing.Union[MetaOapg.properties.apiKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["admin"]) -> typing.Union[MetaOapg.properties.admin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vetted"]) -> typing.Union[MetaOapg.properties.vetted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["learnable"]) -> typing.Union[MetaOapg.properties.learnable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anonymized"]) -> typing.Union[MetaOapg.properties.anonymized, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partner"]) -> typing.Union[MetaOapg.properties.partner, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["striped"]) -> typing.Union[MetaOapg.properties.striped, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["corporate"]) -> typing.Union[MetaOapg.properties.corporate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disabled"]) -> typing.Union[MetaOapg.properties.disabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["explainable"]) -> typing.Union[MetaOapg.properties.explainable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipAddress"]) -> typing.Union[MetaOapg.properties.ipAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["apiKey", "userId", "admin", "vetted", "learnable", "anonymized", "partner", "striped", "corporate", "disabled", "explainable", "ipAddress", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        apiKey: typing.Union[MetaOapg.properties.apiKey, str, schemas.Unset] = schemas.unset,
        userId: typing.Union[MetaOapg.properties.userId, str, schemas.Unset] = schemas.unset,
        admin: typing.Union[MetaOapg.properties.admin, bool, schemas.Unset] = schemas.unset,
        vetted: typing.Union[MetaOapg.properties.vetted, bool, schemas.Unset] = schemas.unset,
        learnable: typing.Union[MetaOapg.properties.learnable, bool, schemas.Unset] = schemas.unset,
        anonymized: typing.Union[MetaOapg.properties.anonymized, bool, schemas.Unset] = schemas.unset,
        partner: typing.Union[MetaOapg.properties.partner, bool, schemas.Unset] = schemas.unset,
        striped: typing.Union[MetaOapg.properties.striped, bool, schemas.Unset] = schemas.unset,
        corporate: typing.Union[MetaOapg.properties.corporate, bool, schemas.Unset] = schemas.unset,
        disabled: typing.Union[MetaOapg.properties.disabled, bool, schemas.Unset] = schemas.unset,
        explainable: typing.Union[MetaOapg.properties.explainable, bool, schemas.Unset] = schemas.unset,
        ipAddress: typing.Union[MetaOapg.properties.ipAddress, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'APIKeyOut':
        return super().__new__(
            cls,
            *_args,
            apiKey=apiKey,
            userId=userId,
            admin=admin,
            vetted=vetted,
            learnable=learnable,
            anonymized=anonymized,
            partner=partner,
            striped=striped,
            corporate=corporate,
            disabled=disabled,
            explainable=explainable,
            ipAddress=ipAddress,
            _configuration=_configuration,
            **kwargs,
        )
