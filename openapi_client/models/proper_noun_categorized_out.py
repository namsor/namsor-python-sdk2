# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.11
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ProperNounCategorizedOut(object):
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
        'name': 'str',
        'common_type': 'str',
        'common_type_alt': 'str',
        'score': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'common_type': 'commonType',
        'common_type_alt': 'commonTypeAlt',
        'score': 'score'
    }

    def __init__(self, id=None, name=None, common_type=None, common_type_alt=None, score=None):  # noqa: E501
        """ProperNounCategorizedOut - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._common_type = None
        self._common_type_alt = None
        self._score = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if common_type is not None:
            self.common_type = common_type
        if common_type_alt is not None:
            self.common_type_alt = common_type_alt
        if score is not None:
            self.score = score

    @property
    def id(self):
        """Gets the id of this ProperNounCategorizedOut.  # noqa: E501


        :return: The id of this ProperNounCategorizedOut.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProperNounCategorizedOut.


        :param id: The id of this ProperNounCategorizedOut.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProperNounCategorizedOut.  # noqa: E501


        :return: The name of this ProperNounCategorizedOut.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProperNounCategorizedOut.


        :param name: The name of this ProperNounCategorizedOut.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def common_type(self):
        """Gets the common_type of this ProperNounCategorizedOut.  # noqa: E501


        :return: The common_type of this ProperNounCategorizedOut.  # noqa: E501
        :rtype: str
        """
        return self._common_type

    @common_type.setter
    def common_type(self, common_type):
        """Sets the common_type of this ProperNounCategorizedOut.


        :param common_type: The common_type of this ProperNounCategorizedOut.  # noqa: E501
        :type: str
        """

        self._common_type = common_type

    @property
    def common_type_alt(self):
        """Gets the common_type_alt of this ProperNounCategorizedOut.  # noqa: E501


        :return: The common_type_alt of this ProperNounCategorizedOut.  # noqa: E501
        :rtype: str
        """
        return self._common_type_alt

    @common_type_alt.setter
    def common_type_alt(self, common_type_alt):
        """Sets the common_type_alt of this ProperNounCategorizedOut.


        :param common_type_alt: The common_type_alt of this ProperNounCategorizedOut.  # noqa: E501
        :type: str
        """

        self._common_type_alt = common_type_alt

    @property
    def score(self):
        """Gets the score of this ProperNounCategorizedOut.  # noqa: E501


        :return: The score of this ProperNounCategorizedOut.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ProperNounCategorizedOut.


        :param score: The score of this ProperNounCategorizedOut.  # noqa: E501
        :type: float
        """

        self._score = score

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
        if not isinstance(other, ProperNounCategorizedOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other