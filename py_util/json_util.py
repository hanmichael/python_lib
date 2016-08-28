#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import logging
import warnings
#warnings.filterwarnings('ignore')

FORMAT = '[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('json_util')

def json_2_str(json_obj):
    """
    Json obj 2 string obj

    @json_obj: json obj

    return str obj or None
    """
    try:
        str_obj = json.dumps(json_obj, ensure_ascii=False)
        if isinstance(str_obj, unicode):
            str_obj = str_obj.encode('utf-8')
        return str_obj
    except Exception,e:
        logger.error('json dumps exception:[%s]' % (str(e)))
        return None

def str_2_json(str_obj):
    """
    Str obj 2 json obj

    @str_obj: string obj

    return json obj or None
    """
    try:
        return json.loads(str_obj)
    except Exception,e:
        logger.error('json loads exception:[%s]' % (str(e)))
        return None


