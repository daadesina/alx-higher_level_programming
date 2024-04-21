#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""

import MySQLdb
import sys

def my_func():
    """python3 -c 'print(__import__("my_module").__doc__)'"""
    connection = MySQLdb.connect(
            user=sys.argv[1],
            host='localhost',
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM states;')
        record = (cursor.fetchall())
        for num in record:
            print(num)

    if connection.is_connected():
        cursor.close()
        connection.close()

if __name__=="__main__":
    my_func()
