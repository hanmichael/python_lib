#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import urllib
import urllib2
import md5
import base64
import logging

FORMAT = '[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('url_util')

def url_quote(url):
    """
    Url quote

    @url: raw url string

    return quote url
    """
    try:
        return urllib2.quote(url)
    except Exception,e:
        logger.error('url:[%s] quote exception:[%s]' % (url, str(e)))
        return None

def url_unquote(quote_url):
    """
    Url unquote

    @url: quote url string

    return raw url
    """
    try:
        return urllib2.unquote(quote_url)
    except Exception,e:
        logger.error('quote url:[%s] unquote exception:[%s]' % (quote_url, str(e)))
        return None

def url_md5(url):
    """
    Url calculate md5 value

    @url: raw url string

    return 32 bytes md5
    """
    try:
        return md5.md5(url).hexdigest()
    except Exception,e:
        logger.error('url:[%s] calc md5 exception:[%s]' % (url, str(e)))
        return None

def url_signature(url):
    """
    Url calculate signature

    @url: raw url string

    return "xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxxxxx"
    """
    try:
        signature = url_md5(url)
        return signature[0:8]+'-'+signature[8:16]+'-'+signature[16:24]+'-'+signature[24:32]
    except Exception,e:
        logger.error('url:[%s] calc signature exception:[%s]' % (url, str(e)))
        return None

def url_encode(url):
    """
    Url encode use base64 urlsafe encode

    @url: raw url string

    return encode url only contain "letter, digit, _-="
    """
    try:
        return base64.urlsafe_b64encode(url)
    except Exception,e:
        logger.error('url:[%s] encode exception:[%s]' % (url, str(e)))
        return None

def url_decode(encode_url):
    """
    Url decode use base64 urlsafe decode

    @url: encode url string

    return raw url
    """
    try:
        return base64.urlsafe_b64decode(encode_url)
    except Exception,e:
        logger.error('url:[%s] decode exception:[%s]' % (encode_url, str(e)))
        return None
