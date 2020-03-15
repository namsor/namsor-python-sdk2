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


class StripeCustomerOut(object):
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
        'stripe_customer_id': 'str',
        'source_country': 'str',
        'source_currency': 'str',
        'striped_cards': 'list[StripeCardOut]'
    }

    attribute_map = {
        'stripe_customer_id': 'stripeCustomerId',
        'source_country': 'sourceCountry',
        'source_currency': 'sourceCurrency',
        'striped_cards': 'stripedCards'
    }

    def __init__(self, stripe_customer_id=None, source_country=None, source_currency=None, striped_cards=None):  # noqa: E501
        """StripeCustomerOut - a model defined in OpenAPI"""  # noqa: E501

        self._stripe_customer_id = None
        self._source_country = None
        self._source_currency = None
        self._striped_cards = None
        self.discriminator = None

        if stripe_customer_id is not None:
            self.stripe_customer_id = stripe_customer_id
        if source_country is not None:
            self.source_country = source_country
        if source_currency is not None:
            self.source_currency = source_currency
        if striped_cards is not None:
            self.striped_cards = striped_cards

    @property
    def stripe_customer_id(self):
        """Gets the stripe_customer_id of this StripeCustomerOut.  # noqa: E501


        :return: The stripe_customer_id of this StripeCustomerOut.  # noqa: E501
        :rtype: str
        """
        return self._stripe_customer_id

    @stripe_customer_id.setter
    def stripe_customer_id(self, stripe_customer_id):
        """Sets the stripe_customer_id of this StripeCustomerOut.


        :param stripe_customer_id: The stripe_customer_id of this StripeCustomerOut.  # noqa: E501
        :type: str
        """

        self._stripe_customer_id = stripe_customer_id

    @property
    def source_country(self):
        """Gets the source_country of this StripeCustomerOut.  # noqa: E501


        :return: The source_country of this StripeCustomerOut.  # noqa: E501
        :rtype: str
        """
        return self._source_country

    @source_country.setter
    def source_country(self, source_country):
        """Sets the source_country of this StripeCustomerOut.


        :param source_country: The source_country of this StripeCustomerOut.  # noqa: E501
        :type: str
        """

        self._source_country = source_country

    @property
    def source_currency(self):
        """Gets the source_currency of this StripeCustomerOut.  # noqa: E501


        :return: The source_currency of this StripeCustomerOut.  # noqa: E501
        :rtype: str
        """
        return self._source_currency

    @source_currency.setter
    def source_currency(self, source_currency):
        """Sets the source_currency of this StripeCustomerOut.


        :param source_currency: The source_currency of this StripeCustomerOut.  # noqa: E501
        :type: str
        """

        self._source_currency = source_currency

    @property
    def striped_cards(self):
        """Gets the striped_cards of this StripeCustomerOut.  # noqa: E501


        :return: The striped_cards of this StripeCustomerOut.  # noqa: E501
        :rtype: list[StripeCardOut]
        """
        return self._striped_cards

    @striped_cards.setter
    def striped_cards(self, striped_cards):
        """Sets the striped_cards of this StripeCustomerOut.


        :param striped_cards: The striped_cards of this StripeCustomerOut.  # noqa: E501
        :type: list[StripeCardOut]
        """

        self._striped_cards = striped_cards

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
        if not isinstance(other, StripeCustomerOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
