#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append('../py_util')
import datetime_util

class DatetimeUtilTest(unittest.TestCase):
    @unittest.skip("skip get year")
    def test_get_year(self):
        self.assertEqual('2016', datetime_util.get_year())

    @unittest.skip("skip get month")
    def test_get_month(self):
        self.assertEqual('08', datetime_util.get_month())

    @unittest.skip("skip get day")
    def test_get_day(self):
        self.assertEqual('14', datetime_util.get_day())

    @unittest.skip("skip get hour")
    def test_get_hour(self):
        self.assertEqual('23', datetime_util.get_hour())

    @unittest.skip("skip get minute")
    def test_get_minute(self):
        self.assertEqual('42', datetime_util.get_minute())

    @unittest.skip("skip get second")
    def test_get_second(self):
        self.assertEqual('16', datetime_util.get_second())

    @unittest.skip("skip get today date")
    def test_get_today_date(self):
        self.assertEqual('2016-08-14', datetime_util.get_today_date())
        self.assertEqual('2016/08/14', datetime_util.get_today_date("%Y/%m/%d"))

    @unittest.skip("skip get yesterday date")
    def test_get_yesterday_date(self):
        self.assertEqual('2016-08-13', datetime_util.get_yesterday_date())
        self.assertEqual('2016/08/13', datetime_util.get_yesterday_date("%Y/%m/%d"))

    @unittest.skip("skip get tomorrow date")
    def test_get_tomorrow_date(self):
        self.assertEqual('2016-08-15', datetime_util.get_tomorrow_date())
        self.assertEqual('2016/08/15', datetime_util.get_tomorrow_date("%Y/%m/%d"))

    @unittest.skip("skip get before date")
    def test_get_before_date(self):
        self.assertEqual('2016-08-09', datetime_util.get_before_date(5))
        self.assertEqual('2016/08/09', datetime_util.get_before_date(5, "%Y/%m/%d"))

    @unittest.skip("skip get after date")
    def test_get_after_date(self):
        self.assertEqual('2016-08-19', datetime_util.get_after_date(5))
        self.assertEqual('2016/08/19', datetime_util.get_after_date(5, "%Y/%m/%d"))

    @unittest.skip("skip get current datetime")
    def test_get_cur_datetime(self):
        self.assertEqual('2016-08-14 23:45:45', datetime_util.get_cur_datetime())

    @unittest.skip("skip get current timestamp")
    def test_get_cur_timestamp(self):
        self.assertEqual('1470564059', datetime_util.get_cur_timestamp())
        self.assertEqual('1470564059123', datetime_util.get_cur_timestamp(13))
        self.assertEqual('1470564059123456', datetime_util.get_cur_timestamp(16))

    def test_timestamp_2_date(self):
        self.assertEqual('2016-08-14', datetime_util.timestamp_2_date(1471190138))
        self.assertEqual('2016/08/14', datetime_util.timestamp_2_date(1471190138, "%Y/%m/%d"))
        self.assertEqual('2016-08-14', datetime_util.timestamp_2_date(1471190138123))
        self.assertEqual('2016-08-14', datetime_util.timestamp_2_date(1471190138123456))

    def test_timestamp_2_datetime(self):
        self.assertEqual('2016-08-14 23:55:38', datetime_util.timestamp_2_datetime(1471190138))
        self.assertEqual('2016/08/14 23:55:38', datetime_util.timestamp_2_datetime(1471190138, "%Y/%m/%d %H:%M:%S"))
        self.assertEqual('2016-08-14 23:55:38', datetime_util.timestamp_2_datetime(1471190138123))
        self.assertEqual('2016-08-14 23:55:38', datetime_util.timestamp_2_datetime(1471190138123456))

    def test_date_2_timestamp(self):
        self.assertEqual(1471104000, datetime_util.date_2_timestamp("2016-08-14"))
        self.assertEqual(1471104000, datetime_util.date_2_timestamp("2016/08/14", "%Y/%m/%d"))

    def test_datetime_2_timestamp(self):
        self.assertEqual(1471190138, datetime_util.datetime_2_timestamp("2016-08-14 23:55:38"))
        self.assertEqual(1471190138, datetime_util.datetime_2_timestamp("2016/08/14 23:55:38", "%Y/%m/%d %H:%M:%S"))

if __name__ == '__main__':
    unittest.main()
