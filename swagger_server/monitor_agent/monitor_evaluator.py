from swagger_server.metrics_store.price_store import PriceStore
from swagger_server.models import Metric, Monitor, GREATER_THAN, LESS_THAN


def monitor_eval(price_store: PriceStore, monitor: Monitor):
    metric = Metric.load(monitor.metric_id)
    if metric:
        results = price_store.query_price(
            metric, start_time="-1m", end_time="", time_interval="1s"
        )
        for result in results:
            if monitor.operator == GREATER_THAN and result > monitor.value:
                monitor.call_webhook(
                    message="Price spike in the last minute", value=result
                )
            if monitor.operator == LESS_THAN and result < monitor.value:
                monitor.call_webhook(
                    message="Price drop in the last minute", value=result
                )
    else:
        raise Exception("metric doesnt exist : " + monitor.to_str())
