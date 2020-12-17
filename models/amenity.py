#!/usr/bin/python3
"""module for amenities"""
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, Float, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.review import Review
from sqlalchemy.schema import Table


class Amenity(BaseModel, Base):
    '''Class that modifies amenities'''
    name = ""
