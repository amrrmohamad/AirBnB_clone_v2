#!/usr/bin/python3
"""Module base_model

This Module contains a definition for class
"""
import models
import sqlalchemy
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Amenity(BaseModel, Base):
    """A class that represents a amenity
    Attributes:
        name (str): the name of the class
    """

    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity
        attributes:
            self: var
            args: type of list
            kwargs: type of dictionary
            """
        super().__init__(*args, **kwargs)
