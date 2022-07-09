#!/usr/bin/env python3
import os
import threading
from datetime import time

import connexion
import pymongo as pymongo

from swagger_server import encoder
from swagger_server.custom_logger import custom_logger
from swagger_server.scheduler import background_scraper


logger = custom_logger.get_module_logger(__name__)

# Start the background thread
stop_run_continuously = background_scraper.run_continuously()

logger.info("server starting")
app = connexion.App(__name__, specification_dir="./swagger/")
app.app.json_encoder = encoder.JSONEncoder
app.add_api(
    "swagger.yaml", arguments={"title": "Metrics Scrapper"}, pythonic_params=True
)
