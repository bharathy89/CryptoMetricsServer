import uuid
import time

import connexion
import six

from custom_logger import custom_logger
from swagger_server.metrics_store.price_store import PriceStore
from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.metric import Metric  # noqa: E501
from swagger_server.models.monitor import Monitor  # noqa: E501
from swagger_server.models.query import Query  # noqa: E501
from swagger_server.models.source import Source  # noqa: E501
from swagger_server import util

logger = custom_logger.get_module_logger(__name__)


def add_metric(body):  # noqa: E501
    """Add a metric

     # noqa: E501

    :param body: adding a metric
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        metric = Metric.from_dict(connexion.request.get_json())  # noqa: E501
        metric.metric_id = str(uuid.uuid4())
        metric.save()
        return metric
    return ApiResponse(code=400, message="invalid request")


def delete_metric(metric_id):  # noqa: E501
    """Deletes a metric

     # noqa: E501

    :param metric_id: metric id to delete
    :type metric_id: str

    :rtype: None
    """
    return "do some magic!"


def delete_metric_monitor(monitor_id):  # noqa: E501
    """deelte a monitor for the metric

     # noqa: E501
    :param monitor_id: metric id to monitor
    :type monitor_id: str

    :rtype: Monitor
    """
    return "do some magic!"


def list_metric_monitors(metric_id=None):  # noqa: E501
    """list all monitors for a metric

     # noqa: E501

    :param metric_id: metric id to monitor
    :type metric_id: str

    :rtype: List[Monitor]
    """
    logger.info(f"fetching monitor for {metric_id}")
    return Monitor.list(metric_id=metric_id)


def list_metric_sources(metric_id):  # noqa: E501
    """List all sources for the metric

     # noqa: E501

    :param metric_id: metric id to delete
    :type metric_id: str

    :rtype: List[Source]
    """
    logger.info(f"fetching sources for {metric_id}")
    return Source.list(metric_id=metric_id)


def list_metrics():  # noqa: E501
    """List all the different metrics

     # noqa: E501


    :rtype: List[Metric]
    """
    logger.info(f"fetching metrics")
    return Metric.list()


def query_metrics(metric_id, body=None):  # noqa: E501
    """List all sources to scrape metrics

     # noqa: E501

    :param metric_id: metric id to delete
    :type metric_id: str
    :param body:
    :type body: dict | bytes

    :rtype: List[Source]
    """
    if connexion.request.is_json:
        query = Query.from_dict(connexion.request.get_json())  # noqa: E501
        metric = Metric.load(metric_id)
        if not metric:
            return ApiResponse(code=404, message="metric not found")
        if query.start_time < query.end_time:
            start_time = time.strftime(
                "%Y-%m-%dT%H:%M:%SZ", time.gmtime(query.start_time)
            )
            end_time = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(query.end_time))
            result = PriceStore().query_price(
                metric, start_time, end_time, query.resolution
            )
            return result
    return ApiResponse(code=400, message="invalid request")


def rank_metrics():  # noqa: E501
    """List all sources to scrape metrics

     # noqa: E501


    :rtype: List[Source]
    """
    metrics = Metric.list()
    price_store = PriceStore()
    final_result = []
    for metric in metrics:
        result = price_store.query_stddev(metric)
        final_result.append((metric.metric_name(), result))

    final_result = sorted(final_result, key=lambda x: x[1], reverse=True)
    return final_result


def set_metric_monitor(body=None):  # noqa: E501
    """set a monitor for a metric

     # noqa: E501

    :param metric_id: metric id to set monitor
    :param body:
    :type body: dict | bytes

    :rtype: Monitor
    """
    if connexion.request.is_json:
        monitor = Monitor.from_dict(connexion.request.get_json())  # noqa: E501
        metric = Metric.load(monitor.metric_id)
        if not metric:
            return ApiResponse(code=404, message="metric not found")
        monitor.monitor_id = str(uuid.uuid4())
        monitor.save()
        return monitor
    return ApiResponse(code=400, message="invalid request")
