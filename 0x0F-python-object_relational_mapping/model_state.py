#!/usr/bin/python3
"""Module that defines State class"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """A class definition of a State"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
