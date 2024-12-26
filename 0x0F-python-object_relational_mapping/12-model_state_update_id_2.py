#!/usr/bin/python3
"""Script that changes the name of a State object from a database"""
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

    update_state = session.query(State).filter_by(id=2).first()
    if update_state:
        update_state.name = "New Mexico"
        session.commit()
