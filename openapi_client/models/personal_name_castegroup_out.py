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


class PersonalNameCastegroupOut(object):
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
        'script': 'str',
        'id': 'str',
        'explanation': 'str',
        'name': 'str',
        'score': 'float',
        'castegroup': 'str',
        'castegroup_alt': 'str',
        'castegroup_top': 'list[str]',
        'probability_calibrated': 'float',
        'probability_alt_calibrated': 'float'
    }

    attribute_map = {
        'script': 'script',
        'id': 'id',
        'explanation': 'explanation',
        'name': 'name',
        'score': 'score',
        'castegroup': 'castegroup',
        'castegroup_alt': 'castegroupAlt',
        'castegroup_top': 'castegroupTop',
        'probability_calibrated': 'probabilityCalibrated',
        'probability_alt_calibrated': 'probabilityAltCalibrated'
    }

    def __init__(self, script=None, id=None, explanation=None, name=None, score=None, castegroup=None, castegroup_alt=None, castegroup_top=None, probability_calibrated=None, probability_alt_calibrated=None):  # noqa: E501
        """PersonalNameCastegroupOut - a model defined in OpenAPI"""  # noqa: E501

        self._script = None
        self._id = None
        self._explanation = None
        self._name = None
        self._score = None
        self._castegroup = None
        self._castegroup_alt = None
        self._castegroup_top = None
        self._probability_calibrated = None
        self._probability_alt_calibrated = None
        self.discriminator = None

        if script is not None:
            self.script = script
        if id is not None:
            self.id = id
        if explanation is not None:
            self.explanation = explanation
        if name is not None:
            self.name = name
        if score is not None:
            self.score = score
        if castegroup is not None:
            self.castegroup = castegroup
        if castegroup_alt is not None:
            self.castegroup_alt = castegroup_alt
        if castegroup_top is not None:
            self.castegroup_top = castegroup_top
        if probability_calibrated is not None:
            self.probability_calibrated = probability_calibrated
        if probability_alt_calibrated is not None:
            self.probability_alt_calibrated = probability_alt_calibrated

    @property
    def script(self):
        """Gets the script of this PersonalNameCastegroupOut.  # noqa: E501


        :return: The script of this PersonalNameCastegroupOut.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this PersonalNameCastegroupOut.


        :param script: The script of this PersonalNameCastegroupOut.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def id(self):
        """Gets the id of this PersonalNameCastegroupOut.  # noqa: E501


        :return: The id of this PersonalNameCastegroupOut.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PersonalNameCastegroupOut.


        :param id: The id of this PersonalNameCastegroupOut.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def explanation(self):
        """Gets the explanation of this PersonalNameCastegroupOut.  # noqa: E501


        :return: The explanation of this PersonalNameCastegroupOut.  # noqa: E501
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """Sets the explanation of this PersonalNameCastegroupOut.


        :param explanation: The explanation of this PersonalNameCastegroupOut.  # noqa: E501
        :type: str
        """

        self._explanation = explanation

    @property
    def name(self):
        """Gets the name of this PersonalNameCastegroupOut.  # noqa: E501

        The input name.  # noqa: E501

        :return: The name of this PersonalNameCastegroupOut.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PersonalNameCastegroupOut.

        The input name.  # noqa: E501

        :param name: The name of this PersonalNameCastegroupOut.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def score(self):
        """Gets the score of this PersonalNameCastegroupOut.  # noqa: E501

        Higher score is better, but score is not normalized. Use calibratedProbability if available.   # noqa: E501

        :return: The score of this PersonalNameCastegroupOut.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this PersonalNameCastegroupOut.

        Higher score is better, but score is not normalized. Use calibratedProbability if available.   # noqa: E501

        :param score: The score of this PersonalNameCastegroupOut.  # noqa: E501
        :type: float
        """
        if score is not None and score > 100:  # noqa: E501
            raise ValueError("Invalid value for `score`, must be a value less than or equal to `100`")  # noqa: E501
        if score is not None and score < 0:  # noqa: E501
            raise ValueError("Invalid value for `score`, must be a value greater than or equal to `0`")  # noqa: E501

        self._score = score

    @property
    def castegroup(self):
        """Gets the castegroup of this PersonalNameCastegroupOut.  # noqa: E501

        Most likely caste group  # noqa: E501

        :return: The castegroup of this PersonalNameCastegroupOut.  # noqa: E501
        :rtype: str
        """
        return self._castegroup

    @castegroup.setter
    def castegroup(self, castegroup):
        """Sets the castegroup of this PersonalNameCastegroupOut.

        Most likely caste group  # noqa: E501

        :param castegroup: The castegroup of this PersonalNameCastegroupOut.  # noqa: E501
        :type: str
        """

        self._castegroup = castegroup

    @property
    def castegroup_alt(self):
        """Gets the castegroup_alt of this PersonalNameCastegroupOut.  # noqa: E501

        Second best alternative : caste group   # noqa: E501

        :return: The castegroup_alt of this PersonalNameCastegroupOut.  # noqa: E501
        :rtype: str
        """
        return self._castegroup_alt

    @castegroup_alt.setter
    def castegroup_alt(self, castegroup_alt):
        """Sets the castegroup_alt of this PersonalNameCastegroupOut.

        Second best alternative : caste group   # noqa: E501

        :param castegroup_alt: The castegroup_alt of this PersonalNameCastegroupOut.  # noqa: E501
        :type: str
        """

        self._castegroup_alt = castegroup_alt

    @property
    def castegroup_top(self):
        """Gets the castegroup_top of this PersonalNameCastegroupOut.  # noqa: E501

        List caste group (top 10)  # noqa: E501

        :return: The castegroup_top of this PersonalNameCastegroupOut.  # noqa: E501
        :rtype: list[str]
        """
        return self._castegroup_top

    @castegroup_top.setter
    def castegroup_top(self, castegroup_top):
        """Sets the castegroup_top of this PersonalNameCastegroupOut.

        List caste group (top 10)  # noqa: E501

        :param castegroup_top: The castegroup_top of this PersonalNameCastegroupOut.  # noqa: E501
        :type: list[str]
        """

        self._castegroup_top = castegroup_top

    @property
    def probability_calibrated(self):
        """Gets the probability_calibrated of this PersonalNameCastegroupOut.  # noqa: E501

        The calibrated probability for country to have been guessed correctly. -1 = still calibrating.   # noqa: E501

        :return: The probability_calibrated of this PersonalNameCastegroupOut.  # noqa: E501
        :rtype: float
        """
        return self._probability_calibrated

    @probability_calibrated.setter
    def probability_calibrated(self, probability_calibrated):
        """Sets the probability_calibrated of this PersonalNameCastegroupOut.

        The calibrated probability for country to have been guessed correctly. -1 = still calibrating.   # noqa: E501

        :param probability_calibrated: The probability_calibrated of this PersonalNameCastegroupOut.  # noqa: E501
        :type: float
        """
        if probability_calibrated is not None and probability_calibrated > 1:  # noqa: E501
            raise ValueError("Invalid value for `probability_calibrated`, must be a value less than or equal to `1`")  # noqa: E501
        if probability_calibrated is not None and probability_calibrated < -1:  # noqa: E501
            raise ValueError("Invalid value for `probability_calibrated`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._probability_calibrated = probability_calibrated

    @property
    def probability_alt_calibrated(self):
        """Gets the probability_alt_calibrated of this PersonalNameCastegroupOut.  # noqa: E501

        The calibrated probability for country OR countryAlt to have been guessed correctly. -1 = still calibrating.   # noqa: E501

        :return: The probability_alt_calibrated of this PersonalNameCastegroupOut.  # noqa: E501
        :rtype: float
        """
        return self._probability_alt_calibrated

    @probability_alt_calibrated.setter
    def probability_alt_calibrated(self, probability_alt_calibrated):
        """Sets the probability_alt_calibrated of this PersonalNameCastegroupOut.

        The calibrated probability for country OR countryAlt to have been guessed correctly. -1 = still calibrating.   # noqa: E501

        :param probability_alt_calibrated: The probability_alt_calibrated of this PersonalNameCastegroupOut.  # noqa: E501
        :type: float
        """
        if probability_alt_calibrated is not None and probability_alt_calibrated > 1:  # noqa: E501
            raise ValueError("Invalid value for `probability_alt_calibrated`, must be a value less than or equal to `1`")  # noqa: E501
        if probability_alt_calibrated is not None and probability_alt_calibrated < -1:  # noqa: E501
            raise ValueError("Invalid value for `probability_alt_calibrated`, must be a value greater than or equal to `-1`")  # noqa: E501

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
        if not isinstance(other, PersonalNameCastegroupOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
