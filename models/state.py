#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from models.base_model import BaseModel, Base
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class from the db"""
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """ getter method for cities"""
        cities_list = []
        dictionary = storage.all(City)
        if dictionary:
            for k, v in dictionary.items():
                if self.id == v.state_id:
                    cities_list.append(v)
        return cities_list
