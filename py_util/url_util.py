#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import urllib
import urllib2
import md5
import base64

def url_quote(raw_url):
    return urllib2.quote(raw_url)

def url_unquote(quote_url):
    return urllib2.unquote(quote_url)

def url_md5(url):
    return md5.md5(url).hexdigest()

def url_encode(raw_url):
    return base64.urlsafe_b64encode(raw_url)

def url_decode(encode_url):
    return base64.urlsafe_b64decode(encode_url)
