#!/usr/bin/python3
"""Lists all State objects and corresponding City objects from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine to interact with the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session to execute database operations
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all State objects along with their associated City objects
    states = session.query(State).order_by(State.id).all()

    # Display State objects and their associated City objects
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    # Close the session
    session.close()

