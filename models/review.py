#!/usr/bin/python3
"""Module base_model

This Module contains a definition for Amenity Class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class that represents a review

    arguments:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The comments of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
