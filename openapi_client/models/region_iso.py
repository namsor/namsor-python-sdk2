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


class RegionISO(object):
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
        'country_name': 'str',
        'country_num_code': 'str',
        'country_iso2': 'str',
        'country_iso3': 'str',
        'country_fips': 'str',
        'subregion': 'str',
        'region': 'str',
        'topregion': 'str'
    }

    attribute_map = {
        'country_name': 'countryName',
        'country_num_code': 'countryNumCode',
        'country_iso2': 'countryISO2',
        'country_iso3': 'countryISO3',
        'country_fips': 'countryFIPS',
        'subregion': 'subregion',
        'region': 'region',
        'topregion': 'topregion'
    }

    def __init__(self, country_name=None, country_num_code=None, country_iso2=None, country_iso3=None, country_fips=None, subregion=None, region=None, topregion=None):  # noqa: E501
        """RegionISO - a model defined in OpenAPI"""  # noqa: E501

        self._country_name = None
        self._country_num_code = None
        self._country_iso2 = None
        self._country_iso3 = None
        self._country_fips = None
        self._subregion = None
        self._region = None
        self._topregion = None
        self.discriminator = None

        if country_name is not None:
            self.country_name = country_name
        if country_num_code is not None:
            self.country_num_code = country_num_code
        if country_iso2 is not None:
            self.country_iso2 = country_iso2
        if country_iso3 is not None:
            self.country_iso3 = country_iso3
        if country_fips is not None:
            self.country_fips = country_fips
        if subregion is not None:
            self.subregion = subregion
        if region is not None:
            self.region = region
        if topregion is not None:
            self.topregion = topregion

    @property
    def country_name(self):
        """Gets the country_name of this RegionISO.  # noqa: E501


        :return: The country_name of this RegionISO.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this RegionISO.


        :param country_name: The country_name of this RegionISO.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

    @property
    def country_num_code(self):
        """Gets the country_num_code of this RegionISO.  # noqa: E501


        :return: The country_num_code of this RegionISO.  # noqa: E501
        :rtype: str
        """
        return self._country_num_code

    @country_num_code.setter
    def country_num_code(self, country_num_code):
        """Sets the country_num_code of this RegionISO.


        :param country_num_code: The country_num_code of this RegionISO.  # noqa: E501
        :type: str
        """

        self._country_num_code = country_num_code

    @property
    def country_iso2(self):
        """Gets the country_iso2 of this RegionISO.  # noqa: E501


        :return: The country_iso2 of this RegionISO.  # noqa: E501
        :rtype: str
        """
        return self._country_iso2

    @country_iso2.setter
    def country_iso2(self, country_iso2):
        """Sets the country_iso2 of this RegionISO.


        :param country_iso2: The country_iso2 of this RegionISO.  # noqa: E501
        :type: str
        """

        self._country_iso2 = country_iso2

    @property
    def country_iso3(self):
        """Gets the country_iso3 of this RegionISO.  # noqa: E501


        :return: The country_iso3 of this RegionISO.  # noqa: E501
        :rtype: str
        """
        return self._country_iso3

    @country_iso3.setter
    def country_iso3(self, country_iso3):
        """Sets the country_iso3 of this RegionISO.


        :param country_iso3: The country_iso3 of this RegionISO.  # noqa: E501
        :type: str
        """

        self._country_iso3 = country_iso3

    @property
    def country_fips(self):
        """Gets the country_fips of this RegionISO.  # noqa: E501


        :return: The country_fips of this RegionISO.  # noqa: E501
        :rtype: str
        """
        return self._country_fips

    @country_fips.setter
    def country_fips(self, country_fips):
        """Sets the country_fips of this RegionISO.


        :param country_fips: The country_fips of this RegionISO.  # noqa: E501
        :type: str
        """

        self._country_fips = country_fips

    @property
    def subregion(self):
        """Gets the subregion of this RegionISO.  # noqa: E501


        :return: The subregion of this RegionISO.  # noqa: E501
        :rtype: str
        """
        return self._subregion

    @subregion.setter
    def subregion(self, subregion):
        """Sets the subregion of this RegionISO.


        :param subregion: The subregion of this RegionISO.  # noqa: E501
        :type: str
        """

        self._subregion = subregion

    @property
    def region(self):
        """Gets the region of this RegionISO.  # noqa: E501


        :return: The region of this RegionISO.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this RegionISO.


        :param region: The region of this RegionISO.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def topregion(self):
        """Gets the topregion of this RegionISO.  # noqa: E501


        :return: The topregion of this RegionISO.  # noqa: E501
        :rtype: str
        """
        return self._topregion

    @topregion.setter
    def topregion(self, topregion):
        """Sets the topregion of this RegionISO.


        :param topregion: The topregion of this RegionISO.  # noqa: E501
        :type: str
        """

        self._topregion = topregion

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
        if not isinstance(other, RegionISO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
