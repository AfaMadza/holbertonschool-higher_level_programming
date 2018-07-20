#!/usr/bin/python3
"""
This module contains a script that lists all states
starting with N from a specific database
"""
import sys
import MySQLdb


def connect_db():
    """
    Connects to a database with given parameters
    """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3])
    return db


def display_states(db):
    """
    Selects and prints states from a database
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name REGEXP '^N' "
                "ORDER BY states.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    display_states(connect_db())
