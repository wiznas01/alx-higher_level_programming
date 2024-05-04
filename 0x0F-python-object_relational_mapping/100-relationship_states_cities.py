#!/usr/bin/python3
"""Script to create the State "California" with the City "San Francisco" from the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cali_state = State(name="California")
    sf_city = City(name="San Francisco", state=cali_state)

    session.add(cali_state)
    session.add(sf_city)
    session.commit()

    print(cali_state.id)
    print(sf_city.id)

    session.close()

