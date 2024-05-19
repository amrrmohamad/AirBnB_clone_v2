#!/usr/bin/python3
"""Module base_model

This Module contains definitions for Places Class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """A class that represents a place

    Attributes:
        non.
    """

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
