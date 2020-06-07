# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.10
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class MatchPersonalFirstLastNameIn(object):
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
        'id': 'str',
        'name1': 'FirstLastNameIn',
        'name2': 'PersonalNameIn',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name1': 'name1',
        'name2': 'name2',
        'name': 'name'
    }

    def __init__(self, id=None, name1=None, name2=None, name=None):  # noqa: E501
        """MatchPersonalFirstLastNameIn - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name1 = None
        self._name2 = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name1 is not None:
            self.name1 = name1
        if name2 is not None:
            self.name2 = name2
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this MatchPersonalFirstLastNameIn.  # noqa: E501


        :return: The id of this MatchPersonalFirstLastNameIn.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MatchPersonalFirstLastNameIn.


        :param id: The id of this MatchPersonalFirstLastNameIn.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name1(self):
        """Gets the name1 of this MatchPersonalFirstLastNameIn.  # noqa: E501


        :return: The name1 of this MatchPersonalFirstLastNameIn.  # noqa: E501
        :rtype: FirstLastNameIn
        """
        return self._name1

    @name1.setter
    def name1(self, name1):
        """Sets the name1 of this MatchPersonalFirstLastNameIn.


        :param name1: The name1 of this MatchPersonalFirstLastNameIn.  # noqa: E501
        :type: FirstLastNameIn
        """

        self._name1 = name1

    @property
    def name2(self):
        """Gets the name2 of this MatchPersonalFirstLastNameIn.  # noqa: E501


        :return: The name2 of this MatchPersonalFirstLastNameIn.  # noqa: E501
        :rtype: PersonalNameIn
        """
        return self._name2

    @name2.setter
    def name2(self, name2):
        """Sets the name2 of this MatchPersonalFirstLastNameIn.


        :param name2: The name2 of this MatchPersonalFirstLastNameIn.  # noqa: E501
        :type: PersonalNameIn
        """

        self._name2 = name2

    @property
    def name(self):
        """Gets the name of this MatchPersonalFirstLastNameIn.  # noqa: E501


        :return: The name of this MatchPersonalFirstLastNameIn.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MatchPersonalFirstLastNameIn.


        :param name: The name of this MatchPersonalFirstLastNameIn.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, MatchPersonalFirstLastNameIn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
