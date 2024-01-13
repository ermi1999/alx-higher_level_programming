#!/usr/bin/python3
"""
This program prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    joined_query = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id)
    for query in joined_query:
        print("{}: ({}) {}".format(query[0], query[1], query[2]))
