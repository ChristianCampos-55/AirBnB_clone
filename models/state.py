#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models import storage
from models.city import City
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    #cities = relationship("City", cascade="all, delete", backref="my_state")

    @property
    def cities(self):
        """getter for cities object"""
        my_list = []
        my_cities = storage.all(City)
        for key, value in my_cities.items():
            if value.state_id == self.id:
                my_list.append(value)
        return my_list
