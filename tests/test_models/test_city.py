#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

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
        """Tests instantiation of City class."""

        inpt = City()
        self.assertEqual(str(type(inpt)), "<class 'models.city.City'>")
        self.assertIsInstance(inpt, City)
        self.assertTrue(issubclass(type(inpt), BaseModel))

    def test_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        inpt = City()
        for key, v in attributes.items():
            self.assertTrue(hasattr(inpt, key))
            self.assertEqual(type(getattr(inpt, key, None)), v)


if __name__ == "__main__":
    unittest.main()
