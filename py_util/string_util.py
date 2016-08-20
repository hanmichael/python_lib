#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging

FORMAT = '[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('string_util')

def is_string(obj):
    """
    Check obj is str or unicode instance

    @obj: input value

    return True/False
    """
    try:
        return isinstance(obj, (str, unicode))
    except Exception,e:
        logger.error('check obj is string exception:[%s]' % (str(e)))
        return False
