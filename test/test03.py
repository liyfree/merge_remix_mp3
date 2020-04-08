#!/usr/bin/env python3
# -*-coding:utf-8-*-
from test.db_util import DB

with DB(host='localhost', user='root', password='root', db_name='ly_test') as db:
    db.execute('select * from staff limit 0, 10')
    results = db.fetchall()
    for i in results:
        print(i)

print('*' * 100)

with DB(host='localhost', user='root', password='root', db_name='ly_test') as db:
    db.execute('select * from staff limit 0, 10')
    results = db.fetchmany(3)
    print(results)

print('*' * 100)

with DB(host='localhost', user='root', password='root', db_name='ly_test') as db:
    db.execute('select * from staff limit 0, 10')
    results = db.fetchone()
    print(results)
