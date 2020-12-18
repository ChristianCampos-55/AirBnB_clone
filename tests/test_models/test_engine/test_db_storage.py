#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "Doesn't apply for File Storage")
class TestDataBaseStorage(unittest.TestCase):
    """test for console"""
    def test_db(self):
        """database tests """
        pass
