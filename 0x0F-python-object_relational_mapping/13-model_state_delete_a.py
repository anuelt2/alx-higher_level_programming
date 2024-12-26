#!/usr/bin/python3
"""
Script that deletes all State objects with name
containing letter `a` from a database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.ilike("%a%")).delete()
    session.commit()
