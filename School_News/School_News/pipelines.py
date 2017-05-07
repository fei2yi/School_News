# -*- coding: utf-8 -*-
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
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

    def process_item(self, item, spider):
        curTime = datetime.now()
        print(str(type(item)))
        # < class 'School_News.items.CollegeCityItem'>
        try:
            sql = """INSERT INTO weather
            (weatherDate, weatherDate2, weatherWea, weatherTem1, weatherTem2, weatherWin, updateTime)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.execute(sql,
                                (
                                    item['weatherDate'][0].encode('utf-8'),
                                    item['weatherDate2'][0].encode('utf-8'),
                                    item['weatherWea'][0].encode('utf-8'),
                                    item['weatherTem1'][0].encode('utf-8'),
                                    item['weatherTem2'][0].encode('utf-8'),
                                    item['weatherWin'][0].encode('utf-8'),
                                    curTime,
                                )
                                )
            self.conn.commit()
        except pymysql.Error:
            print("Error")
        return item
