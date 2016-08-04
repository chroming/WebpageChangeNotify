# -*- coding:utf-8 -*-
import sqlite3


# 创建表
def create_table(db_name, table_name):
    conn = sqlite3.connect('%s.db' % db_name)
    cursor = conn.cursor()
    try:
        cursor.execute('create table ?(id int auto_increment PRIMARY KEY,result text,time timestamp())', table_name)
    except:
        pass
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
    for result in result_list:
        cursor.execute('insert into ? (result) values (?)', (table_name, result))
        conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    create_table('test', 'test')


