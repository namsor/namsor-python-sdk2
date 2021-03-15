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


class NameMatchCandidateOut(object):
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
        'candidate_name': 'str',
        'probability': 'float',
        'pred_score_given_name': 'float',
        'pred_score_family_name': 'float'
    }

    attribute_map = {
        'candidate_name': 'candidateName',
        'probability': 'probability',
        'pred_score_given_name': 'predScoreGivenName',
        'pred_score_family_name': 'predScoreFamilyName'
    }

    def __init__(self, candidate_name=None, probability=None, pred_score_given_name=None, pred_score_family_name=None):  # noqa: E501
        """NameMatchCandidateOut - a model defined in OpenAPI"""  # noqa: E501

        self._candidate_name = None
        self._probability = None
        self._pred_score_given_name = None
        self._pred_score_family_name = None
        self.discriminator = None

        if candidate_name is not None:
            self.candidate_name = candidate_name
        if probability is not None:
            self.probability = probability
        if pred_score_given_name is not None:
            self.pred_score_given_name = pred_score_given_name
        if pred_score_family_name is not None:
            self.pred_score_family_name = pred_score_family_name

    @property
    def candidate_name(self):
        """Gets the candidate_name of this NameMatchCandidateOut.  # noqa: E501


        :return: The candidate_name of this NameMatchCandidateOut.  # noqa: E501
        :rtype: str
        """
        return self._candidate_name

    @candidate_name.setter
    def candidate_name(self, candidate_name):
        """Sets the candidate_name of this NameMatchCandidateOut.


        :param candidate_name: The candidate_name of this NameMatchCandidateOut.  # noqa: E501
        :type: str
        """

        self._candidate_name = candidate_name

    @property
    def probability(self):
        """Gets the probability of this NameMatchCandidateOut.  # noqa: E501


        :return: The probability of this NameMatchCandidateOut.  # noqa: E501
        :rtype: float
        """
        return self._probability

    @probability.setter
    def probability(self, probability):
        """Sets the probability of this NameMatchCandidateOut.


        :param probability: The probability of this NameMatchCandidateOut.  # noqa: E501
        :type: float
        """

        self._probability = probability

    @property
    def pred_score_given_name(self):
        """Gets the pred_score_given_name of this NameMatchCandidateOut.  # noqa: E501


        :return: The pred_score_given_name of this NameMatchCandidateOut.  # noqa: E501
        :rtype: float
        """
        return self._pred_score_given_name

    @pred_score_given_name.setter
    def pred_score_given_name(self, pred_score_given_name):
        """Sets the pred_score_given_name of this NameMatchCandidateOut.


        :param pred_score_given_name: The pred_score_given_name of this NameMatchCandidateOut.  # noqa: E501
        :type: float
        """

        self._pred_score_given_name = pred_score_given_name

    @property
    def pred_score_family_name(self):
        """Gets the pred_score_family_name of this NameMatchCandidateOut.  # noqa: E501


        :return: The pred_score_family_name of this NameMatchCandidateOut.  # noqa: E501
        :rtype: float
        """
        return self._pred_score_family_name

    @pred_score_family_name.setter
    def pred_score_family_name(self, pred_score_family_name):
        """Sets the pred_score_family_name of this NameMatchCandidateOut.


        :param pred_score_family_name: The pred_score_family_name of this NameMatchCandidateOut.  # noqa: E501
        :type: float
        """

        self._pred_score_family_name = pred_score_family_name

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
        if not isinstance(other, NameMatchCandidateOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
