import logging
import logging.config

def setup_logger(log_config,loggername):
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(loggername)
    return logger