#!/usr/bin/python3
""""
Lists all cities from the database hbtn_0e_4_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":

    connection = MySQLdb.connect(
                    user=sys.argv[1],
                    password=sys.argv[2],
                    db=sys.argv[3])
    cursor = connection.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name \
            FROM cities INNER JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id")

    states_data = cursor.fetchall()
    [print(state) for state in states_data]

    cursor.close()
    connection.close()
