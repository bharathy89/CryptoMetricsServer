# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model, get_db
from swagger_server.models.one_of_metric_metric_metadata import (
    OneOfMetricMetricMetadata,
)  # noqa: F401,E501
from swagger_server import util

db = get_db()
table = db["metrics_table"]


class Metric(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        metric_id: str = None,
        metric_type: str = None,
        metric_name: str = None,
        metric_metadata: OneOfMetricMetricMetadata = None,
    ):  # noqa: E501
        """Metric - a model defined in Swagger

        :param metric_id: The metric_id of this Metric.  # noqa: E501
        :type metric_id: str
        :param metric_type: The metric_type of this Metric.  # noqa: E501
        :type metric_type: str
        :param metric_name: The metric_name of this Metric.  # noqa: E501
        :type metric_name: str
        :param metric_metadata: The metric_metadata of this Metric.  # noqa: E501
        :type metric_metadata: OneOfMetricMetricMetadata
        """
        self.swagger_types = {
            "metric_id": str,
            "metric_type": str,
            "metric_name": str,
            "metric_metadata": OneOfMetricMetricMetadata,
        }

        self.attribute_map = {
            "metric_id": "metric_id",
            "metric_type": "metric_type",
            "metric_name": "metric_name",
            "metric_metadata": "metric_metadata",
        }
        self._metric_id = metric_id
        self._metric_type = metric_type
        self._metric_name = metric_name
        self._metric_metadata = metric_metadata

    @classmethod
    def from_dict(cls, dikt) -> "Metric":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Metric of this Metric.  # noqa: E501
        :rtype: Metric
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metric_id(self) -> str:
        """Gets the metric_id of this Metric.


        :return: The metric_id of this Metric.
        :rtype: str
        """
        return self._metric_id

    @metric_id.setter
    def metric_id(self, metric_id: str):
        """Sets the metric_id of this Metric.


        :param metric_id: The metric_id of this Metric.
        :type metric_id: str
        """

        self._metric_id = metric_id

    @property
    def metric_type(self) -> str:
        """Gets the metric_type of this Metric.


        :return: The metric_type of this Metric.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type: str):
        """Sets the metric_type of this Metric.


        :param metric_type: The metric_type of this Metric.
        :type metric_type: str
        """
        allowed_values = ["asset", "pair"]  # noqa: E501
        if metric_type not in allowed_values:
            raise ValueError(
                "Invalid value for `metric_type` ({0}), must be one of {1}".format(
                    metric_type, allowed_values
                )
            )

        self._metric_type = metric_type

    @property
    def metric_name(self) -> str:
        """Gets the metric_name of this Metric.


        :return: The metric_name of this Metric.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name: str):
        """Sets the metric_name of this Metric.


        :param metric_name: The metric_name of this Metric.
        :type metric_name: str
        """

        self._metric_name = metric_name

    @property
    def metric_metadata(self) -> OneOfMetricMetricMetadata:
        """Gets the metric_metadata of this Metric.


        :return: The metric_metadata of this Metric.
        :rtype: OneOfMetricMetricMetadata
        """
        return self._metric_metadata

    @metric_metadata.setter
    def metric_metadata(self, metric_metadata: OneOfMetricMetricMetadata):
        """Sets the metric_metadata of this Metric.


        :param metric_metadata: The metric_metadata of this Metric.
        :type metric_metadata: OneOfMetricMetricMetadata
        """

        self._metric_metadata = metric_metadata

    @classmethod
    def list(cls, offset=0, max_number=100) -> list:
        cursor = table.find().skip(offset).limit(max_number)

        items = []
        for item in cursor:
            items.append(Metric.from_dict(item))
        return items

    @classmethod
    def load(cls, metric_id: str) -> "Metric":
        cursor = table.find_one({"metric_id": metric_id})
        item = {}
        if cursor:
            item = Metric.from_dict(cursor)
        return item

    def save(self):
        res = table.update_one(
            {"metric_id": self.metric_id},
            {
                "$set": self.to_dict(),
            },
            upsert=True,
        )
        return res
