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


class APIClassifiersStatusOut(object):
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
        'software_version': 'SoftwareVersionOut',
        'classifiers': 'list[APIClassifierOut]'
    }

    attribute_map = {
        'software_version': 'softwareVersion',
        'classifiers': 'classifiers'
    }

    def __init__(self, software_version=None, classifiers=None):  # noqa: E501
        """APIClassifiersStatusOut - a model defined in OpenAPI"""  # noqa: E501

        self._software_version = None
        self._classifiers = None
        self.discriminator = None

        if software_version is not None:
            self.software_version = software_version
        if classifiers is not None:
            self.classifiers = classifiers

    @property
    def software_version(self):
        """Gets the software_version of this APIClassifiersStatusOut.  # noqa: E501


        :return: The software_version of this APIClassifiersStatusOut.  # noqa: E501
        :rtype: SoftwareVersionOut
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this APIClassifiersStatusOut.


        :param software_version: The software_version of this APIClassifiersStatusOut.  # noqa: E501
        :type: SoftwareVersionOut
        """

        self._software_version = software_version

    @property
    def classifiers(self):
        """Gets the classifiers of this APIClassifiersStatusOut.  # noqa: E501


        :return: The classifiers of this APIClassifiersStatusOut.  # noqa: E501
        :rtype: list[APIClassifierOut]
        """
        return self._classifiers

    @classifiers.setter
    def classifiers(self, classifiers):
        """Sets the classifiers of this APIClassifiersStatusOut.


        :param classifiers: The classifiers of this APIClassifiersStatusOut.  # noqa: E501
        :type: list[APIClassifierOut]
        """

        self._classifiers = classifiers

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
        if not isinstance(other, APIClassifiersStatusOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
