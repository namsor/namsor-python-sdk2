# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.13
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CorridorOut(object):
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
        'first_last_name_gendered_out': 'FirstLastNameGenderedOut',
        'first_last_name_origined_out': 'FirstLastNameOriginedOut',
        'first_last_name_diasporaed_out': 'FirstLastNameDiasporaedOut',
        'script': 'str',
        'category': 'str'
    }

    attribute_map = {
        'id': 'id',
        'first_last_name_gendered_out': 'FirstLastNameGenderedOut',
        'first_last_name_origined_out': 'FirstLastNameOriginedOut',
        'first_last_name_diasporaed_out': 'FirstLastNameDiasporaedOut',
        'script': 'script',
        'category': 'category'
    }

    def __init__(self, id=None, first_last_name_gendered_out=None, first_last_name_origined_out=None, first_last_name_diasporaed_out=None, script=None, category=None):  # noqa: E501
        """CorridorOut - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._first_last_name_gendered_out = None
        self._first_last_name_origined_out = None
        self._first_last_name_diasporaed_out = None
        self._script = None
        self._category = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if first_last_name_gendered_out is not None:
            self.first_last_name_gendered_out = first_last_name_gendered_out
        if first_last_name_origined_out is not None:
            self.first_last_name_origined_out = first_last_name_origined_out
        if first_last_name_diasporaed_out is not None:
            self.first_last_name_diasporaed_out = first_last_name_diasporaed_out
        if script is not None:
            self.script = script
        if category is not None:
            self.category = category

    @property
    def id(self):
        """Gets the id of this CorridorOut.  # noqa: E501


        :return: The id of this CorridorOut.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CorridorOut.


        :param id: The id of this CorridorOut.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def first_last_name_gendered_out(self):
        """Gets the first_last_name_gendered_out of this CorridorOut.  # noqa: E501


        :return: The first_last_name_gendered_out of this CorridorOut.  # noqa: E501
        :rtype: FirstLastNameGenderedOut
        """
        return self._first_last_name_gendered_out

    @first_last_name_gendered_out.setter
    def first_last_name_gendered_out(self, first_last_name_gendered_out):
        """Sets the first_last_name_gendered_out of this CorridorOut.


        :param first_last_name_gendered_out: The first_last_name_gendered_out of this CorridorOut.  # noqa: E501
        :type: FirstLastNameGenderedOut
        """

        self._first_last_name_gendered_out = first_last_name_gendered_out

    @property
    def first_last_name_origined_out(self):
        """Gets the first_last_name_origined_out of this CorridorOut.  # noqa: E501


        :return: The first_last_name_origined_out of this CorridorOut.  # noqa: E501
        :rtype: FirstLastNameOriginedOut
        """
        return self._first_last_name_origined_out

    @first_last_name_origined_out.setter
    def first_last_name_origined_out(self, first_last_name_origined_out):
        """Sets the first_last_name_origined_out of this CorridorOut.


        :param first_last_name_origined_out: The first_last_name_origined_out of this CorridorOut.  # noqa: E501
        :type: FirstLastNameOriginedOut
        """

        self._first_last_name_origined_out = first_last_name_origined_out

    @property
    def first_last_name_diasporaed_out(self):
        """Gets the first_last_name_diasporaed_out of this CorridorOut.  # noqa: E501


        :return: The first_last_name_diasporaed_out of this CorridorOut.  # noqa: E501
        :rtype: FirstLastNameDiasporaedOut
        """
        return self._first_last_name_diasporaed_out

    @first_last_name_diasporaed_out.setter
    def first_last_name_diasporaed_out(self, first_last_name_diasporaed_out):
        """Sets the first_last_name_diasporaed_out of this CorridorOut.


        :param first_last_name_diasporaed_out: The first_last_name_diasporaed_out of this CorridorOut.  # noqa: E501
        :type: FirstLastNameDiasporaedOut
        """

        self._first_last_name_diasporaed_out = first_last_name_diasporaed_out

    @property
    def script(self):
        """Gets the script of this CorridorOut.  # noqa: E501


        :return: The script of this CorridorOut.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this CorridorOut.


        :param script: The script of this CorridorOut.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def category(self):
        """Gets the category of this CorridorOut.  # noqa: E501


        :return: The category of this CorridorOut.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CorridorOut.


        :param category: The category of this CorridorOut.  # noqa: E501
        :type: str
        """

        self._category = category

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
        if not isinstance(other, CorridorOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
