#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    # Start cursor
    cur = db.cursor()

    # Query
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    # Print query
    for row in rows:
        print(row)

    # Close cursor
    cur.close()
    db.close()
