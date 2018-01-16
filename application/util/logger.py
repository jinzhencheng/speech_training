# -*- coding: utf-8 -*-
# created by Jin(jinzhencheng@outlook.com) at 2018/01/15.

from config import GeneralConfig
import logging


def get_logger(name="speech_training", filename=GeneralConfig.DEFAULT_LOG_FILENAME):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger



