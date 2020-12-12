#!/usr/bin/python3
"""Define City class."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class City(Base):
    """Define City class."""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
