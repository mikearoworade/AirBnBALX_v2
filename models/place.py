#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

# Association table for Many-To-Many between Place and Amenity
place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """Represents a Place for a MySQL database."""
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # Relationship
    user = relationship('User', back_populates='places')
    cities = relationship('City', back_populates='places')

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False,
                                 backref="place_amenities")
    else:
        amenity_ids = []

        @property
        def reviews(self):
            """Returns the list of Review instances linked to the Place (for FileStorage)."""
            from models import storage
            from models.review import Review
            return [review for review in storage.all(Review).values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Returns the list of Amenity instances linked to the Place (for FileStorage)."""
            from models import storage
            from models.amenity import Amenity
            return [amenity for amenity in storage.all(Amenity).values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Adds an Amenity ID to amenity_ids list if obj is of type Amenity."""
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
