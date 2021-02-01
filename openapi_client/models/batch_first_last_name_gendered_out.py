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


class BatchFirstLastNameGenderedOut(object):
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
        'personal_names': 'list[FirstLastNameGenderedOut]'
    }

    attribute_map = {
        'personal_names': 'personalNames'
    }

    def __init__(self, personal_names=None):  # noqa: E501
        """BatchFirstLastNameGenderedOut - a model defined in OpenAPI"""  # noqa: E501

        self._personal_names = None
        self.discriminator = None

        if personal_names is not None:
            self.personal_names = personal_names

    @property
    def personal_names(self):
        """Gets the personal_names of this BatchFirstLastNameGenderedOut.  # noqa: E501


        :return: The personal_names of this BatchFirstLastNameGenderedOut.  # noqa: E501
        :rtype: list[FirstLastNameGenderedOut]
        """
        return self._personal_names

    @personal_names.setter
    def personal_names(self, personal_names):
        """Sets the personal_names of this BatchFirstLastNameGenderedOut.


        :param personal_names: The personal_names of this BatchFirstLastNameGenderedOut.  # noqa: E501
        :type: list[FirstLastNameGenderedOut]
        """

        self._personal_names = personal_names

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
        if not isinstance(other, BatchFirstLastNameGenderedOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
