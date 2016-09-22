#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append('../py_util')
import config_parse
import word_segment

class WordSegmentTest(unittest.TestCase):
    def test_cut(self):
        ws_client = word_segment.WordSegment()
        word_str = "每一行分三部分词语、词频（可省略）、词性（可省略），用空格隔开"
        seg_list = ws_client.cut(word_str)
        print '\t'.join(seg_list)

if __name__ == '__main__':
    unittest.main()
