#!/usr/bin/python3
"""Creates a unique file stroga for the app"""

from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


long_storage = getenv("HBNB_TYPE_STORAGE")

if long_storage == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()