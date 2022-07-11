import json
import os
import threading
import time as t
from datetime import datetime

import schedule as schedule
from custom_logger import custom_logger
from swagger_server.models import Metric, Monitor
from swagger_server.models.source import Source  # noqa: E501
import requests
from swagger_server.metrics_store.price_store import PriceStore
from swagger_server.monitor_agent import monitor_evaluator
from swagger_server.scrapper import register

logger = custom_logger.get_module_logger(__name__)


def run_continuously(interval=1):
    """Continuously run, while executing pending jobs at each
    elapsed time interval.
    @return cease_continuous_run: threading. Event which can
    be set to cease continuous run. Please note that it is
    *intended behavior that run_continuously() does not run
    missed jobs*. For example, if you've registered a job that
    should run every minute and you set a continuous run
    interval of one hour then your job won't be run 60 times
    at each interval but only once.
    """
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                t.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


def background_scrape_job():
    logger.info("running the scrapper")
    source_list = Source.list()
    priceClient = PriceStore()
    for source in source_list:
        logger.info("running the scrapper for %s", source.source_id)
        metric = Metric.load(source.metric_id)
        try:
            if metric:
                timestamp = datetime.now()
                value = register[source.source_type].scrape(metric)
                priceClient.add_metric(timestamp, metric, value)
            else:
                logger.error("Metric doesnt exist : " + source.metric_id)
        except Exception as e:
            logger.error(e)


def background_monitor_job():
    logger.info("running the scrapper")
    monitors = Monitor.list()
    for monitor in monitors:
        logger.info("running the monitor for %s", monitor.to_str())
        try:
            monitor_evaluator.monitor_eval(monitor)
        except Exception as e:
            logger.error(e)


schedule.every(5).seconds.do(background_scrape_job)
schedule.every(5).seconds.do(background_monitor_job)


logger.info("adding to schedule")
