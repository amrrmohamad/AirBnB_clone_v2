#!/usr/bin/python3
"""Creates a unique file stroga for the app"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
