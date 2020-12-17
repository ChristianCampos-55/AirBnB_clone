#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models import storage
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey


class State(BaseModel, Base):
    """ State class """   
    __tablename__ = "states"
    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref="my_state")

    if os.environ.get('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """cities getter"""
            list_cities = []
            dictionary = storage.all(City)
            if dictionary:
                for k, v  in dictionary.items():
                    if self.id == v.state_id:
                        list_cities.append(v)
            return list_cities
