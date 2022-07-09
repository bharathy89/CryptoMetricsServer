import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from custom_logger import custom_logger
import os
from swagger_server.models import Metric

logger = custom_logger.get_module_logger(__name__)

CRYPTO_PRICES = "crypto_prices"


class PriceStore:
    def __init__(self):
        url = "http://{host}:{port}".format(
            host=os.environ["INFLUXDB_HOSTNAME"], port=8086
        )
        self.bucket = os.environ["INFLUXDB_BUCKET"]
        self.org = os.environ["INFLUXDB_ORG"]
        self.client = influxdb_client.InfluxDBClient(
            url=url, token=os.environ["INFLUXDB_TOKEN"], org=self.org
        )
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def add_metric(self, timestamp, metric: Metric, value):
        p = (
            influxdb_client.Point(CRYPTO_PRICES)
            .time(timestamp)
            .tag("metric_name", metric.metric_name)
            .field("price", float(value))
        )
        self.write_api.write(bucket=self.bucket, org=self.org, record=p)
