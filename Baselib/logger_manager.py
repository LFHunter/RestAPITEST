from logging import Logger
import logging
import logging.config
import json


def setup_logger(log_config: json, loggername: str) -> Logger:
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(loggername)
    return logger
