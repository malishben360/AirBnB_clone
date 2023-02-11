#!/usr/bin/env python3
"""
Test BaseModel for expected functionalities
and documentation.
"""

from datetime import datetime
import time
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""
    def test_instantiation(self):
        """Test object is correctly created"""
        inst = BaseModel()
        self.assertIs(type(inst), BaseModel)
        inst.name = "ALX SE"
        inst.number = 89
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, inst.__dict__)
                self.assertIs(type(inst.__dict__[attr]), typ)
        self.assertEqual(inst.name, "ALX SE")
        self.assertEqual(inst.number, 89)

    def test_save(self):
        """Test save method update 'updated_at'"""
        inst = BaseModel()
        created_at = inst.created_at
        updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertEqual(created_at, updated_at)
        self.assertEqual(created_at, new_created_at)
        self.assertNotEqual(updated_at, new_updated_at)

    def test_uuid(self):
        """Test id is a valid uuid"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIn("id", inst.__dict__)
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[a-f0-9]{8}-[a-f0-9]{4}'
                                 '-[a-f0-9]{4}-[a-f0-9]{4}'
                                 '-[a-f0-9]{12}$')
        self.assertNotEqual(inst1.id, inst2.id)

    def test_datetime(self):
        """Test the two BaseModel datetime instances are different
        when BaseModel is instantiated, and at same time have the same value"""
        time1 = datetime.now()
        inst1 = BaseModel()
        time2 = datetime.now()
        self.assertTrue(time1 <= inst1.created_at <= time2)
        time.sleep(1e-4)
        time1 = datetime.now()
        inst2 = BaseModel()
        time2 = datetime.now()
        self.assertTrue(time1 <= inst2.updated_at <= time2)
        self.assertEqual(inst1.created_at, inst1.updated_at)
        self.assertEqual(inst2.created_at, inst2.updated_at)
        self.assertNotEqual(inst1.created_at, inst2.created_at)
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_to_dict(self):
        """Test conversion of object to dictionary for JSON seriallization"""
        inst = BaseModel()
        inst.name = "ALX School"
        inst.number = 89
        uuid = inst.id
        created_at = inst.created_at
        updated_at = inst.updated_at
        dictionary = inst.to_dict()
        expected_attrs = [
                        "id",
                        "created_at",
                        "updated_at",
                        "name",
                        "number",
                        "__class__"
                        ]
        self.assertCountEqual(dictionary.keys(), expected_attrs)
        self.assertEqual(dictionary["id"], uuid)
        self.assertEqual(dictionary["created_at"], created_at.isoformat())
        self.assertEqual(dictionary["updated_at"], updated_at.isoformat())
        self.assertEqual(dictionary["name"], "ALX School")
        self.assertEqual(dictionary["number"], 89)
        self.assertEqual(dictionary["__class__"], "BaseModel")

    def test_str(self):
        """Test str method return the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({:s}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(str(inst), string)
