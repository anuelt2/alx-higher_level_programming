#!/usr/bin/python3
"""Script that takes arguments and displays all values in states table of a
database where name matches the argument, protected against MySQL injections
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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s "
                "ORDER BY id ASC", (search_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
