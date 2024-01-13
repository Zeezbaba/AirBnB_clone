#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import json
from models.user import User
import re
import os
from models.engine.file_storage import FileStorage
import time
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """Test Cases for the User class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of User class."""

        outpt = User()
        self.assertEqual(str(type(outpt)), "<class 'models.user.User'>")
        self.assertIsInstance(outpt, User)
        self.assertTrue(issubclass(type(outpt), BaseModel))

    def test_attributes(self):
        """Tests the attributes of User class."""
        attributes = storage.attributes()["User"]
        o = User()
        for key, v in attributes.items():
            self.assertTrue(hasattr(o, key))
            self.assertEqual(type(getattr(o, key, None)), v)


if __name__ == "__main__":
    unittest.main()
