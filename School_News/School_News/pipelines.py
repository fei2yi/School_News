# -*- coding: utf-8 -*-
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import re
import sys
import pymysql
import pymysql.cursors
from datetime import datetime
from School_News.lib.common_lib import write_file


class SchoolNewsPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLDBPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='yyaiyi',
                                    db='school_news',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def new_table(self, table_name):
        try:
            # 产生异常说明此表不存在，无异常则说明表存在。
            self.cursor.execute("select * from %s" % table_name)
        except:
            if table_name == 'City':
                # 有异常，就会跳到这里，新建表。
                sql = """CREATE TABLE {}(
                 link char(100) ,
                 province char(10),
                 collegeSum char(20) ,
                 collegeLevel char(20),
                 PRIMARY KEY ( link ))""".format(table_name)
                self.cursor.execute(sql)
            if table_name == 'College':
                # 有异常，就会跳到这里，新建表。
                sql = """CREATE TABLE {}(
                 url char(100),
                 name char(20) ,
                 parent char(100) ,
                 PRIMARY KEY (url))""".format(table_name)
                self.cursor.execute(sql)
            if table_name == 'Listtemp':
                # 有异常，就会跳到这里，新建表。
                sql = """CREATE TABLE {}(
                 listUrl char(100),
                 list char(20) ,
                 parent char(100) ,
                 PRIMARY KEY (listUrl))""".format(table_name)
                self.cursor.execute(sql)
            if table_name == 'List':
                # 有异常，就会跳到这里，新建表。
                sql = """CREATE TABLE {}(
                 listUrl char(100),
                 list char(20) ,
                 xpath char(40) ,
                 parent char(100) ,
                 PRIMARY KEY (listUrl))""".format(table_name)
                self.cursor.execute(sql)
            if table_name == 'Page':
                # 有异常，就会跳到这里，新建表。
                sql = """CREATE TABLE {}(
                 pageUrl char(100),
                 pageNum char(10) ,
                 pageSum char(10) ,
                 parent char(100),
                 PRIMARY KEY (pageUrl))""".format(table_name)
                self.cursor.execute(sql)
            if table_name == 'Article':
                # 有异常，就会跳到这里，新建表。
                sql = """CREATE TABLE {}(
                 textUrl char(100),
                 title char(40) ,
                 publishTime char(20) ,
                 parent char(100),
                 PRIMARY KEY (textUrl))""".format(table_name)
                self.cursor.execute(sql)
            if table_name == 'Content':
                # 有异常，就会跳到这里，新建表。
                sql = """CREATE TABLE {}(
                 content VARCHAR(10000),
                 author char(5) ,
                 source char(10) ,
                 parent char(100) ,
                 fileUrls char(100) ,
                 filePaths char(100) ,
                 fileNames char(30) ,
                 publishTime char(10),
                 crawl char(3))""".format(table_name)
                self.cursor.execute(sql)

    def process_item(self, item, spider):
        table_name = re.split('\.|\'', str(type(item)))[-2]
        self.new_table(table_name)
        # < class 'School_News.items.CollegeCityItem'>
        try:
            if table_name == 'City':
                sql = """INSERT INTO {}
                   (province, link, collegeSum, collegeLevel)
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
            if table_name == 'College':
                sql = """INSERT INTO {}
                   (name, url, parent,child)
                    VALUES (%s, %s, %s ,%s)""".format(table_name)
                self.cursor.execute(sql,
                                    (
                                        item['name'].encode('utf-8'),
                                        item['url'].encode('utf-8'),
                                        item['parent'].encode('utf-8'),
                                        0
                                    )
                                    )
                self.conn.commit()
            if table_name == 'Listtemp':
                sql = """INSERT INTO {}
                   (list, listUrl, parent)
                    VALUES (%s, %s, %s)""".format(table_name)
                self.cursor.execute(sql,
                                    (
                                        item['list'].encode('utf-8'),
                                        item['listUrl'].encode('utf-8'),
                                        item['parent'].encode('utf-8')
                                    )
                                    )
                self.conn.commit()
            if table_name == 'List':
                sql = """INSERT INTO {}
                   (list,listUrl,xpath,parent)
                    VALUES (%s, %s, %s,%s)""".format(table_name)
                self.cursor.execute(sql,
                                    (
                                        item['list'].encode('utf-8'),
                                        item['listUrl'].encode('utf-8'),
                                        item['xpath'].encode('utf-8'),
                                        item['parent'].encode('utf-8'),
                                    )
                                    )
                self.conn.commit()
            if table_name == 'Page':
                sql = """INSERT INTO {}
                   (pageUrl, pageNum, pageSum, parent)
                    VALUES (%s, %s, %s, %s)""".format(table_name)
                self.cursor.execute(sql,
                                    (
                                        item['pageUrl'].encode('utf-8'),
                                        item['pageNum'].encode('utf-8'),
                                        item['pageSum'].encode('utf-8'),
                                        item['parent'].encode('utf-8'),
                                    )
                                    )
                self.conn.commit()
            if table_name == 'Article':
                sql = """INSERT INTO {}
                   (title, textUrl, publishTime, parent)
                    VALUES (%s, %s, %s, %s)""".format(table_name)
                self.cursor.execute(sql,
                                    (
                                        item['title'].encode('utf-8'),
                                        item['textUrl'].encode('utf-8'),
                                        item['publishTime'].encode('utf-8'),
                                        item['parent'].encode('utf-8'),
                                    )
                                    )
                self.conn.commit()
            if table_name == 'Content':
                sql = """INSERT INTO {}
                   (author, source, publishTime, content,fileUrls, filePaths, fileNames, parent,crawl)
                    VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s)""".format(table_name)
                self.cursor.execute(sql,
                                    (
                                        item['author'].encode('utf-8'),
                                        item['source'].encode('utf-8'),
                                        item['publishTime'].encode('utf-8'),
                                        item['content'].encode('utf-8'),
                                        item['fileUrls'].encode('utf-8'),
                                        item['filePaths'].encode('utf-8'),
                                        item['fileNames'].encode('utf-8'),
                                        item['parent'].encode('utf-8'),
                                        item['crawl'].encode('utf-8'),
                                    )
                                    )
                self.conn.commit()
        except:
            write_file('pymysql_Error.txt', item['textUrl'] + ' ' + str(sys.exc_info())+' '+str(datetime.now())+'\n')
        return item



        #     try:
        #         item['listUrl']
        #     except KeyError:
        #         write_file('pymysql_Error.txt', item['parent'] + ' ' + 'KeyError')
        #     write_file('pymysql_Error.txt', item['listUrl'] + ' ' + 'pymysql.Error')
        # except pymysql.err.IntegrityError:
        #     write_file('pymysql_Error.txt', item['listUrl'] + ' ' + 'pymysql.err.IntegrityError')
