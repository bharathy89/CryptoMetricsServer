# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.pair import Pair  # noqa: F401,E501
from swagger_server import util
from swagger_server.models.util import get_db

db = get_db()
table = db["metrics_table"]


class Metric(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self, metric_id: str = None, metric_metadata: Pair = None
    ):  # noqa: E501
        """Metric - a model defined in Swagger

        :param metric_id: The metric_id of this Metric.  # noqa: E501
        :type metric_id: str
        :param metric_metadata: The metric_metadata of this Metric.  # noqa: E501
        :type metric_metadata: Pair
        """
        self.swagger_types = {"metric_id": str, "metric_metadata": Pair}

        self.attribute_map = {
            "metric_id": "metric_id",
            "metric_metadata": "metric_metadata",
        }
        self._metric_id = metric_id
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
    def metric_metadata(self) -> Pair:
        """Gets the metric_metadata of this Metric.


        :return: The metric_metadata of this Metric.
        :rtype: Pair
        """
        return self._metric_metadata

    @metric_metadata.setter
    def metric_metadata(self, metric_metadata: Pair):
        """Sets the metric_metadata of this Metric.


        :param metric_metadata: The metric_metadata of this Metric.
        :type metric_metadata: Pair
        """

        self._metric_metadata = metric_metadata

    def metric_name(self):
        return self._metric_metadata.from_asset + self._metric_metadata.to_asset

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
