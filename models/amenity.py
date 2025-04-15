#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database."""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        # place_amenities backref is declared in Place
        pass
