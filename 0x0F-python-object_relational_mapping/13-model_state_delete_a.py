#!/usr/bin/python3
"""deletes the State objects that contain 'a' from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states_delete = session.query(State).filter(State.name.like('%a%'))
    for state in state_delete:
        session.delete(state)
    session.commit()
    session.close()
