#!/usr/bin/python3
"""
This module contains a script that  lists all State
objects containing the letter 'a' in a databse
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    a_states = session.query(State).filter(State.name.like('%a%'))
    for a_state in a_states:
        print("{}: {}".format(a_state.id, a_state.name))
    session.close()
