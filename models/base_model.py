#!/usr/bin/python3
"""
Contains class BaseModel
"""

import models
from datetime import datetime
import uuid
isof = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], isof)
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], isof)
            else:
                self.update_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance
        """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        if "__dict__" in new_dict:
            del new_dict["__dict__"]
        if "__weakref__" in new_dict:
            del new_dict["__weakref__"]
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """String representation of the BaseModel class."""
        new_str = "[{:s}] ({:s}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__
                )
        return new_str
