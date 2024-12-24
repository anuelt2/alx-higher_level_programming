#!/usr/bin/python3
"""Script that takes in name of a state as an argument and lists all
cities if that state
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

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
            SELECT cities.name
            FROM cities
            JOIN states
            ON cities.state_id = states.id
            WHERE states.name LIKE BINARY %s
            ORDER BY cities.id ASC
            """,
            (state_name,)
            )
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))
    cur.close()
    conn.close()
