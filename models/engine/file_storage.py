#!/usr/bin/python3
"""Module file_storage

This Module contains a definition for FileStorage Class
os , importlib , re and json
"""

import os
import importlib
import re
import json


class FileStorage:
    """FileStorage Class.
    Attributes:
        __file_path (str): string - JSON file
        __objects (dict): A dictionary of objects.
    """

    __objects = {}
    __file_path = "file.json"

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(self.__file_path, "w") as f:
            json.dump({k: a.to_dict() for k, a in self.__objects.items()}, f)

    def get_class(self, name):
        """ returns a class from models"""
        am_models = re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()
        module = importlib.import_module(f"models.{am_models}")
        return getattr(module, name)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if (os.path.isfile(self.__file_path)):
            if (os.path.getsize(self.__file_path) > 0):
                with open(self.__file_path, "r") as f:
                    self.__objects = {
                      k: self.get_class(k.split(".")[0])(**a)
                      for k, a in json.load(f).items()
                    }
