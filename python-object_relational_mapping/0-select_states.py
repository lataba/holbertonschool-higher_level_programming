#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":

    connection = MySQLdb.connect(
                    user=sys.argv[1],
                    password=sys.argv[2],
                    db=sys.argv[3])
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    states_data = cursor.fetchall()
    [print(state) for state in states_data]

    cursor.close()
    connection.close()
