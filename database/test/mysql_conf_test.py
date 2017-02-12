#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append('../')
from mysql_conf import MysqlConfig

class MysqlConfigTest(unittest.TestCase):
    def test_mysql_conf(self):
        mysql_config = MysqlConfig()
        mysql_config.__debug_config__()

        mysql_config = MysqlConfig(hostname='localhost')
        mysql_config.__debug_config__()

        mysql_config = MysqlConfig(hostname='localhost', port='3306')
        mysql_config.__debug_config__()

        mysql_config = MysqlConfig(hostname='localhost', port='3306', user='chenguolin')
        mysql_config.__debug_config__()

        mysql_config = MysqlConfig(hostname='localhost', port='3306', user='chenguolin', password='password')
        mysql_config.__debug_config__()

        mysql_config = MysqlConfig(hostname='localhost', port='3306', user='chenguolin', password='password', db='test_db')
        mysql_config.__debug_config__()

        mysql_config = MysqlConfig(hostname='localhost', port='3306', user='chenguolin', password='password', db='test_db', charset='utf8')
        mysql_config.__debug_config__()

if __name__ == '__main__':
    unittest.main()
