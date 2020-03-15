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


class ClassifierMetricsOut(object):
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
        'software_version': 'str',
        'host_address': 'str',
        'learn_queue_size': 'int',
        'buffer_size': 'int',
        'pre_classify_queue_size': 'int',
        'fact_keys_size': 'int',
        'facts_learned': 'int',
        'classify_durations_current': 'float',
        'classify_durations_summary': 'float',
        'learn_durations_current': 'float',
        'learn_durations_summary': 'float',
        'classifier_name': 'str',
        'features_size': 'int',
        'ai_vetted_estimate_total': 'int',
        'ai_vetted_estimate_precision': 'float',
        'ai_vetted_estimate_recall': 'float',
        'ai_vetted_learn_total': 'int',
        'ai_non_vetted_estimate_total': 'int',
        'ai_non_vetted_estimate_precision': 'float',
        'ai_non_vetted_estimate_recall': 'float',
        'ai_non_vetted_learn_total': 'int',
        'metric_time_stamp': 'int',
        'ai_start_time': 'int',
        'ai_vetted_expected_class_metrics': 'list[ExpectedClassMetricsOut]',
        'ai_non_vetted_expected_class_metrics': 'list[ExpectedClassMetricsOut]'
    }

    attribute_map = {
        'software_version': 'softwareVersion',
        'host_address': 'hostAddress',
        'learn_queue_size': 'learnQueueSize',
        'buffer_size': 'bufferSize',
        'pre_classify_queue_size': 'preClassifyQueueSize',
        'fact_keys_size': 'factKeysSize',
        'facts_learned': 'factsLearned',
        'classify_durations_current': 'classifyDurationsCurrent',
        'classify_durations_summary': 'classifyDurationsSummary',
        'learn_durations_current': 'learnDurationsCurrent',
        'learn_durations_summary': 'learnDurationsSummary',
        'classifier_name': 'classifierName',
        'features_size': 'featuresSize',
        'ai_vetted_estimate_total': 'aiVettedEstimateTotal',
        'ai_vetted_estimate_precision': 'aiVettedEstimatePrecision',
        'ai_vetted_estimate_recall': 'aiVettedEstimateRecall',
        'ai_vetted_learn_total': 'aiVettedLearnTotal',
        'ai_non_vetted_estimate_total': 'aiNonVettedEstimateTotal',
        'ai_non_vetted_estimate_precision': 'aiNonVettedEstimatePrecision',
        'ai_non_vetted_estimate_recall': 'aiNonVettedEstimateRecall',
        'ai_non_vetted_learn_total': 'aiNonVettedLearnTotal',
        'metric_time_stamp': 'metricTimeStamp',
        'ai_start_time': 'aiStartTime',
        'ai_vetted_expected_class_metrics': 'aiVettedExpectedClassMetrics',
        'ai_non_vetted_expected_class_metrics': 'aiNonVettedExpectedClassMetrics'
    }

    def __init__(self, software_version=None, host_address=None, learn_queue_size=None, buffer_size=None, pre_classify_queue_size=None, fact_keys_size=None, facts_learned=None, classify_durations_current=None, classify_durations_summary=None, learn_durations_current=None, learn_durations_summary=None, classifier_name=None, features_size=None, ai_vetted_estimate_total=None, ai_vetted_estimate_precision=None, ai_vetted_estimate_recall=None, ai_vetted_learn_total=None, ai_non_vetted_estimate_total=None, ai_non_vetted_estimate_precision=None, ai_non_vetted_estimate_recall=None, ai_non_vetted_learn_total=None, metric_time_stamp=None, ai_start_time=None, ai_vetted_expected_class_metrics=None, ai_non_vetted_expected_class_metrics=None):  # noqa: E501
        """ClassifierMetricsOut - a model defined in OpenAPI"""  # noqa: E501

        self._software_version = None
        self._host_address = None
        self._learn_queue_size = None
        self._buffer_size = None
        self._pre_classify_queue_size = None
        self._fact_keys_size = None
        self._facts_learned = None
        self._classify_durations_current = None
        self._classify_durations_summary = None
        self._learn_durations_current = None
        self._learn_durations_summary = None
        self._classifier_name = None
        self._features_size = None
        self._ai_vetted_estimate_total = None
        self._ai_vetted_estimate_precision = None
        self._ai_vetted_estimate_recall = None
        self._ai_vetted_learn_total = None
        self._ai_non_vetted_estimate_total = None
        self._ai_non_vetted_estimate_precision = None
        self._ai_non_vetted_estimate_recall = None
        self._ai_non_vetted_learn_total = None
        self._metric_time_stamp = None
        self._ai_start_time = None
        self._ai_vetted_expected_class_metrics = None
        self._ai_non_vetted_expected_class_metrics = None
        self.discriminator = None

        if software_version is not None:
            self.software_version = software_version
        if host_address is not None:
            self.host_address = host_address
        if learn_queue_size is not None:
            self.learn_queue_size = learn_queue_size
        if buffer_size is not None:
            self.buffer_size = buffer_size
        if pre_classify_queue_size is not None:
            self.pre_classify_queue_size = pre_classify_queue_size
        if fact_keys_size is not None:
            self.fact_keys_size = fact_keys_size
        if facts_learned is not None:
            self.facts_learned = facts_learned
        if classify_durations_current is not None:
            self.classify_durations_current = classify_durations_current
        if classify_durations_summary is not None:
            self.classify_durations_summary = classify_durations_summary
        if learn_durations_current is not None:
            self.learn_durations_current = learn_durations_current
        if learn_durations_summary is not None:
            self.learn_durations_summary = learn_durations_summary
        if classifier_name is not None:
            self.classifier_name = classifier_name
        if features_size is not None:
            self.features_size = features_size
        if ai_vetted_estimate_total is not None:
            self.ai_vetted_estimate_total = ai_vetted_estimate_total
        if ai_vetted_estimate_precision is not None:
            self.ai_vetted_estimate_precision = ai_vetted_estimate_precision
        if ai_vetted_estimate_recall is not None:
            self.ai_vetted_estimate_recall = ai_vetted_estimate_recall
        if ai_vetted_learn_total is not None:
            self.ai_vetted_learn_total = ai_vetted_learn_total
        if ai_non_vetted_estimate_total is not None:
            self.ai_non_vetted_estimate_total = ai_non_vetted_estimate_total
        if ai_non_vetted_estimate_precision is not None:
            self.ai_non_vetted_estimate_precision = ai_non_vetted_estimate_precision
        if ai_non_vetted_estimate_recall is not None:
            self.ai_non_vetted_estimate_recall = ai_non_vetted_estimate_recall
        if ai_non_vetted_learn_total is not None:
            self.ai_non_vetted_learn_total = ai_non_vetted_learn_total
        if metric_time_stamp is not None:
            self.metric_time_stamp = metric_time_stamp
        if ai_start_time is not None:
            self.ai_start_time = ai_start_time
        if ai_vetted_expected_class_metrics is not None:
            self.ai_vetted_expected_class_metrics = ai_vetted_expected_class_metrics
        if ai_non_vetted_expected_class_metrics is not None:
            self.ai_non_vetted_expected_class_metrics = ai_non_vetted_expected_class_metrics

    @property
    def software_version(self):
        """Gets the software_version of this ClassifierMetricsOut.  # noqa: E501


        :return: The software_version of this ClassifierMetricsOut.  # noqa: E501
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this ClassifierMetricsOut.


        :param software_version: The software_version of this ClassifierMetricsOut.  # noqa: E501
        :type: str
        """

        self._software_version = software_version

    @property
    def host_address(self):
        """Gets the host_address of this ClassifierMetricsOut.  # noqa: E501


        :return: The host_address of this ClassifierMetricsOut.  # noqa: E501
        :rtype: str
        """
        return self._host_address

    @host_address.setter
    def host_address(self, host_address):
        """Sets the host_address of this ClassifierMetricsOut.


        :param host_address: The host_address of this ClassifierMetricsOut.  # noqa: E501
        :type: str
        """

        self._host_address = host_address

    @property
    def learn_queue_size(self):
        """Gets the learn_queue_size of this ClassifierMetricsOut.  # noqa: E501


        :return: The learn_queue_size of this ClassifierMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._learn_queue_size

    @learn_queue_size.setter
    def learn_queue_size(self, learn_queue_size):
        """Sets the learn_queue_size of this ClassifierMetricsOut.


        :param learn_queue_size: The learn_queue_size of this ClassifierMetricsOut.  # noqa: E501
        :type: int
        """

        self._learn_queue_size = learn_queue_size

    @property
    def buffer_size(self):
        """Gets the buffer_size of this ClassifierMetricsOut.  # noqa: E501


        :return: The buffer_size of this ClassifierMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._buffer_size

    @buffer_size.setter
    def buffer_size(self, buffer_size):
        """Sets the buffer_size of this ClassifierMetricsOut.


        :param buffer_size: The buffer_size of this ClassifierMetricsOut.  # noqa: E501
        :type: int
        """

        self._buffer_size = buffer_size

    @property
    def pre_classify_queue_size(self):
        """Gets the pre_classify_queue_size of this ClassifierMetricsOut.  # noqa: E501


        :return: The pre_classify_queue_size of this ClassifierMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._pre_classify_queue_size

    @pre_classify_queue_size.setter
    def pre_classify_queue_size(self, pre_classify_queue_size):
        """Sets the pre_classify_queue_size of this ClassifierMetricsOut.


        :param pre_classify_queue_size: The pre_classify_queue_size of this ClassifierMetricsOut.  # noqa: E501
        :type: int
        """

        self._pre_classify_queue_size = pre_classify_queue_size

    @property
    def fact_keys_size(self):
        """Gets the fact_keys_size of this ClassifierMetricsOut.  # noqa: E501


        :return: The fact_keys_size of this ClassifierMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._fact_keys_size

    @fact_keys_size.setter
    def fact_keys_size(self, fact_keys_size):
        """Sets the fact_keys_size of this ClassifierMetricsOut.


        :param fact_keys_size: The fact_keys_size of this ClassifierMetricsOut.  # noqa: E501
        :type: int
        """

        self._fact_keys_size = fact_keys_size

    @property
    def facts_learned(self):
        """Gets the facts_learned of this ClassifierMetricsOut.  # noqa: E501


        :return: The facts_learned of this ClassifierMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._facts_learned

    @facts_learned.setter
    def facts_learned(self, facts_learned):
        """Sets the facts_learned of this ClassifierMetricsOut.


        :param facts_learned: The facts_learned of this ClassifierMetricsOut.  # noqa: E501
        :type: int
        """

        self._facts_learned = facts_learned

    @property
    def classify_durations_current(self):
        """Gets the classify_durations_current of this ClassifierMetricsOut.  # noqa: E501


        :return: The classify_durations_current of this ClassifierMetricsOut.  # noqa: E501
        :rtype: float
        """
        return self._classify_durations_current

    @classify_durations_current.setter
    def classify_durations_current(self, classify_durations_current):
        """Sets the classify_durations_current of this ClassifierMetricsOut.


        :param classify_durations_current: The classify_durations_current of this ClassifierMetricsOut.  # noqa: E501
        :type: float
        """

        self._classify_durations_current = classify_durations_current

    @property
    def classify_durations_summary(self):
        """Gets the classify_durations_summary of this ClassifierMetricsOut.  # noqa: E501


        :return: The classify_durations_summary of this ClassifierMetricsOut.  # noqa: E501
        :rtype: float
        """
        return self._classify_durations_summary

    @classify_durations_summary.setter
    def classify_durations_summary(self, classify_durations_summary):
        """Sets the classify_durations_summary of this ClassifierMetricsOut.


        :param classify_durations_summary: The classify_durations_summary of this ClassifierMetricsOut.  # noqa: E501
        :type: float
        """

        self._classify_durations_summary = classify_durations_summary

    @property
    def learn_durations_current(self):
        """Gets the learn_durations_current of this ClassifierMetricsOut.  # noqa: E501


        :return: The learn_durations_current of this ClassifierMetricsOut.  # noqa: E501
        :rtype: float
        """
        return self._learn_durations_current

    @learn_durations_current.setter
    def learn_durations_current(self, learn_durations_current):
        """Sets the learn_durations_current of this ClassifierMetricsOut.


        :param learn_durations_current: The learn_durations_current of this ClassifierMetricsOut.  # noqa: E501
        :type: float
        """

        self._learn_durations_current = learn_durations_current

    @property
    def learn_durations_summary(self):
        """Gets the learn_durations_summary of this ClassifierMetricsOut.  # noqa: E501


        :return: The learn_durations_summary of this ClassifierMetricsOut.  # noqa: E501
        :rtype: float
        """
        return self._learn_durations_summary

    @learn_durations_summary.setter
    def learn_durations_summary(self, learn_durations_summary):
        """Sets the learn_durations_summary of this ClassifierMetricsOut.


        :param learn_durations_summary: The learn_durations_summary of this ClassifierMetricsOut.  # noqa: E501
        :type: float
        """

        self._learn_durations_summary = learn_durations_summary

    @property
    def classifier_name(self):
        """Gets the classifier_name of this ClassifierMetricsOut.  # noqa: E501


        :return: The classifier_name of this ClassifierMetricsOut.  # noqa: E501
        :rtype: str
        """
        return self._classifier_name

    @classifier_name.setter
    def classifier_name(self, classifier_name):
        """Sets the classifier_name of this ClassifierMetricsOut.


        :param classifier_name: The classifier_name of this ClassifierMetricsOut.  # noqa: E501
        :type: str
        """

        self._classifier_name = classifier_name

    @property
    def features_size(self):
        """Gets the features_size of this ClassifierMetricsOut.  # noqa: E501


        :return: The features_size of this ClassifierMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._features_size

    @features_size.setter
    def features_size(self, features_size):
        """Sets the features_size of this ClassifierMetricsOut.


        :param features_size: The features_size of this ClassifierMetricsOut.  # noqa: E501
        :type: int
        """

        self._features_size = features_size

    @property
    def ai_vetted_estimate_total(self):
        """Gets the ai_vetted_estimate_total of this ClassifierMetricsOut.  # noqa: E501


        :return: The ai_vetted_estimate_total of this ClassifierMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._ai_vetted_estimate_total

    @ai_vetted_estimate_total.setter
    def ai_vetted_estimate_total(self, ai_vetted_estimate_total):
        """Sets the ai_vetted_estimate_total of this ClassifierMetricsOut.


        :param ai_vetted_estimate_total: The ai_vetted_estimate_total of this ClassifierMetricsOut.  # noqa: E501
        :type: int
        """

        self._ai_vetted_estimate_total = ai_vetted_estimate_total

    @property
    def ai_vetted_estimate_precision(self):
        """Gets the ai_vetted_estimate_precision of this ClassifierMetricsOut.  # noqa: E501


        :return: The ai_vetted_estimate_precision of this ClassifierMetricsOut.  # noqa: E501
        :rtype: float
        """
        return self._ai_vetted_estimate_precision

    @ai_vetted_estimate_precision.setter
    def ai_vetted_estimate_precision(self, ai_vetted_estimate_precision):
        """Sets the ai_vetted_estimate_precision of this ClassifierMetricsOut.


        :param ai_vetted_estimate_precision: The ai_vetted_estimate_precision of this ClassifierMetricsOut.  # noqa: E501
        :type: float
        """

        self._ai_vetted_estimate_precision = ai_vetted_estimate_precision

    @property
    def ai_vetted_estimate_recall(self):
        """Gets the ai_vetted_estimate_recall of this ClassifierMetricsOut.  # noqa: E501


        :return: The ai_vetted_estimate_recall of this ClassifierMetricsOut.  # noqa: E501
        :rtype: float
        """
        return self._ai_vetted_estimate_recall

    @ai_vetted_estimate_recall.setter
    def ai_vetted_estimate_recall(self, ai_vetted_estimate_recall):
        """Sets the ai_vetted_estimate_recall of this ClassifierMetricsOut.


        :param ai_vetted_estimate_recall: The ai_vetted_estimate_recall of this ClassifierMetricsOut.  # noqa: E501
        :type: float
        """

        self._ai_vetted_estimate_recall = ai_vetted_estimate_recall

    @property
    def ai_vetted_learn_total(self):
        """Gets the ai_vetted_learn_total of this ClassifierMetricsOut.  # noqa: E501


        :return: The ai_vetted_learn_total of this ClassifierMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._ai_vetted_learn_total

    @ai_vetted_learn_total.setter
    def ai_vetted_learn_total(self, ai_vetted_learn_total):
        """Sets the ai_vetted_learn_total of this ClassifierMetricsOut.


        :param ai_vetted_learn_total: The ai_vetted_learn_total of this ClassifierMetricsOut.  # noqa: E501
        :type: int
        """

        self._ai_vetted_learn_total = ai_vetted_learn_total

    @property
    def ai_non_vetted_estimate_total(self):
        """Gets the ai_non_vetted_estimate_total of this ClassifierMetricsOut.  # noqa: E501


        :return: The ai_non_vetted_estimate_total of this ClassifierMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._ai_non_vetted_estimate_total

    @ai_non_vetted_estimate_total.setter
    def ai_non_vetted_estimate_total(self, ai_non_vetted_estimate_total):
        """Sets the ai_non_vetted_estimate_total of this ClassifierMetricsOut.


        :param ai_non_vetted_estimate_total: The ai_non_vetted_estimate_total of this ClassifierMetricsOut.  # noqa: E501
        :type: int
        """

        self._ai_non_vetted_estimate_total = ai_non_vetted_estimate_total

    @property
    def ai_non_vetted_estimate_precision(self):
        """Gets the ai_non_vetted_estimate_precision of this ClassifierMetricsOut.  # noqa: E501


        :return: The ai_non_vetted_estimate_precision of this ClassifierMetricsOut.  # noqa: E501
        :rtype: float
        """
        return self._ai_non_vetted_estimate_precision

    @ai_non_vetted_estimate_precision.setter
    def ai_non_vetted_estimate_precision(self, ai_non_vetted_estimate_precision):
        """Sets the ai_non_vetted_estimate_precision of this ClassifierMetricsOut.


        :param ai_non_vetted_estimate_precision: The ai_non_vetted_estimate_precision of this ClassifierMetricsOut.  # noqa: E501
        :type: float
        """

        self._ai_non_vetted_estimate_precision = ai_non_vetted_estimate_precision

    @property
    def ai_non_vetted_estimate_recall(self):
        """Gets the ai_non_vetted_estimate_recall of this ClassifierMetricsOut.  # noqa: E501


        :return: The ai_non_vetted_estimate_recall of this ClassifierMetricsOut.  # noqa: E501
        :rtype: float
        """
        return self._ai_non_vetted_estimate_recall

    @ai_non_vetted_estimate_recall.setter
    def ai_non_vetted_estimate_recall(self, ai_non_vetted_estimate_recall):
        """Sets the ai_non_vetted_estimate_recall of this ClassifierMetricsOut.


        :param ai_non_vetted_estimate_recall: The ai_non_vetted_estimate_recall of this ClassifierMetricsOut.  # noqa: E501
        :type: float
        """

        self._ai_non_vetted_estimate_recall = ai_non_vetted_estimate_recall

    @property
    def ai_non_vetted_learn_total(self):
        """Gets the ai_non_vetted_learn_total of this ClassifierMetricsOut.  # noqa: E501


        :return: The ai_non_vetted_learn_total of this ClassifierMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._ai_non_vetted_learn_total

    @ai_non_vetted_learn_total.setter
    def ai_non_vetted_learn_total(self, ai_non_vetted_learn_total):
        """Sets the ai_non_vetted_learn_total of this ClassifierMetricsOut.


        :param ai_non_vetted_learn_total: The ai_non_vetted_learn_total of this ClassifierMetricsOut.  # noqa: E501
        :type: int
        """

        self._ai_non_vetted_learn_total = ai_non_vetted_learn_total

    @property
    def metric_time_stamp(self):
        """Gets the metric_time_stamp of this ClassifierMetricsOut.  # noqa: E501


        :return: The metric_time_stamp of this ClassifierMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._metric_time_stamp

    @metric_time_stamp.setter
    def metric_time_stamp(self, metric_time_stamp):
        """Sets the metric_time_stamp of this ClassifierMetricsOut.


        :param metric_time_stamp: The metric_time_stamp of this ClassifierMetricsOut.  # noqa: E501
        :type: int
        """

        self._metric_time_stamp = metric_time_stamp

    @property
    def ai_start_time(self):
        """Gets the ai_start_time of this ClassifierMetricsOut.  # noqa: E501


        :return: The ai_start_time of this ClassifierMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._ai_start_time

    @ai_start_time.setter
    def ai_start_time(self, ai_start_time):
        """Sets the ai_start_time of this ClassifierMetricsOut.


        :param ai_start_time: The ai_start_time of this ClassifierMetricsOut.  # noqa: E501
        :type: int
        """

        self._ai_start_time = ai_start_time

    @property
    def ai_vetted_expected_class_metrics(self):
        """Gets the ai_vetted_expected_class_metrics of this ClassifierMetricsOut.  # noqa: E501


        :return: The ai_vetted_expected_class_metrics of this ClassifierMetricsOut.  # noqa: E501
        :rtype: list[ExpectedClassMetricsOut]
        """
        return self._ai_vetted_expected_class_metrics

    @ai_vetted_expected_class_metrics.setter
    def ai_vetted_expected_class_metrics(self, ai_vetted_expected_class_metrics):
        """Sets the ai_vetted_expected_class_metrics of this ClassifierMetricsOut.


        :param ai_vetted_expected_class_metrics: The ai_vetted_expected_class_metrics of this ClassifierMetricsOut.  # noqa: E501
        :type: list[ExpectedClassMetricsOut]
        """

        self._ai_vetted_expected_class_metrics = ai_vetted_expected_class_metrics

    @property
    def ai_non_vetted_expected_class_metrics(self):
        """Gets the ai_non_vetted_expected_class_metrics of this ClassifierMetricsOut.  # noqa: E501


        :return: The ai_non_vetted_expected_class_metrics of this ClassifierMetricsOut.  # noqa: E501
        :rtype: list[ExpectedClassMetricsOut]
        """
        return self._ai_non_vetted_expected_class_metrics

    @ai_non_vetted_expected_class_metrics.setter
    def ai_non_vetted_expected_class_metrics(self, ai_non_vetted_expected_class_metrics):
        """Sets the ai_non_vetted_expected_class_metrics of this ClassifierMetricsOut.


        :param ai_non_vetted_expected_class_metrics: The ai_non_vetted_expected_class_metrics of this ClassifierMetricsOut.  # noqa: E501
        :type: list[ExpectedClassMetricsOut]
        """

        self._ai_non_vetted_expected_class_metrics = ai_non_vetted_expected_class_metrics

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
        if not isinstance(other, ClassifierMetricsOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
