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
        sentence = "每一行分三部分词语、词频（可省略）、词性（可省略），用空格隔开"
        seg_list = ws_client.cut(sentence)
        print '\t'.join(seg_list)

        sentence = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造"
        seg_list = ws_client.cut(sentence)
        print '\t'.join(seg_list)

        sentence = "李小福是创新办主任也是云计算方面的专家"
        seg_list = ws_client.cut(sentence)
        print '\t'.join(seg_list)

        ws_client = word_segment.WordSegment("./data/user_dict.dat")
        sentence = "每一行分三部分词语、词频（可省略）、词性（可省略），用空格隔开"
        seg_list = ws_client.cut(sentence)
        print '\t'.join(seg_list)

        sentence = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造"
        seg_list = ws_client.cut(sentence)
        print '\t'.join(seg_list)

        sentence = "李小福是创新办主任也是云计算方面的专家"
        seg_list = ws_client.cut(sentence)
        print '\t'.join(seg_list)

    def print_weight_list(self, seg_list):
        for item in seg_list:
            print item[0] + ":" + str(item[1]) + "\t",
        print ""

    def test_cut_with_weight(self):
        ws_client = word_segment.WordSegment()
        sentence = "每一行分三部分词语、词频（可省略）、词性（可省略），用空格隔开"
        seg_list = ws_client.cut_with_weight(sentence)
        self.print_weight_list(seg_list)

        sentence = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造"
        seg_list = ws_client.cut_with_weight(sentence)
        self.print_weight_list(seg_list)

        sentence = "李小福是创新办主任也是云计算方面的专家"
        seg_list = ws_client.cut_with_weight(sentence)
        self.print_weight_list(seg_list)

        ws_client = word_segment.WordSegment("./data/user_dict.dat")
        sentence = "每一行分三部分词语、词频（可省略）、词性（可省略），用空格隔开"
        seg_list = ws_client.cut_with_weight(sentence)
        self.print_weight_list(seg_list)

        sentence = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造"
        seg_list = ws_client.cut_with_weight(sentence)
        self.print_weight_list(seg_list)

        sentence = "李小福是创新办主任也是云计算方面的专家"
        seg_list = ws_client.cut_with_weight(sentence)
        self.print_weight_list(seg_list)

if __name__ == '__main__':
    unittest.main()
