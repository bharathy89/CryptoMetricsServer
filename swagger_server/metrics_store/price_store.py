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
        self.query_api = self.client.query_api()

    def add_metric(self, timestamp, metric: Metric, value):
        p = (
            influxdb_client.Point(CRYPTO_PRICES)
            .time(timestamp)
            .tag("metric_name", metric.metric_name())
            .field("price", float(value))
        )
        self.write_api.write(bucket=self.bucket, org=self.org, record=p)

    def query_price(self, metric: Metric, start_time, end_time, time_interval):
        end_time_param = ""
        if end_time:
            end_time_param = ", stop: {end_time}".format(end_time=end_time)
        query = ' from(bucket:"{bucket}")\
        |> range(start: {start_time}{end_time_param})\
        |> filter(fn:(r) => r._measurement == "{measurement}")\
        |> filter(fn: (r) => r.metric_name == "{metric_name}")\
        |> filter(fn:(r) => r._field == "price" )\
        |> window(every: {time_interval})\
        |> mean()'.format(
            bucket=self.bucket,
            start_time=start_time,
            end_time_param=end_time_param,
            measurement=CRYPTO_PRICES,
            metric_name=metric.metric_name(),
            time_interval=time_interval,
        )
        result = self.query_api.query(org=self.org, query=query)
        results = []
        for table in result:
            for record in table.records:
                results.append(record.get_value())
        logger.info(results)
        return results

    def query_stddev(self, metric: Metric):
        query = ' from(bucket:"{bucket}")\
                |> range(start: -24h)\
                |> filter(fn:(r) => r._measurement == "{measurement}")\
                |> filter(fn: (r) => r.metric_name == "{metric_name}")\
                |> filter(fn:(r) => r._field == "price" )\
                |> stddev()'.format(
            bucket=self.bucket,
            measurement=CRYPTO_PRICES,
            metric_name=metric.metric_name(),
        )
        result = self.query_api.query(org=self.org, query=query)
        results = []
        for table in result:
            for record in table.records:
                results.append(record.get_value())
        if len(results) > 0:
            return results[0]
        return 0
