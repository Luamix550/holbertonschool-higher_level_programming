#!/usr/bin/python3
"""
script that lists all State objects that contain the letter (a)
from the database hbtn_0e_6_usa

"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_a = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    for state in states_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
