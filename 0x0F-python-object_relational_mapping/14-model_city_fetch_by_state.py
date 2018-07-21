#!/usr/bin/python3
"""
This module contains a script that deletes all states with
aan 'a' in the name from a database
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    join_query = session.query(State, City).join(City).order_by(City.id)
    for State, City in join_query:
        print("{}: ({}) {}".format(State.name, City.id, City.name))
    session.close()
