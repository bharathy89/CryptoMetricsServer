# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.metric import Metric  # noqa: E501
from swagger_server.models.monitor import Monitor  # noqa: E501
from swagger_server.models.query import Query  # noqa: E501
from swagger_server.models.source import Source  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCryptoMetricsAppController(BaseTestCase):
    """CryptoMetricsAppController integration test stubs"""

    def test_add_metric(self):
        """Test case for add_metric

        Add a metric
        """
        body = Metric()
        response = self.client.open(
            '//metrics',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_metric(self):
        """Test case for delete_metric

        Deletes a metric
        """
        response = self.client.open(
            '//metrics/{metric_id}'.format(metric_id='metric_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_metric_monitor(self):
        """Test case for delete_metric_monitor

        deelte a monitor for the metric
        """
        response = self.client.open(
            '//metrics/{metric_id}/monitors/{monitor_id}'.format(metric_id='metric_id_example', monitor_id='monitor_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_metric_monitors(self):
        """Test case for list_metric_monitors

        list all monitors for a metric
        """
        response = self.client.open(
            '//metrics/{metric_id}/monitors'.format(metric_id='metric_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_metric_sources(self):
        """Test case for list_metric_sources

        List all sources for the metric
        """
        response = self.client.open(
            '//metrics/{metric_id}/sources'.format(metric_id='metric_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_metrics(self):
        """Test case for list_metrics

        List all the different metrics
        """
        response = self.client.open(
            '//metrics',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_query_metrics(self):
        """Test case for query_metrics

        List all sources to scrape metrics
        """
        body = Query()
        response = self.client.open(
            '//metrics/{metric_id}/query'.format(metric_id='metric_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rank_metrics(self):
        """Test case for rank_metrics

        List all sources to scrape metrics
        """
        query_string = [('metric_type', 'metric_type_example')]
        response = self.client.open(
            '//metrics/rank',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_metric_monitor(self):
        """Test case for set_metric_monitor

        set a monitor for a metric
        """
        body = Monitor()
        response = self.client.open(
            '//metrics/{metric_id}/monitors'.format(metric_id='metric_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
