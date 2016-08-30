#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import logging
import warnings
import MySQLdb
#warnings.filterwarnings('ignore')

FORMAT = '[%(levelname)s] [%(asctime)s] [%(filename)s::%(funcName)s::%(lineno)d] [%(message)s]'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('mysql_util')

def db_connect(host, port, user, passwd, db, charset="utf8"):
    """
    Create db connect obj

    @host: mysql host
    @port: mysql host port
    @user: connect mysql user
    @passwd: connect mysql password
    @db: mysql db
    @charset: connect charset, default equal utf-8

    return connect obj
    """

    return MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)

def execute_sql(db, cursor, sql):
    """
    Exceute sql

    @db: db connect obj
    @cursor: mysql cursor
    @sql: sql

    """
    try:
        cursor.execute(sql)
    except Exception, e:
        logger.error('exceute sql:[%s] exception:[%s]' % (sql, str(e)))

def transaction(db, cursor, sql):
    """
    Transaction sql

    @db: db connect obj
    @cursor: mysql cursor
    @sql: sql

    """
    try:
        execute_sql(db, cursor, sql)
        db.commit()
    except:
        logger.error('transaction sql:[%s] exception:[%s]' % (sql, str(e)))
        db.rollback()

def add_table(db, sql):
    """
    Add mysql table

    @db: db connect obj
    @sql: sql

    return True/False
    """
    try:
        cursor = db.cursor()
        execute_sql(db, cursor, sql)
        return True
    except Exception, e:
        logger.error('add table sql:[%s] exception:[%s]' % (sql, str(e)))
        return False

def delete_table(db, sql):
    """
    Delete mysql table

    @db: db connect obj
    @sql: sql

    return True/False
    """
    try:
        cursor = db.cursor()
        execute_sql(db, cursor, sql)
        return True
    except Exception, e:
        logger.error('delete table sql:[%s] exception:[%s]' % (sql, str(e)))
        return False

def select(db, sql):
    """
    Select mysql table

    @db: db connect obj
    @sql: sql

    return results list, return None when exception
    """
    try:
        cursor = db.cursor()
        execute_sql(db, cursor, sql)
        results = cursor.fetchall()
        return results
    except Exception, e:
        logger.error('table select sql:[%s] exception:[%s]' % (sql, str(e)))
        return None

def insert(db, sql):
    """
    Insert mysql table

    @db: db connect obj
    @sql: sql

    return True/False
    """
    try:
        cursor = db.cursor()
        transaction(db, cursor, sql):
        return True
    except Exception, e:
        logger.error('table insert sql:[%s] exception:[%s]' % (sql, str(e)))
        return False

def update(db, sql):
    """
    Update mysql table

    @db: db connect obj
    @sql: sql

    return True/False
    """
    try:
        cursor = db.cursor()
        transaction(db, cursor, sql):
        return True
    except Exception, e:
        logger.error('table update sql:[%s] exception:[%s]' % (sql, str(e)))
        return False

def delete(db, sql):
    """
    Delete mysql table

    @db: db connect obj
    @sql: sql

    return True/False
    """
    try:
        cursor = db.cursor()
        transaction(db, cursor, sql):
        return True
    except Exception, e:
        logger.error('table delete sql:[%s] exception:[%s]' % (sql, str(e)))
        return False

