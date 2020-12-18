#!/usr/bin/python3
"""module for amenities"""
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """ class for amenities """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    place_amenities = relationship('Place', secondary="place_amenity",
                                   backref='amenities', viewonly=False)
