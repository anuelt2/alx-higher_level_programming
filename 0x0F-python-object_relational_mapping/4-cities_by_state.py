#!/usr/bin/python3
"""Script that lists all cities from a database"""
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
    cur.execute(
        """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
        )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
