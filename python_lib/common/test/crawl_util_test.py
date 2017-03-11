#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append('../py_util')
import crawl_util

class CrawlUtilTest(unittest.TestCase):
    def test_crawl_page(self):
        url = ''
        html_page = crawl_util.crawl_page(url)
        self.assertEqual(None, html_page)

        url = 'http://www.baidu.com/'
        html_page = crawl_util.crawl_page(url)
        #print html_page

        url = 'http://jkj.juanpi.com/'
        html_page = crawl_util.crawl_page(url)
        #print html_page

    def test_crawl_final_url(self):
        url = ''
        final_url = crawl_util.crawl_final_url(url)
        self.assertEqual(None, final_url)

        url = 'http://www.baidu.com/'
        final_url = crawl_util.crawl_final_url(url)
        self.assertEqual('https://www.baidu.com/', final_url)

        url = 'http://www.liuzhuni.com/'
        final_url = crawl_util.crawl_final_url(url)
        self.assertEqual('http://www.huim.com/', final_url)

        url = 'http://go.smzdm.com/235bb3865d3d66b9/ca_aa_yh_163_6388742_569_1933_165'
        final_url = crawl_util.crawl_final_url(url)
        print final_url

if __name__ == '__main__':
    unittest.main()
