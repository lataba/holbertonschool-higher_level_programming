#!/usr/bin/python3
""""
Takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":

    connection = MySQLdb.connect(
                    user=sys.argv[1],
                    password=sys.argv[2],
                    db=sys.argv[3])
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE '{}' ORDER BY states.id ASC;".
        format(sys.argv[4]))

    states_data = cursor.fetchall()
    [print(state) for state in states_data]

    cursor.close()
    connection.close()
