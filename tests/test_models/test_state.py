#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from datetime import datetime
import json
from models.state import State
import os
import time
from models.engine.file_storage import FileStorage
import re
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """Test Cases for the State class."""

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
        """Tests instantiation of State class."""

        outpt = State()
        self.assertEqual(str(type(outpt)), "<class 'models.state.State'>")
        self.assertIsInstance(outpt, State)
        self.assertTrue(issubclass(type(outpt), BaseModel))

    def test_attributes(self):
        """Tests the attributes of State class."""
        attributes = storage.attributes()["State"]
        o = State()
        for key, v in attributes.items():
            self.assertTrue(hasattr(o, key))
            self.assertEqual(type(getattr(o, key, None)), v)


if __name__ == "__main__":
    unittest.main()
