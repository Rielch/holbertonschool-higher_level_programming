#!/usr/bin/python3
"""prints the state id of the specific state from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == argv[4]).first()
    if not state:
        print("Not found")
    else:
        print(state.id)
    session.close()
