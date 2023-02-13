#!/usr/bin/env python3
"""
Module for base model instance serialization
andcdeserialization.
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instance to JSON file and
    deserializes JSON file to instance"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj=None):
        """sets in __objects the obj"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        jsn_objs = {}
        for key in self.__objects.keys():
            jsn_objs[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(jsn_objs, file)

    def reload(self):
        """deserializes the JSON file to __objects
        only if the JSON file exists"""
        try:
            with open(self.__file_path, "r") as file:
                objects = json.load(file)
                for key in objects.keys():
                    self.__objects[key] = BaseModel(**objects[key])
        except FileNotFoundError:
            pass