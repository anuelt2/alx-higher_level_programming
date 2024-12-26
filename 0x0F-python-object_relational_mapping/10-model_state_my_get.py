#!/usr/bin/python3
"""Script that prints the State object with the name
passed as argument from a database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    search_name = argv[4]

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=search_name).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
