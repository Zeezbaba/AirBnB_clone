#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from datetime import datetime
import json
from models.review import Review
import os
import time
from models.engine.file_storage import FileStorage
import re
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    """Test Cases for the Review class."""

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
        """Tests instantiation of Review class."""

        dic = Review()
        self.assertEqual(str(type(dic)), "<class 'models.review.Review'>")
        self.assertIsInstance(dic, Review)
        self.assertTrue(issubclass(type(dic), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Review class."""
        attributes = storage.attributes()["Review"]
        outpt = Review()
        for key, v in attributes.items():
            self.assertTrue(hasattr(outpt, key))
            self.assertEqual(type(getattr(outpt, key, None)), v)


if __name__ == "__main__":
    unittest.main()
