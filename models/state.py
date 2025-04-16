#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class for HBNB project """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete, delete-orphan"
        )
    else:
        @property
        def cities(self):
            """Returns the list of City instances with state_id == State.id"""
            from models import storage
            from models.city import City
            # return [city for city in storage.all(City).values() if city.state_id == self.id]
            city_list = []
            all_cities = storage.all(City).values()
            for city in all_cities:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
