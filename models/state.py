#!/usr/bin/python3
"""State Module for HBNB project"""
from os import getenv
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Ret City(es) which state_id equals State.id """
            cit_list = []
            for k, j in models.storage.all().items():
                if j.__class__.__name__ == 'City':
                    if j.state_id == self.id:
                        cit_list.append(j)
            return cit_list

    else:
        cities = relationship("City", cascade="all, delete, delete-orphan",
                              backref="state")
