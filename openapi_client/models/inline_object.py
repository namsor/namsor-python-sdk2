# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.9
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineObject(object):
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
        'stripe_token': 'str',
        'stripe_email': 'str'
    }

    attribute_map = {
        'stripe_token': 'stripeToken',
        'stripe_email': 'stripeEmail'
    }

    def __init__(self, stripe_token=None, stripe_email=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI"""  # noqa: E501

        self._stripe_token = None
        self._stripe_email = None
        self.discriminator = None

        if stripe_token is not None:
            self.stripe_token = stripe_token
        if stripe_email is not None:
            self.stripe_email = stripe_email

    @property
    def stripe_token(self):
        """Gets the stripe_token of this InlineObject.  # noqa: E501


        :return: The stripe_token of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._stripe_token

    @stripe_token.setter
    def stripe_token(self, stripe_token):
        """Sets the stripe_token of this InlineObject.


        :param stripe_token: The stripe_token of this InlineObject.  # noqa: E501
        :type: str
        """

        self._stripe_token = stripe_token

    @property
    def stripe_email(self):
        """Gets the stripe_email of this InlineObject.  # noqa: E501


        :return: The stripe_email of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._stripe_email

    @stripe_email.setter
    def stripe_email(self, stripe_email):
        """Sets the stripe_email of this InlineObject.


        :param stripe_email: The stripe_email of this InlineObject.  # noqa: E501
        :type: str
        """

        self._stripe_email = stripe_email

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
        if not isinstance(other, InlineObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
