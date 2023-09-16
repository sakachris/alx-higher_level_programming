#!/usr/bin/python3

"""
module for listing states from a database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    qry = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
    ORDER BY states.id ASC".format(argv[4])
    cur.execute(qry)
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
