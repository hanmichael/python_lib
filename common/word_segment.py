#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import logging
import warnings
import jieba
import jieba.analyse
#warnings.filterwarnings('ignore')

FORMAT = '[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('word_segment')

class WordSegment(object):
    def __init__(self, user_dict=None):
        """
        Init WordSegment Client

        @user_dict: user dict

        每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开
        """
        self.user_dict = user_dict
        if self.user_dict is not None:
            jieba.load_userdict(self.user_dict)

    def cut(self, sentence):
        """
        Cut word string

        @sentence: word string

        return list or None
        ["word1", "word2" ...]
        """
        try:
            seg_list = jieba.lcut(sentence, cut_all=False, HMM=True)
            return [item.encode('utf-8') for item in seg_list]
        except Exception,e:
            logger.error('cut sentence:[%s] exception:[%s]' % (sentence, str(e)))
            return None

    def cut_with_weight(self, sentence, top_k=None):
        """
        Cut word string with weight

        @sentence: word string
        @top_k: return top k weight item, default return all

        return list or None
        ["word1`weight1", "word2`weight2" ...]
        """
        try:
            if top_k is None:
                top_k = 2147483647
            seg_list = jieba.analyse.extract_tags(sentence, topK=top_k, withWeight=True)
            return [(item[0].encode('utf-8'), item[1]) for item in seg_list]
        except Exception,e:
            logger.error('cut sentence:[%s] exception:[%s]' % (sentence, str(e)))
            return None
