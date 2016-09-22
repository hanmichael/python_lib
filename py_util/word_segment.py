#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import logging
import warnings
import jieba
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
        if user_dict is not None:
            jieba.load_userdict(user_dict)

    def cut(self, word_str):
        """
        Cut word string

        @word_str: word string

        return list or None
        """
        try:
            seg_list = list(jieba.cut(word_str, cut_all=False, HMM=True))
            return [item.encode('utf-8') for item in seg_list]
        except Exception,e:
            logger.error('check is json exception:[%s]' % (str(e)))
            return None
