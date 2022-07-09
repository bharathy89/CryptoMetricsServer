from __future__ import absolute_import

from swagger_server.scrapper.cryptowatch_scrapper import CryptoWatch

register = {
    "cryptowatch": CryptoWatch(),
}