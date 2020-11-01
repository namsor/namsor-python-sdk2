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


class APIClassifierOut(object):
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
        'serving': 'bool',
        'learning': 'bool',
        'shutting_down': 'bool',
        'probability_calibrated': 'bool'
    }

    attribute_map = {
        'classifier_name': 'classifierName',
        'serving': 'serving',
        'learning': 'learning',
        'shutting_down': 'shuttingDown',
        'probability_calibrated': 'probabilityCalibrated'
    }

    def __init__(self, classifier_name=None, serving=None, learning=None, shutting_down=None, probability_calibrated=None):  # noqa: E501
        """APIClassifierOut - a model defined in OpenAPI"""  # noqa: E501

        self._classifier_name = None
        self._serving = None
        self._learning = None
        self._shutting_down = None
        self._probability_calibrated = None
        self.discriminator = None

        if classifier_name is not None:
            self.classifier_name = classifier_name
        if serving is not None:
            self.serving = serving
        if learning is not None:
            self.learning = learning
        if shutting_down is not None:
            self.shutting_down = shutting_down
        if probability_calibrated is not None:
            self.probability_calibrated = probability_calibrated

    @property
    def classifier_name(self):
        """Gets the classifier_name of this APIClassifierOut.  # noqa: E501


        :return: The classifier_name of this APIClassifierOut.  # noqa: E501
        :rtype: str
        """
        return self._classifier_name

    @classifier_name.setter
    def classifier_name(self, classifier_name):
        """Sets the classifier_name of this APIClassifierOut.


        :param classifier_name: The classifier_name of this APIClassifierOut.  # noqa: E501
        :type: str
        """

        self._classifier_name = classifier_name

    @property
    def serving(self):
        """Gets the serving of this APIClassifierOut.  # noqa: E501


        :return: The serving of this APIClassifierOut.  # noqa: E501
        :rtype: bool
        """
        return self._serving

    @serving.setter
    def serving(self, serving):
        """Sets the serving of this APIClassifierOut.


        :param serving: The serving of this APIClassifierOut.  # noqa: E501
        :type: bool
        """

        self._serving = serving

    @property
    def learning(self):
        """Gets the learning of this APIClassifierOut.  # noqa: E501


        :return: The learning of this APIClassifierOut.  # noqa: E501
        :rtype: bool
        """
        return self._learning

    @learning.setter
    def learning(self, learning):
        """Sets the learning of this APIClassifierOut.


        :param learning: The learning of this APIClassifierOut.  # noqa: E501
        :type: bool
        """

        self._learning = learning

    @property
    def shutting_down(self):
        """Gets the shutting_down of this APIClassifierOut.  # noqa: E501


        :return: The shutting_down of this APIClassifierOut.  # noqa: E501
        :rtype: bool
        """
        return self._shutting_down

    @shutting_down.setter
    def shutting_down(self, shutting_down):
        """Sets the shutting_down of this APIClassifierOut.


        :param shutting_down: The shutting_down of this APIClassifierOut.  # noqa: E501
        :type: bool
        """

        self._shutting_down = shutting_down

    @property
    def probability_calibrated(self):
        """Gets the probability_calibrated of this APIClassifierOut.  # noqa: E501


        :return: The probability_calibrated of this APIClassifierOut.  # noqa: E501
        :rtype: bool
        """
        return self._probability_calibrated

    @probability_calibrated.setter
    def probability_calibrated(self, probability_calibrated):
        """Sets the probability_calibrated of this APIClassifierOut.


        :param probability_calibrated: The probability_calibrated of this APIClassifierOut.  # noqa: E501
        :type: bool
        """

        self._probability_calibrated = probability_calibrated

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
        if not isinstance(other, APIClassifierOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
