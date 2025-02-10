import logging
import json
import logging.config
from logging import Logger


def setup_logger(log_config: json, loggername: str) -> Logger:
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(loggername)
    return logger
