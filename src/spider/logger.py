from os.path import join
from loguru import logger

from config import Config as cfg


def configure_logger():
    logger.add(join(cfg.LOGDIR, "app.log"), rotation="500 MB")