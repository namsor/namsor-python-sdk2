import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.personal_api import PersonalApi
from openapi_client.apis.tags.social_api import SocialApi
from openapi_client.apis.tags.chinese_api import ChineseApi
from openapi_client.apis.tags.japanese_api import JapaneseApi
from openapi_client.apis.tags.indian_api import IndianApi
from openapi_client.apis.tags.admin_api import AdminApi
from openapi_client.apis.tags.general_api import GeneralApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PERSONAL: PersonalApi,
        TagValues.SOCIAL: SocialApi,
        TagValues.CHINESE: ChineseApi,
        TagValues.JAPANESE: JapaneseApi,
        TagValues.INDIAN: IndianApi,
        TagValues.ADMIN: AdminApi,
        TagValues.GENERAL: GeneralApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PERSONAL: PersonalApi,
        TagValues.SOCIAL: SocialApi,
        TagValues.CHINESE: ChineseApi,
        TagValues.JAPANESE: JapaneseApi,
        TagValues.INDIAN: IndianApi,
        TagValues.ADMIN: AdminApi,
        TagValues.GENERAL: GeneralApi,
    }
)
