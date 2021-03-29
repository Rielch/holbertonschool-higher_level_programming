#!/usr/bin/python3
"""lists the first State object from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state == session.query(State).filter(State.id == 1).first()
    if not state:
        print("Nothing")
    else:
        print('{}: {}'.format(state.id, state.name))
    session.close()
