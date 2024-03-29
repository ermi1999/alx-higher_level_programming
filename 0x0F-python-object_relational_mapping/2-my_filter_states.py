#!/usr/bin/python3
"""
This takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
    Args:
        Arg1: mysql username.
        Arg2: mysql password.
        Arg3: database name
        Arg4: state name searched
"""
import MySQLdb
import sys
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = BINARY '{}'"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
