#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa

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

    state_Obj = session.query(State).order_by(State.id).first()
    if state_Obj:
        print("{}: {}".format(state_Obj.id, state_Obj.name))
    else:
        print("Nothing")

    session.close()
