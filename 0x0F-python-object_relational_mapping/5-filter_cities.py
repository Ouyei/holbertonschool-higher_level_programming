#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the cities
    from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    # Query
    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })

        rows = cur.fetchall()

    # Print query
    if rows is not None:
        print(", ".join([row[1] for row in rows]))

    # Close cursor
    cur.close()
    db.close()
