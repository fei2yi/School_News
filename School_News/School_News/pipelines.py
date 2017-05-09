# -*- coding: utf-8 -*-
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import re
import pymysql
import pymysql.cursors


class SchoolNewsPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLStoreSchool_NewsPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='yyaiyi',
                                    db='world',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()
        # 清空表：
        # self.cursor.execute("truncate table")
        # self.conn.commit()

    def new_table(self, table_name):
        try:
            # 产生异常说明此表不存在，无异常则说明表存在。
            self.cursor.execute("select * from %s" % table_name)
        except:
            # 有异常，就会跳到这里，新建表。
            sql = """CREATE TABLE %s(
             list1 char(100),
             list2 char(100) ,
             list3 char(100) ,
             list4 char(100))""" % table_name
            self.cursor.execute(sql)

    def process_item(self, item, spider):
        print(str(type(item)))
        table_name = re.split('\.|\'', str(type(item)))[-2]
        self.new_table(table_name)
        # < class 'School_News.items.CollegeCityItem'>

        try:
            sql = """INSERT INTO {}
            (list1, list2, list3, list4)
             VALUES (%s, %s, %s, %s)""".format(table_name)
            self.cursor.execute(sql,
                                (
                                    item['province'].encode('utf-8'),
                                    item['link'].encode('utf-8'),
                                    item['collegeSum'].encode('utf-8'),
                                    item['collegeLevel'].encode('utf-8'),

                                )
                                )
            self.conn.commit()
        except pymysql.Error:
            print("Error")
        return item
