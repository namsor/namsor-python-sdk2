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


class APIClassifierTaxonomyOut(object):
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
        'classifier_name': 'str',
        'taxonomy_classes': 'list[str]'
    }

    attribute_map = {
        'classifier_name': 'classifierName',
        'taxonomy_classes': 'taxonomyClasses'
    }

    def __init__(self, classifier_name=None, taxonomy_classes=None):  # noqa: E501
        """APIClassifierTaxonomyOut - a model defined in OpenAPI"""  # noqa: E501

        self._classifier_name = None
        self._taxonomy_classes = None
        self.discriminator = None

        if classifier_name is not None:
            self.classifier_name = classifier_name
        if taxonomy_classes is not None:
            self.taxonomy_classes = taxonomy_classes

    @property
    def classifier_name(self):
        """Gets the classifier_name of this APIClassifierTaxonomyOut.  # noqa: E501


        :return: The classifier_name of this APIClassifierTaxonomyOut.  # noqa: E501
        :rtype: str
        """
        return self._classifier_name

    @classifier_name.setter
    def classifier_name(self, classifier_name):
        """Sets the classifier_name of this APIClassifierTaxonomyOut.


        :param classifier_name: The classifier_name of this APIClassifierTaxonomyOut.  # noqa: E501
        :type: str
        """

        self._classifier_name = classifier_name

    @property
    def taxonomy_classes(self):
        """Gets the taxonomy_classes of this APIClassifierTaxonomyOut.  # noqa: E501


        :return: The taxonomy_classes of this APIClassifierTaxonomyOut.  # noqa: E501
        :rtype: list[str]
        """
        return self._taxonomy_classes

    @taxonomy_classes.setter
    def taxonomy_classes(self, taxonomy_classes):
        """Sets the taxonomy_classes of this APIClassifierTaxonomyOut.


        :param taxonomy_classes: The taxonomy_classes of this APIClassifierTaxonomyOut.  # noqa: E501
        :type: list[str]
        """

        self._taxonomy_classes = taxonomy_classes

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
        if not isinstance(other, APIClassifierTaxonomyOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
