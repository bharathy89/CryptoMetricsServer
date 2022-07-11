import json

import requests
from swagger_server.scrapper.base_scrapper import BaseScrapper
from swagger_server.models.metric import Metric

# TODO: Ideally fetch from a creds db
KEY = "0GARP3I5PZ3ESV08N0I0"


class CryptoWatch(BaseScrapper):
    def __init__(self):
        self.url = "https://api.cryptowat.ch/markets/kraken/{metric}/price?apikey={key}"

    def scrape(self, metric: Metric):
        response = requests.get(self.url.format(metric=metric.metric_name(), key=KEY))
        if response.ok:
            json_response = json.loads(response.text)
            if "result" in json_response and "price" in json_response["result"]:
                price = json_response["result"]["price"]
                return 3 * price
        raise Exception("failed to fetch metric from CryptoWatch : " + response.text)
