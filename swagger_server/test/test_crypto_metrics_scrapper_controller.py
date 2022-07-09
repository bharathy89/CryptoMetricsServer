# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.source import Source  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCryptoMetricsScrapperController(BaseTestCase):
    """CryptoMetricsScrapperController integration test stubs"""

    def test_add_source(self):
        """Test case for add_source

        Add a source to scrape metrics
        """
        body = Source()
        response = self.client.open(
            '//sources',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_source(self):
        """Test case for delete_source

        Deletes a source
        """
        response = self.client.open(
            '//sources/{source_id}'.format(source_id='source_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_source(self):
        """Test case for get_source

        Find source by id
        """
        response = self.client.open(
            '//sources/{source_id}'.format(source_id='source_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_sources(self):
        """Test case for list_sources

        List all sources to scrape metrics
        """
        response = self.client.open(
            '//sources',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
