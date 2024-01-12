#!/usr/bin/python3
"""
this program prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).limit(1)
    if instance:
        print("{}: {}".format(instance[0].id, instance[0].name))
    else:
        print()
    session.close()
