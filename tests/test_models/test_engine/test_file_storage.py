#!/usr/bin/env python3
"""
Tests the file storage module classes, methods and docstrings
"""
import unittest
import inspect
import pycodestyle
import json
from models.engine import file_storage
from models import base_model
FileStorage = file_storage.FileStorage
BaseModel = base_model.BaseModel


class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py requires docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py requires docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage class requires docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "FileStorage class requires docstring")

    def test_fs_func_docstrings(self):
        """Test for docstrings in FileStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method requires docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method requires docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    def test_new(self):
        """Test new method adds an object to __objects"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        test_dict = {}
        instance = BaseModel()
        instance.name = "ALX School"
        instance.age = 31
        inst_key = instance.__class__.__name__ + "." + instance.id
        storage.new(instance)
        test_dict[inst_key] = instance
        self.assertIn(inst_key, FileStorage._FileStorage__objects)
        self.assertEqual(test_dict[inst_key],
                         FileStorage._FileStorage__objects[inst_key])
        FileStorage._FileStorage__objects = save

    def test_save(self):
        """Test __objects is serialized and saved in file.json"""
        storage = FileStorage()
        new_dict = {}
        instance = BaseModel()
        key = instance.__class__.__name__ + '.' + instance.id
        new_dict[key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        file_temp = json.dumps(new_dict)
        with open("file.json", "r") as json_file:
            js = json_file.read()
        self.assertEqual(json.loads(file_temp), json.loads(js))

    def test_all(self):
        """Test __objects is returned"""
        storage = FileStorage()
        objects = storage.all()
        self.assertEqual(type(objects), dict)
        self.assertIs(storage._FileStorage__objects, objects)
