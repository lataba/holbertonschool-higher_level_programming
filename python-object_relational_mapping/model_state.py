#!/usr/bin/python3
"""
Defines a State model that inherits from SQLAlchemy Base
and links to the MySQL table states.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
