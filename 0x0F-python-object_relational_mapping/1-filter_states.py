#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
    Args:
        arg1 mysql username
        arg2 mysql password
        arg3 database name
"""
import MySQLdb
import sys
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY
     'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
