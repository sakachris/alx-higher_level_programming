#!/usr/bin/python3

"""
script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    qry = "SELECT * FROM states WHERE name LIKE BINARY %s\
    ORDER BY states.id ASC"
    matches = (argv[4],)
    cur.execute(qry, matches)
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
