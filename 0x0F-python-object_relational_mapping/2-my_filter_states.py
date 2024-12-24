#!/usr/bin/python3
"""Script that takes an argument and displays all values in states table
that matches argument
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    search_name = argv[4]

    conn = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=db_name,
            port=3306
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                .format(search_name))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
