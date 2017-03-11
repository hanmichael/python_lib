#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging
import warnings
import ConfigParser

FORMAT = '[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('config_parse')
logger.setLevel(logging.INFO)

def config_parse(config_file):
    """
    Parse config file

    @conf: config file path

    return dict
    """
    try:
        config_reader = ConfigParser.ConfigParser()
        config_reader.read(config_file)
        config_dict = {}
        for section in config_reader.sections():
            config_dict[section] = {}
            for option in config_reader.options(section):
                value = config_reader.get(section, option)
                config_dict[section][option] = value
        return config_dict
    except Exception,e:
        logger.error('parse config file:[%s] exception:[%s]' % (config_file, str(e)))
        return {}
