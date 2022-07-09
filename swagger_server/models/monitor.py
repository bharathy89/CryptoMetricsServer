# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model, get_db
from swagger_server import util


db = get_db()
table = db["monitors_table"]


class Monitor(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, monitor_id: str=None, metric_id: str=None, operand: str=None, value: float=None, notify_webhook: str=None):  # noqa: E501
        """Monitor - a model defined in Swagger

        :param monitor_id: The monitor_id of this Monitor.  # noqa: E501
        :type monitor_id: str
        :param metric_id: The metric_id of this Monitor.  # noqa: E501
        :type metric_id: str
        :param operand: The operand of this Monitor.  # noqa: E501
        :type operand: str
        :param value: The value of this Monitor.  # noqa: E501
        :type value: float
        :param notify_webhook: The notify_webhook of this Monitor.  # noqa: E501
        :type notify_webhook: str
        """
        self.swagger_types = {
            'monitor_id': str,
            'metric_id': str,
            'operand': str,
            'value': float,
            'notify_webhook': str
        }

        self.attribute_map = {
            'monitor_id': 'monitor_id',
            'metric_id': 'metric_id',
            'operand': 'operand',
            'value': 'value',
            'notify_webhook': 'notify_webhook'
        }
        self._monitor_id = monitor_id
        self._metric_id = metric_id
        self._operand = operand
        self._value = value
        self._notify_webhook = notify_webhook

    @classmethod
    def from_dict(cls, dikt) -> 'Monitor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Monitor of this Monitor.  # noqa: E501
        :rtype: Monitor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def monitor_id(self) -> str:
        """Gets the monitor_id of this Monitor.


        :return: The monitor_id of this Monitor.
        :rtype: str
        """
        return self._monitor_id

    @monitor_id.setter
    def monitor_id(self, monitor_id: str):
        """Sets the monitor_id of this Monitor.


        :param monitor_id: The monitor_id of this Monitor.
        :type monitor_id: str
        """

        self._monitor_id = monitor_id

    @property
    def metric_id(self) -> str:
        """Gets the metric_id of this Monitor.


        :return: The metric_id of this Monitor.
        :rtype: str
        """
        return self._metric_id

    @metric_id.setter
    def metric_id(self, metric_id: str):
        """Sets the metric_id of this Monitor.


        :param metric_id: The metric_id of this Monitor.
        :type metric_id: str
        """

        self._metric_id = metric_id

    @property
    def operand(self) -> str:
        """Gets the operand of this Monitor.


        :return: The operand of this Monitor.
        :rtype: str
        """
        return self._operand

    @operand.setter
    def operand(self, operand: str):
        """Sets the operand of this Monitor.


        :param operand: The operand of this Monitor.
        :type operand: str
        """

        self._operand = operand

    @property
    def value(self) -> float:
        """Gets the value of this Monitor.


        :return: The value of this Monitor.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value: float):
        """Sets the value of this Monitor.


        :param value: The value of this Monitor.
        :type value: float
        """

        self._value = value

    @property
    def notify_webhook(self) -> str:
        """Gets the notify_webhook of this Monitor.


        :return: The notify_webhook of this Monitor.
        :rtype: str
        """
        return self._notify_webhook

    @notify_webhook.setter
    def notify_webhook(self, notify_webhook: str):
        """Sets the notify_webhook of this Monitor.


        :param notify_webhook: The notify_webhook of this Monitor.
        :type notify_webhook: str
        """

        self._notify_webhook = notify_webhook

    @classmethod
    def list(cls, metric_id="", offset=0, max_number=100) -> list:
        cursor = None
        if metric_id:
            cursor = table.find({"metric_id": metric_id}).skip(offset).limit(
                max_number)
        else:
            cursor = table.find().skip(offset).limit(max_number)

        items = []
        for item in cursor:
            items.append(Monitor.from_dict(item))
        return items

    @classmethod
    def load(cls, monitor_id: str) -> "Monitor":
        cursor = table.find_one({"monitor_id": monitor_id})
        item = {}
        if cursor:
            item = Monitor.from_dict(cursor)
        return item

    def save(self):
        res = table.update_one({"monitor_id": self.monitor_id},
                               {
                                   "$set": self.to_dict(),
                               }, upsert=True)
        return res
