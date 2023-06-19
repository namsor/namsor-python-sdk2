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


class BatchNameMatchCandidatesOut(object):
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
        'names_and_match_candidates': 'list[NameMatchCandidatesOut]'
    }

    attribute_map = {
        'names_and_match_candidates': 'namesAndMatchCandidates'
    }

    def __init__(self, names_and_match_candidates=None):  # noqa: E501
        """BatchNameMatchCandidatesOut - a model defined in OpenAPI"""  # noqa: E501

        self._names_and_match_candidates = None
        self.discriminator = None

        if names_and_match_candidates is not None:
            self.names_and_match_candidates = names_and_match_candidates

    @property
    def names_and_match_candidates(self):
        """Gets the names_and_match_candidates of this BatchNameMatchCandidatesOut.  # noqa: E501

        Classified matched names  # noqa: E501

        :return: The names_and_match_candidates of this BatchNameMatchCandidatesOut.  # noqa: E501
        :rtype: list[NameMatchCandidatesOut]
        """
        return self._names_and_match_candidates

    @names_and_match_candidates.setter
    def names_and_match_candidates(self, names_and_match_candidates):
        """Sets the names_and_match_candidates of this BatchNameMatchCandidatesOut.

        Classified matched names  # noqa: E501

        :param names_and_match_candidates: The names_and_match_candidates of this BatchNameMatchCandidatesOut.  # noqa: E501
        :type: list[NameMatchCandidatesOut]
        """

        self._names_and_match_candidates = names_and_match_candidates

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
        if not isinstance(other, BatchNameMatchCandidatesOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
