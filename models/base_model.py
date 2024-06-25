# ?!/usr/bin/python3
"""Module base_model

This Module contains a definition for BaseModel Class
"""

import models
import uuid
from datetime import datetime
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


time = "%Y-%m-%dT%H:%M:%S.%f"
if models.long_storage == "db":
    Base = declarative_base()
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
else:
    Base = object


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """__init__ function of class Base_model
        Arguments:
            *args.
            **kwargs (dict): k/v pairs
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def save(self):
        """Update 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()
        models.storage.new(self)

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of '__dict__' of the instance
        """
        dict_new = self.__dict__.copy()
        if "created_at" in dict_new:
            dict_new["created_at"] = dict_new["created_at"].strftime(time)
        if "updated_at" in dict_new:
            dict_new["updated_at"] = dict_new["updated_at"].strftime(time)
        dict_new["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in dict_new:
            del dict_new["_sa_instance_state"]
        return dict_new

    def __str__(self) -> str:
        """should print/str BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
