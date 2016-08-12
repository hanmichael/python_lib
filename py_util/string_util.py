#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def is_string(obj):
    """
    Check obj is str or unicode instance

    @obj: input value

    return True/False
    """
    try:
        return isinstance(obj, (str, unicode))
    except Exception,e:
        print 'check obj is string exception:[%s]' % (str(e))
        return False
