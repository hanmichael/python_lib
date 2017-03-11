#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import logging
import warnings
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FORMAT = '[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('crawl_util')
logger.setLevel(logging.INFO)

def crawl_page(url):
    """
    Crawl url page

    @url: url link

    return html/None
    """
    try:
        user_agent = (
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
        )
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = user_agent
        driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true'])
        driver.get(url)
        return driver.page_source
    except Exception,e:
        logger.error('url:[%s] crawl html page exception:[%s]' % (url, str(e)))
        return None

def crawl_final_url(url, wait_seconds = 20):
    """
    Crawl final url, URL_A->URL_B->URL_C, return URL_C

    @url: url link
    @wait_seconds: implicitly wait seconds, default equal 20

    return final url
    """
    try:
        user_agent = (
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
        )
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = user_agent
        driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true'])
        driver.get(url)
        driver.implicitly_wait(wait_seconds) #seconds
        return driver.current_url
    except Exception,e:
        logger.error('url:[%s] crawl final url exception:[%s]' % (url, str(e)))
        return None
