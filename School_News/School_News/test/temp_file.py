from datetime import date, datetime, timedelta
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='yyaiyi',
                             db='world',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# 获取明天的时间

cursor = connection.cursor()
# sql = 'CREATE DATABASE School_News'
sql = "CREATE TABLE runoob_tbl(" \
      "a INT NOT NULL AUTO_INCREMENT, "\
        "b VARCHAR(100) NOT NULL, "\
        "c VARCHAR(40) NOT NULL, "\
        "PRIMARY KEY (a)) ENGINE=InnoDB DEFAULT CHARSET=utf8; "
sql2 ='DROP TABLE runoob_tbl ;'
cursor.execute(sql)


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
