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


class BillingInfoInOut(object):
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
        'billing_email': 'str',
        'preferred_currency': 'str',
        'customer_name': 'str',
        'customer_phone': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'address_city': 'str',
        'address_postal_code': 'str',
        'address_state': 'str',
        'address_country': 'str',
        'vat_id': 'str'
    }

    attribute_map = {
        'billing_email': 'billingEmail',
        'preferred_currency': 'preferredCurrency',
        'customer_name': 'customerName',
        'customer_phone': 'customerPhone',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'address_city': 'addressCity',
        'address_postal_code': 'addressPostalCode',
        'address_state': 'addressState',
        'address_country': 'addressCountry',
        'vat_id': 'vatID'
    }

    def __init__(self, billing_email=None, preferred_currency=None, customer_name=None, customer_phone=None, address_line1=None, address_line2=None, address_city=None, address_postal_code=None, address_state=None, address_country=None, vat_id=None):  # noqa: E501
        """BillingInfoInOut - a model defined in OpenAPI"""  # noqa: E501

        self._billing_email = None
        self._preferred_currency = None
        self._customer_name = None
        self._customer_phone = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_city = None
        self._address_postal_code = None
        self._address_state = None
        self._address_country = None
        self._vat_id = None
        self.discriminator = None

        if billing_email is not None:
            self.billing_email = billing_email
        if preferred_currency is not None:
            self.preferred_currency = preferred_currency
        if customer_name is not None:
            self.customer_name = customer_name
        if customer_phone is not None:
            self.customer_phone = customer_phone
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if address_city is not None:
            self.address_city = address_city
        if address_postal_code is not None:
            self.address_postal_code = address_postal_code
        if address_state is not None:
            self.address_state = address_state
        if address_country is not None:
            self.address_country = address_country
        if vat_id is not None:
            self.vat_id = vat_id

    @property
    def billing_email(self):
        """Gets the billing_email of this BillingInfoInOut.  # noqa: E501


        :return: The billing_email of this BillingInfoInOut.  # noqa: E501
        :rtype: str
        """
        return self._billing_email

    @billing_email.setter
    def billing_email(self, billing_email):
        """Sets the billing_email of this BillingInfoInOut.


        :param billing_email: The billing_email of this BillingInfoInOut.  # noqa: E501
        :type: str
        """

        self._billing_email = billing_email

    @property
    def preferred_currency(self):
        """Gets the preferred_currency of this BillingInfoInOut.  # noqa: E501


        :return: The preferred_currency of this BillingInfoInOut.  # noqa: E501
        :rtype: str
        """
        return self._preferred_currency

    @preferred_currency.setter
    def preferred_currency(self, preferred_currency):
        """Sets the preferred_currency of this BillingInfoInOut.


        :param preferred_currency: The preferred_currency of this BillingInfoInOut.  # noqa: E501
        :type: str
        """

        self._preferred_currency = preferred_currency

    @property
    def customer_name(self):
        """Gets the customer_name of this BillingInfoInOut.  # noqa: E501


        :return: The customer_name of this BillingInfoInOut.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this BillingInfoInOut.


        :param customer_name: The customer_name of this BillingInfoInOut.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def customer_phone(self):
        """Gets the customer_phone of this BillingInfoInOut.  # noqa: E501


        :return: The customer_phone of this BillingInfoInOut.  # noqa: E501
        :rtype: str
        """
        return self._customer_phone

    @customer_phone.setter
    def customer_phone(self, customer_phone):
        """Sets the customer_phone of this BillingInfoInOut.


        :param customer_phone: The customer_phone of this BillingInfoInOut.  # noqa: E501
        :type: str
        """

        self._customer_phone = customer_phone

    @property
    def address_line1(self):
        """Gets the address_line1 of this BillingInfoInOut.  # noqa: E501


        :return: The address_line1 of this BillingInfoInOut.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this BillingInfoInOut.


        :param address_line1: The address_line1 of this BillingInfoInOut.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this BillingInfoInOut.  # noqa: E501


        :return: The address_line2 of this BillingInfoInOut.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this BillingInfoInOut.


        :param address_line2: The address_line2 of this BillingInfoInOut.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def address_city(self):
        """Gets the address_city of this BillingInfoInOut.  # noqa: E501


        :return: The address_city of this BillingInfoInOut.  # noqa: E501
        :rtype: str
        """
        return self._address_city

    @address_city.setter
    def address_city(self, address_city):
        """Sets the address_city of this BillingInfoInOut.


        :param address_city: The address_city of this BillingInfoInOut.  # noqa: E501
        :type: str
        """

        self._address_city = address_city

    @property
    def address_postal_code(self):
        """Gets the address_postal_code of this BillingInfoInOut.  # noqa: E501


        :return: The address_postal_code of this BillingInfoInOut.  # noqa: E501
        :rtype: str
        """
        return self._address_postal_code

    @address_postal_code.setter
    def address_postal_code(self, address_postal_code):
        """Sets the address_postal_code of this BillingInfoInOut.


        :param address_postal_code: The address_postal_code of this BillingInfoInOut.  # noqa: E501
        :type: str
        """

        self._address_postal_code = address_postal_code

    @property
    def address_state(self):
        """Gets the address_state of this BillingInfoInOut.  # noqa: E501


        :return: The address_state of this BillingInfoInOut.  # noqa: E501
        :rtype: str
        """
        return self._address_state

    @address_state.setter
    def address_state(self, address_state):
        """Sets the address_state of this BillingInfoInOut.


        :param address_state: The address_state of this BillingInfoInOut.  # noqa: E501
        :type: str
        """

        self._address_state = address_state

    @property
    def address_country(self):
        """Gets the address_country of this BillingInfoInOut.  # noqa: E501


        :return: The address_country of this BillingInfoInOut.  # noqa: E501
        :rtype: str
        """
        return self._address_country

    @address_country.setter
    def address_country(self, address_country):
        """Sets the address_country of this BillingInfoInOut.


        :param address_country: The address_country of this BillingInfoInOut.  # noqa: E501
        :type: str
        """

        self._address_country = address_country

    @property
    def vat_id(self):
        """Gets the vat_id of this BillingInfoInOut.  # noqa: E501


        :return: The vat_id of this BillingInfoInOut.  # noqa: E501
        :rtype: str
        """
        return self._vat_id

    @vat_id.setter
    def vat_id(self, vat_id):
        """Sets the vat_id of this BillingInfoInOut.


        :param vat_id: The vat_id of this BillingInfoInOut.  # noqa: E501
        :type: str
        """

        self._vat_id = vat_id

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
        if not isinstance(other, BillingInfoInOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
