#!/usr/bin/python3
""" Place Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Integer, Float, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.review import Review
from sqlalchemy.schema import Table


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenity_ids = []

    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'), primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'), nullable=False))

    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)

    else:
        @property
        def amenities(self):
            """ getter for amenities"""
            amenity_list = []
            results = storage.all(Amenity)
            for amenity in results.values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """ amenities setter"""
            if obj and isinstance(obj, Amenity):
                type(self).amenity_ids.append(obj.id)

    @property
    def reviews(self):
        """getter reviews"""
        review_dict = {}
        objs_ = storage.all(Review)
        for key, value in objs_.items():
            if value.place_id == self.id:
                review_dict[key] = value
        return review_dict
