# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.12
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class APICounterV2Out(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'api_key': 'APIKeyOut',
        'api_service': 'str',
        'created_date_time': 'int',
        'total_usage': 'int',
        'last_flushed_date_time': 'int',
        'last_used_date_time': 'int',
        'service_features_usage': 'dict(str, int)'
    }

    attribute_map = {
        'api_key': 'apiKey',
        'api_service': 'apiService',
        'created_date_time': 'createdDateTime',
        'total_usage': 'totalUsage',
        'last_flushed_date_time': 'lastFlushedDateTime',
        'last_used_date_time': 'lastUsedDateTime',
        'service_features_usage': 'serviceFeaturesUsage'
    }

    def __init__(self, api_key=None, api_service=None, created_date_time=None, total_usage=None, last_flushed_date_time=None, last_used_date_time=None, service_features_usage=None):  # noqa: E501
        """APICounterV2Out - a model defined in OpenAPI"""  # noqa: E501

        self._api_key = None
        self._api_service = None
        self._created_date_time = None
        self._total_usage = None
        self._last_flushed_date_time = None
        self._last_used_date_time = None
        self._service_features_usage = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if api_service is not None:
            self.api_service = api_service
        if created_date_time is not None:
            self.created_date_time = created_date_time
        if total_usage is not None:
            self.total_usage = total_usage
        if last_flushed_date_time is not None:
            self.last_flushed_date_time = last_flushed_date_time
        if last_used_date_time is not None:
            self.last_used_date_time = last_used_date_time
        if service_features_usage is not None:
            self.service_features_usage = service_features_usage

    @property
    def api_key(self):
        """Gets the api_key of this APICounterV2Out.  # noqa: E501


        :return: The api_key of this APICounterV2Out.  # noqa: E501
        :rtype: APIKeyOut
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this APICounterV2Out.


        :param api_key: The api_key of this APICounterV2Out.  # noqa: E501
        :type: APIKeyOut
        """

        self._api_key = api_key

    @property
    def api_service(self):
        """Gets the api_service of this APICounterV2Out.  # noqa: E501


        :return: The api_service of this APICounterV2Out.  # noqa: E501
        :rtype: str
        """
        return self._api_service

    @api_service.setter
    def api_service(self, api_service):
        """Sets the api_service of this APICounterV2Out.


        :param api_service: The api_service of this APICounterV2Out.  # noqa: E501
        :type: str
        """

        self._api_service = api_service

    @property
    def created_date_time(self):
        """Gets the created_date_time of this APICounterV2Out.  # noqa: E501


        :return: The created_date_time of this APICounterV2Out.  # noqa: E501
        :rtype: int
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this APICounterV2Out.


        :param created_date_time: The created_date_time of this APICounterV2Out.  # noqa: E501
        :type: int
        """

        self._created_date_time = created_date_time

    @property
    def total_usage(self):
        """Gets the total_usage of this APICounterV2Out.  # noqa: E501


        :return: The total_usage of this APICounterV2Out.  # noqa: E501
        :rtype: int
        """
        return self._total_usage

    @total_usage.setter
    def total_usage(self, total_usage):
        """Sets the total_usage of this APICounterV2Out.


        :param total_usage: The total_usage of this APICounterV2Out.  # noqa: E501
        :type: int
        """

        self._total_usage = total_usage

    @property
    def last_flushed_date_time(self):
        """Gets the last_flushed_date_time of this APICounterV2Out.  # noqa: E501


        :return: The last_flushed_date_time of this APICounterV2Out.  # noqa: E501
        :rtype: int
        """
        return self._last_flushed_date_time

    @last_flushed_date_time.setter
    def last_flushed_date_time(self, last_flushed_date_time):
        """Sets the last_flushed_date_time of this APICounterV2Out.


        :param last_flushed_date_time: The last_flushed_date_time of this APICounterV2Out.  # noqa: E501
        :type: int
        """

        self._last_flushed_date_time = last_flushed_date_time

    @property
    def last_used_date_time(self):
        """Gets the last_used_date_time of this APICounterV2Out.  # noqa: E501


        :return: The last_used_date_time of this APICounterV2Out.  # noqa: E501
        :rtype: int
        """
        return self._last_used_date_time

    @last_used_date_time.setter
    def last_used_date_time(self, last_used_date_time):
        """Sets the last_used_date_time of this APICounterV2Out.


        :param last_used_date_time: The last_used_date_time of this APICounterV2Out.  # noqa: E501
        :type: int
        """

        self._last_used_date_time = last_used_date_time

    @property
    def service_features_usage(self):
        """Gets the service_features_usage of this APICounterV2Out.  # noqa: E501


        :return: The service_features_usage of this APICounterV2Out.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._service_features_usage

    @service_features_usage.setter
    def service_features_usage(self, service_features_usage):
        """Sets the service_features_usage of this APICounterV2Out.


        :param service_features_usage: The service_features_usage of this APICounterV2Out.  # noqa: E501
        :type: dict(str, int)
        """

        self._service_features_usage = service_features_usage

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, APICounterV2Out):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
