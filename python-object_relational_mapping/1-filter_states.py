#!/usr/bin/python3
""""
Lists all states with a name starting with N
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
    [print(state) for state in states_data if state[1][0] == "N"]

    cursor.close()
    connection.close()
