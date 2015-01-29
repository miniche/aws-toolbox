# -*- coding: utf-8 -*-

import logging


def init():
    """
    Initializes the root logger. By default, the level threesold is defined to INFO.
    """
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.getLogger().setLevel(logging.INFO)
