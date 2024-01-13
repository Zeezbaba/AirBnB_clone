#!/usr/bin/python3
"""Test module for the Amenity Class."""

import unittest
from datetime import datetime
import re
from models.amenity import Amenity
import time
import os
from models.engine.file_storage import FileStorage
import json
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resetting Stored data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Amenity class."""

        inst = Amenity()
        self.assertEqual(str(type(inst)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(inst, Amenity)
        self.assertTrue(issubclass(type(inst), BaseModel))

    def test_8_attributes(self):
        """attributes of Amenity class testing."""
        attributes = storage.attributes()["Amenity"]
        attr = Amenity()
        for key, obj in attributes.items():
            self.assertTrue(hasattr(attr, key))
            self.assertEqual(type(getattr(attr, key, None)), obj)


if __name__ == "__main__":
    unittest.main()
