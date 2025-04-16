#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

# Create SQLAlchemy declarative base
Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models with common attributes and methods"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            # Set missing attributes
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.utcnow()
            else:
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.utcnow()
            else:
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def save(self):
        """Updates updated_at with current time and saves instance to storage"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance to dict excluding SQLAlchemy internal attributes"""
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Deletes current instance from storage"""
        models.storage.delete(self)

    def __str__(self):
        """String representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"


