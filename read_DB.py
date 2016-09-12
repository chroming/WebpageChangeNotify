# -*- coding:utf-8 -*-

import sqlite3


# 创建表
def create_table(db_name, table_name):
    conn = sqlite3.connect('%s.db' % db_name)
    cursor = conn.cursor()
    cursor.execute("create table %s (id INTEGER PRIMARY KEY AUTOINCREMENT,result text UNIQUE,date timestamp not null default (datetime('now','localtime')))"%table_name,)
    cursor.close()
    conn.close()


# 读取数据库
def read_db(db_name, table_name, size=100):
    conn = sqlite3.connect('%s.db' % db_name)
    cursor = conn.cursor()
    cursor.execute('select * from ?', table_name)
    result_all = cursor.fetchmany(size)
    cursor.close()
    conn.close()
    return result_all


# 写入数据库
# 由于写入数据库比较耗时,直接将更新的所有传递给write_db
def write_db(db_name, table_name, result_list):
    conn = sqlite3.connect('%s.db' % db_name)
    cursor = conn.cursor()
    new_list = []
    for result in result_list:
        sql = "insert into %s (result) values ('%s')" % (table_name, result)
        #cursor.execute(sql)
        #conn.commit()
        try:
            cursor.execute(sql)
            new_list.append(result)
            conn.commit()
            print(u"写入  "+sql+u" 成功！")
        except:
            print(result+u" 已存在！")
    cursor.close()
    conn.close()
    return new_list


if __name__ == '__main__':
    create_table('test', 'test')


