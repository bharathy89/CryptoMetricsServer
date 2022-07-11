from custom_logger import custom_logger
from swagger_server.metrics_store.price_store import PriceStore
from swagger_server.models import Metric, Monitor, Operation, ConstantValue

logger = custom_logger.get_module_logger(__name__)
price_store = PriceStore()

condition_operator_map = {
    ">": lambda x, y: x > y,
    ">=": lambda x, y: x >= y,
    "<": lambda x, y: x < y,
    "<=": lambda x, y: x <= y,
    "==": lambda x, y: x == y,
}


def divide(x, y):
    if y == 0:
        return 0
    return x / y


operator_map = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": divide,
}


def operation_eval(operation: Operation, sample_interval):
    if not operation.operand_type1:
        raise ValueError("operand1 cannot be empty")
    if not operation.operand_value1:
        raise ValueError("operand1 cannot be empty")

    result1 = operand_eval(operation.operand_type1,
                           operation.operand_value1,
                           operation.function,
                           operation.sample_interval,
                           sample_interval)
    result2 = 0
    if operation.operand_type2:
        result2 = operand_eval(operation.operand_type2,
                               operation.operand_value2,
                               operation.function,
                               operation.sample_interval,
                               sample_interval)

    if not operation.operator:
        return result1
    return perform_operator(result1, result2, operation.operator)


def perform_operator(result1, result2, operator):
    if isinstance(result1, list) and isinstance(result2, list):
        final_result = []
        if len(result1) == len(result2):
            for i, j in zip(result1, result2):
                final_result.append(operator_map[operator](i, j))
            return final_result
        else:
            logger.info("wrong sampling interval between operands "
                        "result1: {r1} result2: {r2}".format(r1=result1,
                                                             r2=result2))
            raise Exception(
                "wrong sampling interval between "
                "operands result1: {r1} result2: {r2}".format(r1=len(result1),
                                                              r2=len(result2)))
    elif isinstance(result1, list) and isinstance(result2, float):
        final_result = [operator_map[operator](i, result2) for i in result1]
        return final_result
    elif isinstance(result1, float) and isinstance(result2, list):
        final_result = [operator_map[operator](result1, i) for i in result2]
        return final_result
    elif isinstance(result1, float) and isinstance(result2, float):
        final_result = result1 + result2
        return final_result
    else:
        raise Exception("query couldnt be computed")


def perform_conditional_operator(result1, result2, operator):
    logger.info("{r1} {op} {r2}".format(r1=result1, op=operator, r2=result2))
    if isinstance(result1, list) \
            and isinstance(result2, list) and len(result1) == len(result2):
        for i, j in zip(result1, result2):
            if condition_operator_map[operator](i, j):
                return True
    elif isinstance(result1, list) and len(result1) > 1:
        if isinstance(result2, list) and len(result2) == 1:
            for i in result1:
                if condition_operator_map[operator](i, result2[0]):
                    return True
        elif isinstance(result2, float):
            for i in result1:
                if condition_operator_map[operator](i, result2):
                    return True
        else:
            logger.info("wrong sampling interval between operands "
                            "result1: {r1} result2: {r2}".format(r1=result1,
                                                                 r2=result2))
            raise Exception("wrong sampling interval between operands "
                            "result1: {r1} result2: {r2}".format(r1=result1,
                                                                 r2=result2))
    elif isinstance(result2, list) and len(result2) > 1:
        if isinstance(result1, float):
            for i in result2:
                if condition_operator_map[operator](result1, i):
                    return True
        elif isinstance(result1, list) and len(result1) == 1:
            for i in result2:
                if condition_operator_map[operator](result1[0], i):
                    return True
        else:
            logger.info("wrong sampling interval between operands "
                        "result1: {r1} result2: {r2}".format(r1=result1,
                                                             r2=result2))
            raise Exception("wrong sampling interval between operands "
                            "result1: {r1} result2: {r2}".format(r1=result1,
                                                                 r2=result2))
    elif isinstance(result1, float) and isinstance(result2, float):
        if condition_operator_map[operator](result1, result2):
            return True
    else:
        raise Exception("query couldnt be computed")
    return False


def operand_eval(operand_type,
                 operand_value,
                 function,
                 operation_sample_interval,
                 toplevel_sample_interval):
    if operand_type == "operation" and isinstance(operand_value, Operation):
        return operation_eval(operand_value, toplevel_sample_interval)
    elif operand_type == "metric":
        metric = Metric.load(operand_value["metric_id"])
        logger.info("processing metric " + metric.to_str())
        return price_store.query_eval(
            metric,
            start_time="-"+toplevel_sample_interval,
            time_interval=operation_sample_interval,
            func=function,
        )
    elif operand_type == "constant":
        return operand_value["value"]
    else:
        raise ValueError("operand is invalid format: " + operand_type + " : " + str(operand_value))


def monitor_eval(monitor: Monitor):
    if monitor.condition:
        triggered = False
        notified_time = None
        result1 = operation_eval(monitor.condition.operand_1,
                                 monitor.sample_interval)
        result2 = operation_eval(monitor.condition.operand_2,
                                 monitor.sample_interval)
        if monitor.condition.conditional_operator in condition_operator_map:
            if perform_conditional_operator(
                    result1, result2, monitor.condition.conditional_operator
            ):
                notified_time = monitor.call_webhook()
        else:
            raise ValueError("conditional operator is not valid")
        if triggered:
            if notified_time > 0:
                monitor.last_notified = notified_time
        monitor.active = triggered
        logger.info(monitor.to_str())
        monitor.save()
