from datetime import date, datetime, timedelta
import pymysql
import re
import time, sched
import random


def process_item(self, item, spider):
    table_name = re.split('\.|\'', str(type(item)))[-2]
    sql = """INSERT INTO {} (name, url, parent,child)
        VALUES (%s,)""".format(table_name)
    self.cursor.execute(sql,(
                            item['name'].encode('utf-8'),))
    self.conn.commit()


# li = ['dada', 'www', 'wweee']
# random.shuffle(li)
# print(li)
# tag_attr = [
#     (['table', 'thead', 'tbody', 'tfoot', 'th', 'tr', 'td'],
#      ['style', 'align', 'valign', 'width', 'colspan', 'rowspan']),
#     # (['img'],
#     # ['width', 'height', 'src'])
# ]
# tag_attr = {k: vs for ks, vs in tag_attr for k in ks}
# for ks, vs in tag_attr:
#     print(ks,vs)
# print(tag_attr)
# str = input("Enter your input: ")
# print(str)

# # 被调度触发的函数
# def event_func(msg):
#     print("Current Time:", time.time(), 'msg:', msg)
#
#     # 初始化sched模块的scheduler类
#     s = sched.scheduler(time.time, time.sleep)
#     # 设置两个调度
#     while 1:
#         s.enter(2, 2, event_func, ("Small event.",))
#         s.enter(3, 1, event_func, ("Big event.",))
#         s.run()
#     while True:
#         time.sleep(3)

# a = 'http://news.sasu.edu.cn/index.php'
# b = a.split('.')
# print(len(b[4]))

# def process_item(self, item, spider):
#     if isinstance(item, WhoscoredNewItem):
#         table_name = item.pop('table_name')
#         col_str = ''
#         row_str = ''
#         for key in item.keys():
#             col_str = col_str + " " + key + ","
#             row_str = "{}'{}',".format(row_str, item[key] if "'" not in item[key] else item[key].replace("'", "\\'"))
#             sql = "insert INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE ".format(table_name, col_str[1:-1],
#                                                                                     row_str[:-1])
#         for (key, value) in six.iteritems(item):
#             sql += "{} = '{}', ".format(key, value if "'" not in value else value.replace("'", "\\'"))
#         sql = sql[:-2]
#         self.cursor.execute(sql)  # 执行SQL
#         self.cnx.commit()  # 写入操作

#

def aww():
    conn = pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='yyaiyi',
                                db='school_news',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    sql = """IF EXISTS Listtemp"""
    cursor.execute(sql)
    conn.commit()
aww()
# def new_table(self, table_name):
#     d = self.cursor.execute("select * from school_news")
#     e = self.cursor.execute("show databases")
#     if table_name not in d:
#         sql = """CREATE TABLE %s(
#                #      list1 char(100),
#                #      list2 char(100) ,
#                #      list3 char(100) ,
#                #      list4 char(100))""" % table_name
#         self.cursor.execute(sql)

# try:
#     # 产生异常说明此表不存在，无异常则说明表存在。
#     self.cursor.execute("select * from %s" % table_name)
# except:
#     # 有异常，就会跳到这里，新建表。
#     sql = """CREATE TABLE %s(
#      list1 char(100),
#      list2 char(100) ,
#      list3 char(100) ,
#      list4 char(100))""" % table_name
#     self.cursor.execute(sql)

# def process_item(self, item, spider):
#     # print(str(type(item)))
#     # table_name = re.split('\.|\'', str(type(item)))[-2]
#     self.new_table(item)
#     # < class 'School_News.items.CollegeCityItem'>

# try:
#     sql = """INSERT INTO {}
#     (list1, list2, list3, list4)
#      VALUES (%s, %s, %s, %s)""".format(table_name)
#     self.cursor.execute(sql,
#                         (
#                             item['province'].encode('utf-8'),
#                             item['link'].encode('utf-8'),
#                             item['collegeSum'].encode('utf-8'),
#                             item['collegeLevel'].encode('utf-8'),
#
#                         )
#                         )
#     self.conn.commit()
# except pymysql.Error:
#     print("Error")


# MySQLStoreSchool_NewsPipeline().process_item('a', 1)
# import re
#
# a="< class 'School_News.items.CollegeCityItem'>"
# # 四个分隔符为：,  ;  *  \n
# x= re.split('\.|\'',a)
# print(x[-2])
# # import time, sched
#
#
# # 被调度触发的函数
# def event_func(msg):
#     print("Current Time:", time.time(), 'msg:', msg)
#
#     # 初始化sched模块的scheduler类
# s = sched.scheduler(time.time, time.sleep)
# # 设置两个调度
# while 1:
#     s.enter(2, 2, event_func, ("Small event.",))
#     s.enter(3, 1, event_func, ("Big event.",))
#     s.run()
# # while True:
#     time.sleep(3)
# import pymysql.cursors
#
# # Connect to the database
# connection = pymysql.connect(host='localhost',
#                              port=3306,
#                              user='root',
#                              password='yyaiyi',
#                              db='world',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# 获取明天的时间

# cursor = connection.cursor()
# # sql = 'CREATE DATABASE School_News'
# sql = "CREATE TABLE runoob_tbl(" \
#       "a INT NOT NULL AUTO_INCREMENT, "\
#         "b VARCHAR(100) NOT NULL, "\
#         "c VARCHAR(40) NOT NULL, "\
#         "PRIMARY KEY (a)) ENGINE=InnoDB DEFAULT CHARSET=utf8; "
# sql2 ='DROP TABLE runoob_tbl ;'
# cursor.execute(sql)


# 执行sql语句
# try:
#     with connection.cursor() as cursor:
#         # 执行sql语句，插入记录
#         sql = 'INSERT INTO city (first_name, last_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)'
#         cursor.execute(sql, ('Robin', 'Zhyea', tomorrow, 'M', date(1989, 6, 14)))
#     # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
#     connection.commit()
#
# finally:
#     connection.close()



# aList = []
# for i in range(5):
#     aList.append(  i )
# print(aList)
