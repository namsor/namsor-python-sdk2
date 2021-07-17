# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. By default, enpoints use 1 unit per name (ex. Gender), but Ethnicity classification uses 10 to 20 units per name depending on taxonomy. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.15
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class APIUsageAggregatedOut(object):
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
        'time_unit': 'str',
        'period_start': 'int',
        'period_end': 'int',
        'total_usage': 'int',
        'history_truncated': 'bool',
        'data': 'list[list[int]]',
        'col_headers': 'list[str]',
        'row_headers': 'list[str]'
    }

    attribute_map = {
        'time_unit': 'timeUnit',
        'period_start': 'periodStart',
        'period_end': 'periodEnd',
        'total_usage': 'totalUsage',
        'history_truncated': 'historyTruncated',
        'data': 'data',
        'col_headers': 'colHeaders',
        'row_headers': 'rowHeaders'
    }

    def __init__(self, time_unit=None, period_start=None, period_end=None, total_usage=None, history_truncated=None, data=None, col_headers=None, row_headers=None):  # noqa: E501
        """APIUsageAggregatedOut - a model defined in OpenAPI"""  # noqa: E501

        self._time_unit = None
        self._period_start = None
        self._period_end = None
        self._total_usage = None
        self._history_truncated = None
        self._data = None
        self._col_headers = None
        self._row_headers = None
        self.discriminator = None

        if time_unit is not None:
            self.time_unit = time_unit
        if period_start is not None:
            self.period_start = period_start
        if period_end is not None:
            self.period_end = period_end
        if total_usage is not None:
            self.total_usage = total_usage
        if history_truncated is not None:
            self.history_truncated = history_truncated
        if data is not None:
            self.data = data
        if col_headers is not None:
            self.col_headers = col_headers
        if row_headers is not None:
            self.row_headers = row_headers

    @property
    def time_unit(self):
        """Gets the time_unit of this APIUsageAggregatedOut.  # noqa: E501

        Time unit is DAY, WEEK or MONTH depending on prior usage  # noqa: E501

        :return: The time_unit of this APIUsageAggregatedOut.  # noqa: E501
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this APIUsageAggregatedOut.

        Time unit is DAY, WEEK or MONTH depending on prior usage  # noqa: E501

        :param time_unit: The time_unit of this APIUsageAggregatedOut.  # noqa: E501
        :type: str
        """

        self._time_unit = time_unit

    @property
    def period_start(self):
        """Gets the period_start of this APIUsageAggregatedOut.  # noqa: E501

        Start datetime of the reporting period  # noqa: E501

        :return: The period_start of this APIUsageAggregatedOut.  # noqa: E501
        :rtype: int
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start):
        """Sets the period_start of this APIUsageAggregatedOut.

        Start datetime of the reporting period  # noqa: E501

        :param period_start: The period_start of this APIUsageAggregatedOut.  # noqa: E501
        :type: int
        """

        self._period_start = period_start

    @property
    def period_end(self):
        """Gets the period_end of this APIUsageAggregatedOut.  # noqa: E501

        End datetime of the reporting period  # noqa: E501

        :return: The period_end of this APIUsageAggregatedOut.  # noqa: E501
        :rtype: int
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end):
        """Sets the period_end of this APIUsageAggregatedOut.

        End datetime of the reporting period  # noqa: E501

        :param period_end: The period_end of this APIUsageAggregatedOut.  # noqa: E501
        :type: int
        """

        self._period_end = period_end

    @property
    def total_usage(self):
        """Gets the total_usage of this APIUsageAggregatedOut.  # noqa: E501

        Total usage in the current period  # noqa: E501

        :return: The total_usage of this APIUsageAggregatedOut.  # noqa: E501
        :rtype: int
        """
        return self._total_usage

    @total_usage.setter
    def total_usage(self, total_usage):
        """Sets the total_usage of this APIUsageAggregatedOut.

        Total usage in the current period  # noqa: E501

        :param total_usage: The total_usage of this APIUsageAggregatedOut.  # noqa: E501
        :type: int
        """

        self._total_usage = total_usage

    @property
    def history_truncated(self):
        """Gets the history_truncated of this APIUsageAggregatedOut.  # noqa: E501

        If the history was truncaded due to data limit  # noqa: E501

        :return: The history_truncated of this APIUsageAggregatedOut.  # noqa: E501
        :rtype: bool
        """
        return self._history_truncated

    @history_truncated.setter
    def history_truncated(self, history_truncated):
        """Sets the history_truncated of this APIUsageAggregatedOut.

        If the history was truncaded due to data limit  # noqa: E501

        :param history_truncated: The history_truncated of this APIUsageAggregatedOut.  # noqa: E501
        :type: bool
        """

        self._history_truncated = history_truncated

    @property
    def data(self):
        """Gets the data of this APIUsageAggregatedOut.  # noqa: E501

        Data points : usage per DAY, WEEK or MONTH and per apiService  # noqa: E501

        :return: The data of this APIUsageAggregatedOut.  # noqa: E501
        :rtype: list[list[int]]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this APIUsageAggregatedOut.

        Data points : usage per DAY, WEEK or MONTH and per apiService  # noqa: E501

        :param data: The data of this APIUsageAggregatedOut.  # noqa: E501
        :type: list[list[int]]
        """

        self._data = data

    @property
    def col_headers(self):
        """Gets the col_headers of this APIUsageAggregatedOut.  # noqa: E501

        apiServices as column headers   # noqa: E501

        :return: The col_headers of this APIUsageAggregatedOut.  # noqa: E501
        :rtype: list[str]
        """
        return self._col_headers

    @col_headers.setter
    def col_headers(self, col_headers):
        """Sets the col_headers of this APIUsageAggregatedOut.

        apiServices as column headers   # noqa: E501

        :param col_headers: The col_headers of this APIUsageAggregatedOut.  # noqa: E501
        :type: list[str]
        """

        self._col_headers = col_headers

    @property
    def row_headers(self):
        """Gets the row_headers of this APIUsageAggregatedOut.  # noqa: E501

        dates as row headers   # noqa: E501

        :return: The row_headers of this APIUsageAggregatedOut.  # noqa: E501
        :rtype: list[str]
        """
        return self._row_headers

    @row_headers.setter
    def row_headers(self, row_headers):
        """Sets the row_headers of this APIUsageAggregatedOut.

        dates as row headers   # noqa: E501

        :param row_headers: The row_headers of this APIUsageAggregatedOut.  # noqa: E501
        :type: list[str]
        """

        self._row_headers = row_headers

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
        if not isinstance(other, APIUsageAggregatedOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
