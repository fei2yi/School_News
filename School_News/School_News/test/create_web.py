import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='yyaiyi',
                       db='school_news',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
cursor.execute("SELECT * FROM collegecityitem a INNER "
               "JOIN collegewebitem b ON a.link = b.parent WHERE collegeLevel='普通本科院校(908所)'")

a = cursor.fetchall()


def new_table(table_name):
    try:
        # 产生异常说明此表不存在，无异常则说明表存在。
        cursor.execute("select * from %s" % table_name)
    except:
        if table_name == 'college':
            # 有异常，就会跳到这里，新建表。
            sql = """CREATE TABLE {}(
             url char(100),
             name char(20) ,
             parent char(100) ,
             child char(4),
             PRIMARY KEY (url))""".format(table_name)
            cursor.execute(sql)


def process_i(i):
    table_name = 'college'
    new_table(table_name)
    try:
        if table_name == 'college':
            sql = """INSERT INTO {}
               (name, url, parent,child)
                VALUES (%s, %s, %s ,%s)""".format(table_name)
            cursor.execute(sql,
                           (
                               i.get('name').encode('utf-8'),
                               i.get('url').encode('utf-8'),
                               i.get('parent').encode('utf-8'),
                               0,
                           )
                           )
            conn.commit()
    except:
        print('存储出错！')


def create(a):
    for index, i in enumerate(a):
        print(index, i.get('name'), i.get('url'), i.get('parent'))
        process_i(i)


create(a)
