#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import logging
import requests
import warnings
#warnings.filterwarnings('ignore')

FORMAT = '[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('request_util')

def get(url, params=None, timeout=10, headers=None, cookies=None, proxies=None):
    """
    Get request

    @url: request url, http://www.xxx.com/query
    @params: url params dict, such as "{"query":"iPhone", "time":"1426827389"}"
    @timeout: request timeout second
    @headers: request headers
    @cookies: request cookies
    @proxies: request proxies

    return response obj
    """
    try:
        response = requests.get(url, timeout=timeout, params=params, headers=headers, cookies=cookies)
        return response
    except Exception,e:
        logger.error('url:[%s] request get exception:[%s]\n' % (url, str(e)))
        return None

def post(url, data, timeout=10, headers=None, cookies=None, proxies=None):
    """
    Post request

    @url: request url, http://www.xxx.com/query
    @data: post data, dict obj
    @timeout: request timeout second
    @headers: request headers
    @cookies: request cookies
    @proxies: request proxies

    return response obj
    """
    try:
        response = requests.post(url, data=json.dumps(data), timeout=timeout, headers=headers, cookies=cookies, proxies=proxies)
        return response
    except Exception,e:
        logger.error('url:[%s] request post exception:[%s]\n' % (url, str(e)))
        return None
