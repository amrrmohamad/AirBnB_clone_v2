#!/usr/bin/python3
"""Module base_model

This Module contains a definition for Amenity Class
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel


class Review(BaseModel, Base):
    """A class that represents a review

    arguments:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The comments of the review.
    """
    if models.long_storage == 'db':
        __tablename__ = 'reviews'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        user_id = ""
        place_id = ""
        text = ""

    def __init__(self, *args, **kwargs) -> str:
        """initializes Review"""
        super().__init__(*args, **kwargs)
