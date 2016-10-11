#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging
import warnings
import hashlib
import jieba
from itertools import groupby
#warnings.filterwarnings("ignore")

FORMAT = "[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]"
logging.basicConfig(format=FORMAT)
logger = logging.getLogger("simhash")

class Simhash(object):
    def __init__(self, doc_str, hash_bit=64, top_sentence=None):
        self.doc_str = doc_str
        self.hash_bit = hash_bit
        self.top_sentence = top_sentence
        self.all_stop_char = ["。","，","、","＇","：","∶","；","?","‘","’","“","”","〝","〞","ˆ","ˇ","﹕","︰","﹔","﹖","﹑","·","¨","…",".","¸",";","！","´","？","！","～","—","ˉ","｜","‖","＂","〃","｀","@","﹫","¡","¿","﹏","﹋","﹌","︴","々","﹟","#","﹩","$","﹠","&","﹪","%","*","﹡","﹢","﹦","﹤","‐","￣","¯","―","﹨","ˆ","˜","﹍","﹎","+","=","<","＿","_","-","\\","ˇ","~","﹉","﹊","（","）","〈","〉","‹","›","﹛","﹜","『","』","〖","〗","［","］","《","》","〔","〕","{","}","「","」","【","】","︵","︷","︿","︹","︽","_","﹁","﹃","︻","︶","︸","﹀","︺","︾","ˉ","﹂","﹄","︼",")","("]
        self.all_blank_char = [" ", "\t", "\n", "\r", "\r\n"]

    def __normalize__(self):
        doc_str = self.doc_str.lower()
        for char in self.all_stop_char:
            doc_str = doc_str.replace(char, '')
        for char in self.all_blank_char:
            doc_str = doc_str.replace(char, '')
        self.doc_str = doc_str

    def __cut__(self):
        seg_list = jieba.lcut(self.doc_str, cut_all=False, HMM=True)
        return [item.encode("utf-8") for item in seg_list]

    def __hash__(self, seg_str):
        if self.hash_bit == 32:
            return str(bin(int(hashlib.md5(seg_str).hexdigest()[12:20], 16)))[2:]
        elif self.hash_bit == 64:
            return str(bin(int(hashlib.md5(seg_str).hexdigest()[8:24], 16)))[2:]
        else:
            return str(bin(int(hashlib.md5(seg_str).hexdigest(), 16)))[2:]

    def __calc_simhash__(self, seg_list):
        weight_dict = {}
        for pair in seg_list:
            bin_str, weight = pair
            pos = 0
            for c in bin_str:
                if pos not in weight_dict:
                    weight_dict[pos] = 0
                if int(c) == 1:
                    weight_dict[pos] += weight
                else:
                    weight_dict[pos] -= weight
                pos += 1
        new_bin_str = ''
        for pos, sum_value in weight_dict.items():
            if sum_value > 0:
                new_bin_str += '1'
            else:
                new_bin_str += '0'
        return int(new_bin_str, 2)

    def calc(self):
        try:
            self.__normalize__()
            seg_list = self.__cut__()
            new_seg_list = []
            for key, group in groupby(sorted(seg_list)):
                new_seg_list.append((self.__hash__(key), len(list(group))))
            # sort by weight
            new_seg_list.sort(key=lambda pair:pair[1], reverse=True)
            if self.top_sentence is not None:
                new_seg_list = new_seg_list[:self.top_sentence]
            return self.__calc_simhash__(new_seg_list)
        except Exception,e:
            logger.error('calc doc string:[%s] exception:[%s]\n' % (self.doc_str, str(e)))
            return None

def calc_simhash(doc_str, hash_bit=64, top_sentence=None):
    """
    Calc doc string simhash value

    @doc_str: input doc string
    @hash_bit: calc hash bit simhash value, default 64

    return int value
    """
    try:
        simhash_obj = Simhash(doc_str, hash_bit, top_sentence)
        return simhash_obj.calc()
    except Exception,e:
        logger.error('calc_simhash function exception:[%s]\n' % str(e))
        return None

def hamming_distance(simhash1, simhash2):
    """
    Calc two simhash value hamming distance

    @simhash1: first simhash value
    @simhash2: second simhash value

    return distance
    """
    try:
        bin_str1 = bin(simhash1)
        bin_str2 = bin(simhash2)
        if len(bin_str1) != len(bin_str2):
            logger.error('two simhash value length not equal')
            return None
        return sum(c1 != c2 for c1, c2 in zip(bin_str1, bin_str2))
    except Exception,e:
        logger.error('hamming_distance function exception:[%s]\n' % str(e))
        return None

def is_similar(simhash1, simhash2, min_dis_count = 3):
    """
    Check two simhash value is similar

    @simhash1: first simhash value
    @simhash2: second simhash value
    @min_dis_count: min distance count

    return True/False
    """
    try:
        dis = hamming_distance(simhash1, simhash2)
        if dis is None or dis > min_dis_count:
            return False
        return True
    except Exception,e:
        logger.error('is_similar function exception:[%s]\n' % str(e))
        return False
