#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    user = relationship("User",
                        backref=backref("reviews",
                                        cascade="all, delete-orphan"))
    place = relationship("Place",
                         backref=backref("reviews",
                                         cascade="all, delete-orphan"))
