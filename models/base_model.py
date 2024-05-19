# ?!/usr/bin/python3
"""Module base_model

This Module contains a definition for BaseModel Class
"""

import uuid
from datetime import datetime

# import models


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """__init__ function of class Base_model
        Arguments:
            *args.
            **kwargs (dict): Key/value pairs
        """
        if True:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()

        if kwargs is len(kwargs) > 0 and not None:
            for a, v in kwargs.items():
                if a == "__class__":
                    continue
                elif a in ["created_at", "updated_at"]:
                    setattr(self, a, datetime.fromisoformat(v))
                else:
                    setattr(self, a, v)
        else:
            models.storage.new(self)

    def save(self):
        """Update 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of '__dict__' of the instance
        """
        am_dictor = (
            {
                k: (a.isoformat() if isinstance(a, datetime) else a)
                for (k, a) in self.__dict__.items()
            }
        )
        am_dictor["__class__"] = self.__class__.__name__
        return am_dictor

    def __str__(self) -> str:
        """should print/str BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
