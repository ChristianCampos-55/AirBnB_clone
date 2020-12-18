#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")

    elif os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Cities getter to find object """
            city = []
            for obj in list(models.storage.all(City).values()):
                if obj.state_id == self.id:
                    city.append(obj)
            return city
