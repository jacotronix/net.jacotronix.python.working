'''
Created on 18 Dec 2012

@author: Jamie
'''

# install sqlite sqlite3

import sqlite3
import datetime

t=18.5
p=1312

conn = sqlite3.connect("test.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS logging (datetime TIMESTAMP, temp FLOAT, pressure INT)')
c.execute('INSERT INTO logging VALUES(?, ?, ?)', (datetime.datetime.now(), t, p))


conn.commit()

#------------------------------
#
#
#http://stackoverflow.com/questions/1829872/read-datetime-back-from-sqlite-as-a-datetime-in-python
#
#>>> db = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
#>>> c = db.cursor()
#>>> c.execute('create table foo (bar integer, baz timestamp)')
#<sqlite3.Cursor object at 0x40fc50>
#>>> c.execute('insert into foo values(?, ?)', (23, datetime.datetime.now()))
#<sqlite3.Cursor object at 0x40fc50>
#>>> c.execute('select * from foo')
#<sqlite3.Cursor object at 0x40fc50>
#>>> c.fetchall()
#[(23, datetime.datetime(2009, 12, 1, 19, 31, 1, 40113))]