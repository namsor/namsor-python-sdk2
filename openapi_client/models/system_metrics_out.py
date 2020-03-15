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


class SystemMetricsOut(object):
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
        'cache_metrics': 'list[CacheMetricsOut]',
        'classifier_metrics': 'list[ClassifierMetricsOut]',
        'source_metrics': 'list[SourceMetricsOut]',
        'total_mem': 'int',
        'free_mem': 'int',
        'max_mem': 'int'
    }

    attribute_map = {
        'cache_metrics': 'cacheMetrics',
        'classifier_metrics': 'classifierMetrics',
        'source_metrics': 'sourceMetrics',
        'total_mem': 'totalMem',
        'free_mem': 'freeMem',
        'max_mem': 'maxMem'
    }

    def __init__(self, cache_metrics=None, classifier_metrics=None, source_metrics=None, total_mem=None, free_mem=None, max_mem=None):  # noqa: E501
        """SystemMetricsOut - a model defined in OpenAPI"""  # noqa: E501

        self._cache_metrics = None
        self._classifier_metrics = None
        self._source_metrics = None
        self._total_mem = None
        self._free_mem = None
        self._max_mem = None
        self.discriminator = None

        if cache_metrics is not None:
            self.cache_metrics = cache_metrics
        if classifier_metrics is not None:
            self.classifier_metrics = classifier_metrics
        if source_metrics is not None:
            self.source_metrics = source_metrics
        if total_mem is not None:
            self.total_mem = total_mem
        if free_mem is not None:
            self.free_mem = free_mem
        if max_mem is not None:
            self.max_mem = max_mem

    @property
    def cache_metrics(self):
        """Gets the cache_metrics of this SystemMetricsOut.  # noqa: E501


        :return: The cache_metrics of this SystemMetricsOut.  # noqa: E501
        :rtype: list[CacheMetricsOut]
        """
        return self._cache_metrics

    @cache_metrics.setter
    def cache_metrics(self, cache_metrics):
        """Sets the cache_metrics of this SystemMetricsOut.


        :param cache_metrics: The cache_metrics of this SystemMetricsOut.  # noqa: E501
        :type: list[CacheMetricsOut]
        """

        self._cache_metrics = cache_metrics

    @property
    def classifier_metrics(self):
        """Gets the classifier_metrics of this SystemMetricsOut.  # noqa: E501


        :return: The classifier_metrics of this SystemMetricsOut.  # noqa: E501
        :rtype: list[ClassifierMetricsOut]
        """
        return self._classifier_metrics

    @classifier_metrics.setter
    def classifier_metrics(self, classifier_metrics):
        """Sets the classifier_metrics of this SystemMetricsOut.


        :param classifier_metrics: The classifier_metrics of this SystemMetricsOut.  # noqa: E501
        :type: list[ClassifierMetricsOut]
        """

        self._classifier_metrics = classifier_metrics

    @property
    def source_metrics(self):
        """Gets the source_metrics of this SystemMetricsOut.  # noqa: E501


        :return: The source_metrics of this SystemMetricsOut.  # noqa: E501
        :rtype: list[SourceMetricsOut]
        """
        return self._source_metrics

    @source_metrics.setter
    def source_metrics(self, source_metrics):
        """Sets the source_metrics of this SystemMetricsOut.


        :param source_metrics: The source_metrics of this SystemMetricsOut.  # noqa: E501
        :type: list[SourceMetricsOut]
        """

        self._source_metrics = source_metrics

    @property
    def total_mem(self):
        """Gets the total_mem of this SystemMetricsOut.  # noqa: E501


        :return: The total_mem of this SystemMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._total_mem

    @total_mem.setter
    def total_mem(self, total_mem):
        """Sets the total_mem of this SystemMetricsOut.


        :param total_mem: The total_mem of this SystemMetricsOut.  # noqa: E501
        :type: int
        """

        self._total_mem = total_mem

    @property
    def free_mem(self):
        """Gets the free_mem of this SystemMetricsOut.  # noqa: E501


        :return: The free_mem of this SystemMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._free_mem

    @free_mem.setter
    def free_mem(self, free_mem):
        """Sets the free_mem of this SystemMetricsOut.


        :param free_mem: The free_mem of this SystemMetricsOut.  # noqa: E501
        :type: int
        """

        self._free_mem = free_mem

    @property
    def max_mem(self):
        """Gets the max_mem of this SystemMetricsOut.  # noqa: E501


        :return: The max_mem of this SystemMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._max_mem

    @max_mem.setter
    def max_mem(self, max_mem):
        """Sets the max_mem of this SystemMetricsOut.


        :param max_mem: The max_mem of this SystemMetricsOut.  # noqa: E501
        :type: int
        """

        self._max_mem = max_mem

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
        if not isinstance(other, SystemMetricsOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
