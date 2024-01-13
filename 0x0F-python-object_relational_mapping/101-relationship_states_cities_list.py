#!/usr/bin/python3
"""
this script creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    joined_query = session.query(State, City).join(City)
    results = joined_query.all()
    name = ""
    for state, city in results:
        if state.name != name:
            print("{}: {}".format(state.id, state.name))
            name = state.name
        print('\t' + "{}: {}".format(city.id, city.name))
    session.close()
