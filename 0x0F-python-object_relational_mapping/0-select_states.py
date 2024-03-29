#!/usr/bin/python3
"""This program lists all states from the database hbtn_0e_0_usa
        Arg1:
            mysql username
        Arg2:
            mysql password
        Arg3:
            database name.
"""
import MySQLdb
import sys
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
