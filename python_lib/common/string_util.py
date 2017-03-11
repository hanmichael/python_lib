#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import logging
import warnings
import json_util
from hashlib import md5

FORMAT = '[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('string_util')
logger.setLevel(logging.INFO)

# global var
URL_PATTERN = re.compile(
    r'^'
    r'((http|ftp)s?://)?'  # scheme
    r'([a-z_\d-]+:[a-z_\d-]+@)?'  # user:password
    r'(www\.)?'  # www.
    r'((?<!\.)[a-z\d\.-]+\.[a-z]{2,6}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|localhost)'  # domain
    r'(:\d{2,})?'  # port number
    r'(/[a-z\d_%\+-]*)*'  # folders
    r'(\.[a-z\d_%\+-]+)*'  # file extension
    r'(\?[a-z\d_\+%-=]*)?'  # query string
    r'(#\S*)?'  # hash
    r'$',
    re.IGNORECASE
)
EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z\d\._\+-]+@([a-z\d-]+\.?[a-z\d-]+)+\.[a-z]{2,4}$',
    re.IGNORECASE
)
IP_PATTERN = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

def is_string(input):
    """
    Check input is str or unicode instance

    @input: input value

    return True/False
    """
    try:
        return isinstance(input, (str, unicode))
    except Exception,e:
        logger.error('check is string exception:[%s]' % (str(e)))
        return False

def is_url(input, allowed_schemas = None):
    """
    Check input is a valid url

    @input: input obj
    @allowed_schemas: allowed schemas list [http, ftp, https ...], default allowed any schema

    return True/False
    """
    try:
        if URL_PATTERN.match(input):
            ret = True
        else:
            ret = False
        if ret and allowed_schemas:
            return ret and any([input.startswith(s) for s in allowed_schemas])
        return ret
    except Exception,e:
        logger.error('check is url exception:[%s]' % (str(e)))
        return False

def is_email(input):
    """
    Check input is a valid email

    @input: input email string

    return True/False
    """
    try:
        if EMAIL_PATTERN.match(input):
            return True
        return False
    except Exception,e:
        logger.error('check is email exception:[%s]' % (str(e)))
        return False

def is_json(input):
    """
    Check input string is a valid json obj

    @input: input string

    return True/False
    """
    try:
        return json_util.str_2_json(input)
    except Exception,e:
        logger.error('check is json exception:[%s]' % (str(e)))
        return False

def is_ip(input):
    """
    Check input string is a valid ip

    @input: input string

    return True/False
    """
    try:
        if IP_PATTERN.match(input):
            return True
        return False
    except Exception,e:
        logger.error('check is json exception:[%s]' % (str(e)))
        return False

def hash_128(input_str):
    """
    Hash string to 128 bit int

    @input_str: input string

    return 128 bit int
    """
    try:
        return int(md5(input_str).hexdigest(), 16)
    except Exception,e:
        logger.error('hash 128 exception:[%s]' % (str(e)))
        return None

def hash_64(input_str):
    """
    Hash string to 64 bit int

    @input_str: input string

    return 64 bit int
    """
    try:
        return int(md5(input_str).hexdigest()[8:24], 16)
    except Exception,e:
        logger.error('hash 64 exception:[%s]' % (str(e)))
        return None

def hash_32(input_str):
    """
    Hash string to 32 bit int

    @input_str: input string

    return 32 bit int
    """
    try:
        return int(md5(input_str).hexdigest()[12:20], 16)
    except Exception,e:
        logger.error('hash 32 exception:[%s]' % (str(e)))
        return None
