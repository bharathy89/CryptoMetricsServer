import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.source import Source  # noqa: E501
from swagger_server import util


def add_source(body):  # noqa: E501
    """Add a source to scrape metrics

     # noqa: E501

    :param body: adding a source to be scraped for metrics.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Source.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_source(source_id):  # noqa: E501
    """Deletes a source

     # noqa: E501

    :param source_id: source id to delete
    :type source_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_source(source_id):  # noqa: E501
    """Find source by id

    Returns a source # noqa: E501

    :param source_id: ID of source to return
    :type source_id: str

    :rtype: Source
    """
    return 'do some magic!'


def list_sources():  # noqa: E501
    """List all sources to scrape metrics

     # noqa: E501


    :rtype: List[Source]
    """
    return 'do some magic!'
