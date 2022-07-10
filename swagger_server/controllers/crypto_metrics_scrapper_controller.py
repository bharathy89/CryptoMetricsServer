import uuid

import connexion
import six

from custom_logger import custom_logger
from swagger_server.models import Metric
from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.source import Source  # noqa: E501
from swagger_server import util

logger = custom_logger.get_module_logger(__name__)


def add_source(body):  # noqa: E501
    """Add a source to scrape metrics

     # noqa: E501

    :param body: adding a source to be scraped for metrics.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        source = Source.from_dict(connexion.request.get_json())  # noqa: E501
        metric = Metric.load(source.metric_id)
        if not metric:
            return ApiResponse(code=404, message="metric not found")
        new_source = Source()
        new_source.source_id = str(uuid.uuid4())
        new_source.metric_id = metric.metric_id
        new_source.source_type = source.source_type
        new_source.save()
        return new_source
    return ApiResponse(code=400, message="invalid request")


def delete_source(source_id):  # noqa: E501
    """Deletes a source

     # noqa: E501

    :param source_id: source id to delete
    :type source_id: str

    :rtype: None
    """
    return "do some magic!"


def get_source(source_id):  # noqa: E501
    """Find source by id

    Returns a source # noqa: E501

    :param source_id: ID of source to return
    :type source_id: str

    :rtype: Source
    """
    logger.info("fetching source %s", source_id)
    source = Source.load(source_id)
    if source:
        return source
    return ApiResponse(code=404, message="source not found")


def list_sources():  # noqa: E501
    """List all sources to scrape metrics

     # noqa: E501


    :rtype: List[Source]
    """
    logger.info("fetching sources")
    return Source.list()
