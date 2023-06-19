# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. By default, enpoints use 1 unit per name (ex. Gender), but Ethnicity classification uses 10 to 20 units per name depending on taxonomy. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.26
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FeedbackLoopOut(object):
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
        'feedback_credits': 'int'
    }

    attribute_map = {
        'feedback_credits': 'feedbackCredits'
    }

    def __init__(self, feedback_credits=None):  # noqa: E501
        """FeedbackLoopOut - a model defined in OpenAPI"""  # noqa: E501

        self._feedback_credits = None
        self.discriminator = None

        if feedback_credits is not None:
            self.feedback_credits = feedback_credits

    @property
    def feedback_credits(self):
        """Gets the feedback_credits of this FeedbackLoopOut.  # noqa: E501

        Number of units recredited as per feedback loop successful classification  # noqa: E501

        :return: The feedback_credits of this FeedbackLoopOut.  # noqa: E501
        :rtype: int
        """
        return self._feedback_credits

    @feedback_credits.setter
    def feedback_credits(self, feedback_credits):
        """Sets the feedback_credits of this FeedbackLoopOut.

        Number of units recredited as per feedback loop successful classification  # noqa: E501

        :param feedback_credits: The feedback_credits of this FeedbackLoopOut.  # noqa: E501
        :type: int
        """

        self._feedback_credits = feedback_credits

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
        if not isinstance(other, FeedbackLoopOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
