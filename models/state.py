#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from models.city import City
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class within the model"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """ getter method for cities"""
        from models import storage
        cities_list = []
        dictionary = storage.all(City)
        if dictionary:
            for k, v in dictionary.items():
                if self.id == v.state_id:
                    cities_list.append(v)
        return cities_list
