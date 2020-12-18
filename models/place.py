#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, Float, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.schema import Table

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """Place for  MySQL database."""
    __tablename__ = "places"

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
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    @property
    def amenities(self):
        """ getter method for amenities"""
        amenities_list = []
        from models import storage
        dictionary = storage.all(Amenity)
        if dictionary:
            for k, v in dictionary.items():
                if self.id == v.place_id:
                    amenities_list.append(v)
        return amenities_list

    @amenities.setter
    def amenities(self, value):
        """setter method for amenities"""
        if type(value) != Amenity:
            return
        self.amenity_ids.append(value)

    @property
    def reviews(self):
        """ getter method for reviews"""
        reviews_list = []
        from models import storage
        dictionary = storage.all(Review)
        if dictionary:
            for k, v in dictionary.items():
                if self.id == v.place_id:
                    reviews_list.append(v)
        return reviews_list
