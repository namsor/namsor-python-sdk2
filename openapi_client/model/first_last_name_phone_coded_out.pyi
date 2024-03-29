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


class FirstLastNamePhoneCodedOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents the output of inferring the LIKELY country and phone code from a personal name and phone number.
    """


    class MetaOapg:
        
        class properties:
            script = schemas.StrSchema
            id = schemas.StrSchema
            explanation = schemas.StrSchema
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            internationalPhoneNumberVerified = schemas.StrSchema
            phoneCountryIso2Verified = schemas.StrSchema
            phoneCountryCode = schemas.Int32Schema
            phoneCountryCodeAlt = schemas.Int32Schema
            phoneCountryIso2 = schemas.StrSchema
            phoneCountryIso2Alt = schemas.StrSchema
            originCountryIso2 = schemas.StrSchema
            originCountryIso2Alt = schemas.StrSchema
            phoneNumber = schemas.StrSchema
            verified = schemas.BoolSchema
            
            
            class score(
                schemas.Float64Schema
            ):
                pass
            countryIso2 = schemas.StrSchema
            __annotations__ = {
                "script": script,
                "id": id,
                "explanation": explanation,
                "firstName": firstName,
                "lastName": lastName,
                "internationalPhoneNumberVerified": internationalPhoneNumberVerified,
                "phoneCountryIso2Verified": phoneCountryIso2Verified,
                "phoneCountryCode": phoneCountryCode,
                "phoneCountryCodeAlt": phoneCountryCodeAlt,
                "phoneCountryIso2": phoneCountryIso2,
                "phoneCountryIso2Alt": phoneCountryIso2Alt,
                "originCountryIso2": originCountryIso2,
                "originCountryIso2Alt": originCountryIso2Alt,
                "phoneNumber": phoneNumber,
                "verified": verified,
                "score": score,
                "countryIso2": countryIso2,
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
    def __getitem__(self, name: typing_extensions.Literal["internationalPhoneNumberVerified"]) -> MetaOapg.properties.internationalPhoneNumberVerified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneCountryIso2Verified"]) -> MetaOapg.properties.phoneCountryIso2Verified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneCountryCode"]) -> MetaOapg.properties.phoneCountryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneCountryCodeAlt"]) -> MetaOapg.properties.phoneCountryCodeAlt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneCountryIso2"]) -> MetaOapg.properties.phoneCountryIso2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneCountryIso2Alt"]) -> MetaOapg.properties.phoneCountryIso2Alt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originCountryIso2"]) -> MetaOapg.properties.originCountryIso2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originCountryIso2Alt"]) -> MetaOapg.properties.originCountryIso2Alt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumber"]) -> MetaOapg.properties.phoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verified"]) -> MetaOapg.properties.verified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryIso2"]) -> MetaOapg.properties.countryIso2: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["script", "id", "explanation", "firstName", "lastName", "internationalPhoneNumberVerified", "phoneCountryIso2Verified", "phoneCountryCode", "phoneCountryCodeAlt", "phoneCountryIso2", "phoneCountryIso2Alt", "originCountryIso2", "originCountryIso2Alt", "phoneNumber", "verified", "score", "countryIso2", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["internationalPhoneNumberVerified"]) -> typing.Union[MetaOapg.properties.internationalPhoneNumberVerified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneCountryIso2Verified"]) -> typing.Union[MetaOapg.properties.phoneCountryIso2Verified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneCountryCode"]) -> typing.Union[MetaOapg.properties.phoneCountryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneCountryCodeAlt"]) -> typing.Union[MetaOapg.properties.phoneCountryCodeAlt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneCountryIso2"]) -> typing.Union[MetaOapg.properties.phoneCountryIso2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneCountryIso2Alt"]) -> typing.Union[MetaOapg.properties.phoneCountryIso2Alt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originCountryIso2"]) -> typing.Union[MetaOapg.properties.originCountryIso2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originCountryIso2Alt"]) -> typing.Union[MetaOapg.properties.originCountryIso2Alt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumber"]) -> typing.Union[MetaOapg.properties.phoneNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verified"]) -> typing.Union[MetaOapg.properties.verified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score"]) -> typing.Union[MetaOapg.properties.score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryIso2"]) -> typing.Union[MetaOapg.properties.countryIso2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["script", "id", "explanation", "firstName", "lastName", "internationalPhoneNumberVerified", "phoneCountryIso2Verified", "phoneCountryCode", "phoneCountryCodeAlt", "phoneCountryIso2", "phoneCountryIso2Alt", "originCountryIso2", "originCountryIso2Alt", "phoneNumber", "verified", "score", "countryIso2", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        script: typing.Union[MetaOapg.properties.script, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        explanation: typing.Union[MetaOapg.properties.explanation, str, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        internationalPhoneNumberVerified: typing.Union[MetaOapg.properties.internationalPhoneNumberVerified, str, schemas.Unset] = schemas.unset,
        phoneCountryIso2Verified: typing.Union[MetaOapg.properties.phoneCountryIso2Verified, str, schemas.Unset] = schemas.unset,
        phoneCountryCode: typing.Union[MetaOapg.properties.phoneCountryCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        phoneCountryCodeAlt: typing.Union[MetaOapg.properties.phoneCountryCodeAlt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        phoneCountryIso2: typing.Union[MetaOapg.properties.phoneCountryIso2, str, schemas.Unset] = schemas.unset,
        phoneCountryIso2Alt: typing.Union[MetaOapg.properties.phoneCountryIso2Alt, str, schemas.Unset] = schemas.unset,
        originCountryIso2: typing.Union[MetaOapg.properties.originCountryIso2, str, schemas.Unset] = schemas.unset,
        originCountryIso2Alt: typing.Union[MetaOapg.properties.originCountryIso2Alt, str, schemas.Unset] = schemas.unset,
        phoneNumber: typing.Union[MetaOapg.properties.phoneNumber, str, schemas.Unset] = schemas.unset,
        verified: typing.Union[MetaOapg.properties.verified, bool, schemas.Unset] = schemas.unset,
        score: typing.Union[MetaOapg.properties.score, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        countryIso2: typing.Union[MetaOapg.properties.countryIso2, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FirstLastNamePhoneCodedOut':
        return super().__new__(
            cls,
            *_args,
            script=script,
            id=id,
            explanation=explanation,
            firstName=firstName,
            lastName=lastName,
            internationalPhoneNumberVerified=internationalPhoneNumberVerified,
            phoneCountryIso2Verified=phoneCountryIso2Verified,
            phoneCountryCode=phoneCountryCode,
            phoneCountryCodeAlt=phoneCountryCodeAlt,
            phoneCountryIso2=phoneCountryIso2,
            phoneCountryIso2Alt=phoneCountryIso2Alt,
            originCountryIso2=originCountryIso2,
            originCountryIso2Alt=originCountryIso2Alt,
            phoneNumber=phoneNumber,
            verified=verified,
            score=score,
            countryIso2=countryIso2,
            _configuration=_configuration,
            **kwargs,
        )
