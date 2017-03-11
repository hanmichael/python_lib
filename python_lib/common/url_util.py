#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
import urllib
import urllib2
import md5
import base64
import logging
import tldextract
import warnings

FORMAT = '[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('url_util')
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

def url_valid(url):
    """
    Check Url is valid

    @url: raw url string

    return True/False
    """
    try:
        if URL_PATTERN.match(url):
            return True
        return False
    except Exception,e:
        logger.error('check url:[%s] is valid exception:[%s]' % (url, str(e)))
        return False

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

def get_host(url):
    """
    Url get host

    @url: url string

    return host or None
    """
    try:
        if url_valid(url) is False:
            logger.warning('url:[%s] is invalid' % url)
            return None
        extract_obj = tldextract.extract(url)
        host = extract_obj.subdomain + "." + extract_obj.domain + "." + extract_obj.suffix
        return host.strip('.')
    except Exception,e:
        logger.error('url:[%s] get host exception:[%s]' % (url, str(e)))
        return None

def get_domain(url):
    """
    Url get domain

    @url: url string

    return domain or None
    """
    try:
        if url_valid(url) is False:
            logger.warning('url:[%s] is invalid' % url)
            return None
        extract_obj = tldextract.extract(url)
        domain = extract_obj.domain + "." + extract_obj.suffix
        return domain.strip('.')
    except Exception,e:
        logger.error('url:[%s] get domain exception:[%s]' % (url, str(e)))
        return None
