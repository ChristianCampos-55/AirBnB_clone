#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from models.city import City
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey


class State(BaseModel, Base):
    """ State class """
    
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

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
