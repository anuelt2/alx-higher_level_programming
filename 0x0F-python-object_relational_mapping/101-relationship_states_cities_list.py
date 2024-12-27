#!/usr/bin/python3
"""
Script that lists all State objects and corresponding
City objects contained in a database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
            pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda city: city.id):
            print(f"\t{city.id}: {city.name}")
    session.close()
