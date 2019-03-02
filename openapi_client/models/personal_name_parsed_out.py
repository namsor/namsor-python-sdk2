# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 1000 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.2-beta
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PersonalNameParsedOut(object):
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
        'name_parser_type': 'str',
        'name_parser_type_alt': 'str',
        'first_last_name': 'FirstLastNameOut',
        'score': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'name_parser_type': 'nameParserType',
        'name_parser_type_alt': 'nameParserTypeAlt',
        'first_last_name': 'firstLastName',
        'score': 'score'
    }

    def __init__(self, id=None, name=None, name_parser_type=None, name_parser_type_alt=None, first_last_name=None, score=None):  # noqa: E501
        """PersonalNameParsedOut - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._name_parser_type = None
        self._name_parser_type_alt = None
        self._first_last_name = None
        self._score = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if name_parser_type is not None:
            self.name_parser_type = name_parser_type
        if name_parser_type_alt is not None:
            self.name_parser_type_alt = name_parser_type_alt
        if first_last_name is not None:
            self.first_last_name = first_last_name
        if score is not None:
            self.score = score

    @property
    def id(self):
        """Gets the id of this PersonalNameParsedOut.  # noqa: E501


        :return: The id of this PersonalNameParsedOut.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PersonalNameParsedOut.


        :param id: The id of this PersonalNameParsedOut.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PersonalNameParsedOut.  # noqa: E501


        :return: The name of this PersonalNameParsedOut.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PersonalNameParsedOut.


        :param name: The name of this PersonalNameParsedOut.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def name_parser_type(self):
        """Gets the name_parser_type of this PersonalNameParsedOut.  # noqa: E501


        :return: The name_parser_type of this PersonalNameParsedOut.  # noqa: E501
        :rtype: str
        """
        return self._name_parser_type

    @name_parser_type.setter
    def name_parser_type(self, name_parser_type):
        """Sets the name_parser_type of this PersonalNameParsedOut.


        :param name_parser_type: The name_parser_type of this PersonalNameParsedOut.  # noqa: E501
        :type: str
        """

        self._name_parser_type = name_parser_type

    @property
    def name_parser_type_alt(self):
        """Gets the name_parser_type_alt of this PersonalNameParsedOut.  # noqa: E501


        :return: The name_parser_type_alt of this PersonalNameParsedOut.  # noqa: E501
        :rtype: str
        """
        return self._name_parser_type_alt

    @name_parser_type_alt.setter
    def name_parser_type_alt(self, name_parser_type_alt):
        """Sets the name_parser_type_alt of this PersonalNameParsedOut.


        :param name_parser_type_alt: The name_parser_type_alt of this PersonalNameParsedOut.  # noqa: E501
        :type: str
        """

        self._name_parser_type_alt = name_parser_type_alt

    @property
    def first_last_name(self):
        """Gets the first_last_name of this PersonalNameParsedOut.  # noqa: E501


        :return: The first_last_name of this PersonalNameParsedOut.  # noqa: E501
        :rtype: FirstLastNameOut
        """
        return self._first_last_name

    @first_last_name.setter
    def first_last_name(self, first_last_name):
        """Sets the first_last_name of this PersonalNameParsedOut.


        :param first_last_name: The first_last_name of this PersonalNameParsedOut.  # noqa: E501
        :type: FirstLastNameOut
        """

        self._first_last_name = first_last_name

    @property
    def score(self):
        """Gets the score of this PersonalNameParsedOut.  # noqa: E501


        :return: The score of this PersonalNameParsedOut.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this PersonalNameParsedOut.


        :param score: The score of this PersonalNameParsedOut.  # noqa: E501
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
        if not isinstance(other, PersonalNameParsedOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
