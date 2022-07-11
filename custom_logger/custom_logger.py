import logging
import os
from os.path import exists

file_path = "./log"
file_full_path = "{file_path}/{name}".format(
    file_path=file_path, name="application.log"
)


def get_module_logger(mod_name):
    """
    To use this, do logger = get_module_logger(__name__)
    """
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
        "%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    if not exists(file_path):
        os.mkdir(file_path)
    filehandler = logging.FileHandler(file_full_path)
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    return logger


if __name__ == "__main__":
    get_module_logger(__name__).info("HELLO WORLD!")
