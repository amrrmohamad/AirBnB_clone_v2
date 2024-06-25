#!/usr/bin/python3
"""Module base_model
    with database
This Module for City Class
"""
import models
from models.base_model import BaseMode, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """A class that represents a city

    arguments:
        name (str): name of the city
        state_id (str): the state id
    """

    if models.long_storage == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
