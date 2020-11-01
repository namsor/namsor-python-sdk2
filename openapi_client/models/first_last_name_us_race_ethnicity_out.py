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


class FirstLastNameUSRaceEthnicityOut(object):
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
        'id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'race_ethnicity_alt': 'str',
        'race_ethnicity': 'str',
        'score': 'float',
        'race_ethnicities_top': 'list[str]',
        'probability_calibrated': 'float',
        'probability_alt_calibrated': 'float'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'race_ethnicity_alt': 'raceEthnicityAlt',
        'race_ethnicity': 'raceEthnicity',
        'score': 'score',
        'race_ethnicities_top': 'raceEthnicitiesTop',
        'probability_calibrated': 'probabilityCalibrated',
        'probability_alt_calibrated': 'probabilityAltCalibrated'
    }

    def __init__(self, id=None, first_name=None, last_name=None, race_ethnicity_alt=None, race_ethnicity=None, score=None, race_ethnicities_top=None, probability_calibrated=None, probability_alt_calibrated=None):  # noqa: E501
        """FirstLastNameUSRaceEthnicityOut - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._first_name = None
        self._last_name = None
        self._race_ethnicity_alt = None
        self._race_ethnicity = None
        self._score = None
        self._race_ethnicities_top = None
        self._probability_calibrated = None
        self._probability_alt_calibrated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if race_ethnicity_alt is not None:
            self.race_ethnicity_alt = race_ethnicity_alt
        if race_ethnicity is not None:
            self.race_ethnicity = race_ethnicity
        if score is not None:
            self.score = score
        if race_ethnicities_top is not None:
            self.race_ethnicities_top = race_ethnicities_top
        if probability_calibrated is not None:
            self.probability_calibrated = probability_calibrated
        if probability_alt_calibrated is not None:
            self.probability_alt_calibrated = probability_alt_calibrated

    @property
    def id(self):
        """Gets the id of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501


        :return: The id of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FirstLastNameUSRaceEthnicityOut.


        :param id: The id of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501


        :return: The first_name of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this FirstLastNameUSRaceEthnicityOut.


        :param first_name: The first_name of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501


        :return: The last_name of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this FirstLastNameUSRaceEthnicityOut.


        :param last_name: The last_name of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def race_ethnicity_alt(self):
        """Gets the race_ethnicity_alt of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501

        Second most likely US 'race'/ethnicity  # noqa: E501

        :return: The race_ethnicity_alt of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :rtype: str
        """
        return self._race_ethnicity_alt

    @race_ethnicity_alt.setter
    def race_ethnicity_alt(self, race_ethnicity_alt):
        """Sets the race_ethnicity_alt of this FirstLastNameUSRaceEthnicityOut.

        Second most likely US 'race'/ethnicity  # noqa: E501

        :param race_ethnicity_alt: The race_ethnicity_alt of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :type: str
        """
        allowed_values = ["W_NL", "HL", "A", "B_NL"]  # noqa: E501
        if race_ethnicity_alt not in allowed_values:
            raise ValueError(
                "Invalid value for `race_ethnicity_alt` ({0}), must be one of {1}"  # noqa: E501
                .format(race_ethnicity_alt, allowed_values)
            )

        self._race_ethnicity_alt = race_ethnicity_alt

    @property
    def race_ethnicity(self):
        """Gets the race_ethnicity of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501

        Most likely US 'race'/ethnicity  # noqa: E501

        :return: The race_ethnicity of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :rtype: str
        """
        return self._race_ethnicity

    @race_ethnicity.setter
    def race_ethnicity(self, race_ethnicity):
        """Sets the race_ethnicity of this FirstLastNameUSRaceEthnicityOut.

        Most likely US 'race'/ethnicity  # noqa: E501

        :param race_ethnicity: The race_ethnicity of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :type: str
        """
        allowed_values = ["W_NL", "HL", "A", "B_NL"]  # noqa: E501
        if race_ethnicity not in allowed_values:
            raise ValueError(
                "Invalid value for `race_ethnicity` ({0}), must be one of {1}"  # noqa: E501
                .format(race_ethnicity, allowed_values)
            )

        self._race_ethnicity = race_ethnicity

    @property
    def score(self):
        """Gets the score of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501

        Compatibility to NamSor_v1 Origin score value  # noqa: E501

        :return: The score of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this FirstLastNameUSRaceEthnicityOut.

        Compatibility to NamSor_v1 Origin score value  # noqa: E501

        :param score: The score of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def race_ethnicities_top(self):
        """Gets the race_ethnicities_top of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501

        List 'race'/ethnicities  # noqa: E501

        :return: The race_ethnicities_top of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :rtype: list[str]
        """
        return self._race_ethnicities_top

    @race_ethnicities_top.setter
    def race_ethnicities_top(self, race_ethnicities_top):
        """Sets the race_ethnicities_top of this FirstLastNameUSRaceEthnicityOut.

        List 'race'/ethnicities  # noqa: E501

        :param race_ethnicities_top: The race_ethnicities_top of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :type: list[str]
        """

        self._race_ethnicities_top = race_ethnicities_top

    @property
    def probability_calibrated(self):
        """Gets the probability_calibrated of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501


        :return: The probability_calibrated of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :rtype: float
        """
        return self._probability_calibrated

    @probability_calibrated.setter
    def probability_calibrated(self, probability_calibrated):
        """Sets the probability_calibrated of this FirstLastNameUSRaceEthnicityOut.


        :param probability_calibrated: The probability_calibrated of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :type: float
        """

        self._probability_calibrated = probability_calibrated

    @property
    def probability_alt_calibrated(self):
        """Gets the probability_alt_calibrated of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501


        :return: The probability_alt_calibrated of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :rtype: float
        """
        return self._probability_alt_calibrated

    @probability_alt_calibrated.setter
    def probability_alt_calibrated(self, probability_alt_calibrated):
        """Sets the probability_alt_calibrated of this FirstLastNameUSRaceEthnicityOut.


        :param probability_alt_calibrated: The probability_alt_calibrated of this FirstLastNameUSRaceEthnicityOut.  # noqa: E501
        :type: float
        """

        self._probability_alt_calibrated = probability_alt_calibrated

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
        if not isinstance(other, FirstLastNameUSRaceEthnicityOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
