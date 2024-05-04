#!/usr/bin/python3
"""Script to fetch the id of a State object by name"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()

