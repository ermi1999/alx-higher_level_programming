#!/usr/bin/python3
"""
this script deletes all State objects with
a name containing the letter a from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instances = session.query(State).filter(State.name.like('%a%'))
    for instance in instances:
        session.delete(instance)
    session.commit()
    session.close()
