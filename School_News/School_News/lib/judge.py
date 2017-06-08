import pymysql


def judge_table_exist(cursor, tablename):
    try:
        cursor.execute("SELECT * FROM {}".format(tablename))
        return True
    except:
        return False


def conn_database():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='yyaiyi',
                           db='school_news',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn
