# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Pair(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, from_asset: str = None, to_asset: str = None):  # noqa: E501
        """Pair - a model defined in Swagger

        :param from_asset: The from_asset of this Pair.  # noqa: E501
        :type from_asset: str
        :param to_asset: The to_asset of this Pair.  # noqa: E501
        :type to_asset: str
        """
        self.swagger_types = {"from_asset": str, "to_asset": str}

        self.attribute_map = {"from_asset": "from_asset", "to_asset": "to_asset"}
        self._from_asset = from_asset
        self._to_asset = to_asset

    @classmethod
    def from_dict(cls, dikt) -> "Pair":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pair of this Pair.  # noqa: E501
        :rtype: Pair
        """
        return util.deserialize_model(dikt, cls)

    @property
    def from_asset(self) -> str:
        """Gets the from_asset of this Pair.


        :return: The from_asset of this Pair.
        :rtype: str
        """
        return self._from_asset

    @from_asset.setter
    def from_asset(self, from_asset: str):
        """Sets the from_asset of this Pair.


        :param from_asset: The from_asset of this Pair.
        :type from_asset: str
        """

        self._from_asset = from_asset

    @property
    def to_asset(self) -> str:
        """Gets the to_asset of this Pair.


        :return: The to_asset of this Pair.
        :rtype: str
        """
        return self._to_asset

    @to_asset.setter
    def to_asset(self, to_asset: str):
        """Sets the to_asset of this Pair.


        :param to_asset: The to_asset of this Pair.
        :type to_asset: str
        """

        self._to_asset = to_asset
