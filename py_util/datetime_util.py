#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import datetime

def get_year():
    """
    Get current year
    return 2015 or 2016 or 2017 ...
    """
    try:
        return time.strftime('%Y')
    except Exception,e:
        sys.stderr.write('get [year] exception:[%s]' % (str(e)))
        return None

def get_month():
    """
    Get current month
    return 01 or 02 or 03 ... 12
    """
    try:
        return time.strftime('%m')
    except Exception,e:
        sys.stderr.write('get [month] exception:[%s]' % (str(e)))
        return None

def get_date():
    """
    Get current date
    return 01 or 02 or 03 ... 31
    """
    try:
        return time.strftime('%d')
    except Exception,e:
        sys.stderr.write('get [date] exception:[%s]' % (str(e)))
        return None

def get_hour():
    """
    Get current hour
    return 00 or 01 or 02 ... 23
    """
    try:
        return time.strftime('%H')
    except Exception,e:
        sys.stderr.write('get [hour] exception:[%s]' % (str(e)))
        return None

def get_minute():
    """
    Get current minute
    return 00 or 01 or 02 ... 59
    """
    try:
        return time.strftime('%M')
    except Exception,e:
        sys.stderr.write('get [minute] exception:[%s]' % (str(e)))
        return None

def get_second():
    """
    Get current second
    return 00 or 01 or 02 ... 59
    """
    try:
        return time.strftime('%S')
    except Exception,e:
        sys.stderr.write('get [minute] exception:[%s]' % (str(e)))
        return None

def get_today_date(format = "%Y-%m-%d"):
    """
    Get today date

    @format: date format, may be "2016-07-11" or "2016_07_11" ...
    """
    try:
        return datetime.date.today().strftime(format)
    except Exception,e:
        sys.stderr.write('get today [date] exception:[%s]' % (str(e)))
        return None

def get_yesterday_date(format = "%Y-%m-%d"):
    """
    Get yesterday date

    @format: date format, may be "2016-07-11" or "2016_07_11" ...
    """
    try:
        return get_before_date(1)
    except Exception,e:
        sys.stderr.write('get yesterday [date] exception:[%s]' % (str(e)))
        return None

def get_tomorrow_date(format = "%Y-%m-%d"):
    """
    Get tomorrow date

    @format: date format, may be "2016-07-11" or "2016_07_11" ...
    """
    try:
        return get_after_date(1)
    except Exception,e:
        sys.stderr.write('get yesterday [date] exception:[%s]' % (str(e)))
        return None

def get_before_date(before_days = 0, format = "%Y-%m-%d"):
    """
    Get today before n days date

    @before_days: if yesterday before_days=1
    @format: date format, may be "2016-07-11" or "2016_07_11" ...
    """
    try:
        return (datetime.date.today()-datetime.timedelta(days=before_days)).strftime(format)
    except Exception,e:
        sys.stderr.write('get before [date] exception:[%s]' % (str(e)))
        return None

def get_after_date(after_days = 0, format = "%Y-%m-%d"):
    """
    Get today after n days date

    @after_days: if tomorrow before_days=1
    @format: date format, may be "2016-07-11" or "2016_07_11" ...
    """
    try:
        return (datetime.date.today()-datetime.timedelta(days=-after_days)).strftime(format)
    except Exception,e:
        sys.stderr.write('get after [date] exception:[%s]' % (str(e)))
        return None

def get_cur_datetime(format = '%Y-%m-%d %H:%M:%S'):
    """
    Get current dattetime

    @format: datetime format, may be "2016-07-11 20:15:08" or "2016_07_11_20_15_08" ...
    """
    try:
        return time.strftime(format)
    except Exception,e:
        sys.stderr.write('get current [datetime] exception:[%s]' % (str(e)))
        return None

def get_cur_timestamp(length = 10):
    """
    Get current timestatmp

    @length: 10, 13, 16 three choice, default 10
             a. 10, return may be 1470564059
             b. 13, return may be 1470564059607
             c. 16, return may be 1470564059607434
    """
    try:
        str_timestamp = str(int(time.time() * 1000000))
        return str_timestamp[:length]
    except Exception,e:
        sys.stderr.write('get current [timestamp] exception:[%s]' % (str(e)))
        return None

def timestamp_2_date(timestamp, format = "%Y-%m-%d"):
    """
    transform timestamp to date

    @timestamp: allow 10, 13, 16 length timestamp
    @format: date format, may be "2016-07-11" or "2016_07_11" ...
    """
    try:
        return datetime.date.fromtimestamp(int(str(timestamp)[:10])).strftime(format)
    except Exception,e:
        sys.stderr.write('[timestamp] 2 [date] exception:[%s]' % (str(e)))
        return None

def timestamp_2_datetime(timestamp, format = "%Y-%m-%d %H:%M:%S"):
    """
    transform timestamp to datetime

    @timestamp: allow 10, 13, 16 length timestamp
    @format: datetime format, may be "2016-07-11 20:15:08" or "2016_07_11_20_15_08" ...
    """
    try:
        return datetime.datetime.fromtimestamp(int(str(timestamp)[:10])).strftime(format)
    except Exception,e:
        sys.stderr.write('[timestamp] 2 [datetime] exception:[%s]' % (str(e)))
        return None
