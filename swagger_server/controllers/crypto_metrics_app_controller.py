import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.metric import Metric  # noqa: E501
from swagger_server.models.monitor import Monitor  # noqa: E501
from swagger_server.models.query import Query  # noqa: E501
from swagger_server.models.source import Source  # noqa: E501
from swagger_server import util


def add_metric(body):  # noqa: E501
    """Add a metric

     # noqa: E501

    :param body: adding a metric
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Metric.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_metric(metric_id):  # noqa: E501
    """Deletes a metric

     # noqa: E501

    :param metric_id: metric id to delete
    :type metric_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_metric_monitor(metric_id, monitor_id):  # noqa: E501
    """deelte a monitor for the metric

     # noqa: E501

    :param metric_id: metric id to monitor
    :type metric_id: str
    :param monitor_id: metric id to monitor
    :type monitor_id: str

    :rtype: List[Monitor]
    """
    return 'do some magic!'


def list_metric_monitors(metric_id):  # noqa: E501
    """list all monitors for a metric

     # noqa: E501

    :param metric_id: metric id to monitor
    :type metric_id: str

    :rtype: List[Monitor]
    """
    return 'do some magic!'


def list_metric_sources(metric_id):  # noqa: E501
    """List all sources for the metric

     # noqa: E501

    :param metric_id: metric id to delete
    :type metric_id: str

    :rtype: List[Source]
    """
    return 'do some magic!'


def list_metrics():  # noqa: E501
    """List all the different metrics

     # noqa: E501


    :rtype: List[Metric]
    """
    return 'do some magic!'


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
        body = Query.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def rank_metrics(metric_type=None):  # noqa: E501
    """List all sources to scrape metrics

     # noqa: E501

    :param metric_type: 
    :type metric_type: str

    :rtype: List[Source]
    """
    return 'do some magic!'


def set_metric_monitor(metric_id, body=None):  # noqa: E501
    """set a monitor for a metric

     # noqa: E501

    :param metric_id: metric id to set monitor
    :type metric_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: Monitor
    """
    if connexion.request.is_json:
        body = Monitor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
