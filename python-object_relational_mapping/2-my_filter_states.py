#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    name_s = state_name_searched

    cur = db.cursor()
    cur.execute("SELECt * FROM states WHERE name = %s ORDER BY id", (name_s,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
