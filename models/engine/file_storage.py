#!/usr/bin/python3
"""Module file_storage

This Module contains a definition for FileStorage Class
os , importlib , re and json
"""
import os
import re
import json
import importlib
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

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

    def all(self, cls = None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dictionary = {}
            for key, value in self.__objects.items():
                if cls == value.__class__.__name__ or  cls == value.__class__:
                    new_dictionary[key] = value
            return new_dictionary
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
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def close(self):
        """call reload() method"""
        self.reload()