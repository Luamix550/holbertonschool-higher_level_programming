#!/usr/bin/python3
"""
script that prints the State object with the name
passed as argument from the database

"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]
    search = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=search).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
