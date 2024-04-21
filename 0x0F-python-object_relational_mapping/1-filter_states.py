#!/usr/bin/python3
"""1-filter_states.py"""
import MySQLdb
import sys


def filter_states():
    """1-filter_states.py"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cur = db.cursor()
    cur.execute("SELECT *\
            FROM states\
            WHERE name LIKE BINARY 'N%'\
            ORDER BY id ASC")
    result = cur.fetchall()
    for num in result:
        print(num)

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()
