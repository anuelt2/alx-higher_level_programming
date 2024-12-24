#!/usr/bin/python3
"""Script that lists all states from a database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=db_name,
            port=3306
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
