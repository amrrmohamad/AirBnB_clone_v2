#!/usr/bin/python3
"""Module base_model

This Module contains a definition for User Class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class that represents a user.

    Attributes:
        email (str): The email of the users.
        first_name (str): The first name of the users.
        last_name (str): The last name of the users.
        password (str): The password of the userss.
    """
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    email = ""
    first_name = ""
    last_name = ""
    password = ""
