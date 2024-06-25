#!/usr/bin/python3
"""Module base_model

This Module contains definitions for Places Class
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review


class Place(BaseModel, Base):
    """A class that represents a place

    Attributes:
        non.
    """
    if models.long_storage == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        description = Column(String(1024), nullable=True)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        price_by_night = Column(Integer, nullable=False, default=0)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities", viewonly=False)
    elif models.long_storage != 'db':
        @property
        def reviews(self):
            """getter attribute returns the list of Review instances"""
            from models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
    else:
        number_rooms = 0
        city_id = ""
        description = ""
        name = ""
        number_bathrooms = 0
        user_id = ""
        latitude = 0.0
        price_by_night = 0
        max_guest = 0
        amenity_ids = []
        longitude = 0.0

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
