#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import datetime

def get_year():
    return datetime.datetime.today().strftime('%Y')

def get_month():
    return datetime.datetime.today().strftime('%m')

def get_date():
    return datetime.datetime.today().strftime('%d')

def get_hour():
    return datetime.datetime.today().strftime('%H')

def get_minute():
    return datetime.datetime.today().strftime('%M')

def get_second():
    return datetime.datetime.today().strftime('%S')

def get_today_date(format = "%Y-%m-%d"):
    return datetime.date.today().strftime(format)

def get_before_date(before_days = 0, format = "%Y-%m-%d"):
    return (datetime.date.today()-datetime.timedelta(days=before_days)).strftime(format)

def get_after_date(after_days = 0, format = "%Y-%m-%d"):
    return (datetime.date.today()-datetime.timedelta(days=-after_days)).strftime(format)

def get_cur_datetime(format = '%Y-%m-%d %H:%M:%S'):
    return time.strftime(format)

def get_cur_timestamp(length = 10):
    str_timestamp = str(int(time.time() * 1000000))
    return str_timestamp[:length]

def timestamp_2_date(timestamp, format = "%Y-%m-%d"):
    return datetime.date.fromtimestamp(int(str(timestamp)[:10])).strftime(format)

def timestamp_2_datetime(timestamp, format = "%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.fromtimestamp(int(str(timestamp)[:10])).strftime(format)
