from datetime import date, datetime, timedelta
import pymysql
import pymysql.cursors
import re

#
# class MySQLStoreSchool_NewsPipeline(object):
#     def __init__(self):
#         self.conn = pymysql.connect(host='localhost',
#                                     port=3306,
#                                     user='root',
#                                     password='yyaiyi',
#                                     db='school_news',
#                                     charset='utf8mb4',
#                                     cursorclass=pymysql.cursors.DictCursor)
#         self.cursor = self.conn.cursor()
        # 清空表：
        # self.cursor.execute("truncate table")
        # self.conn.commit()

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
