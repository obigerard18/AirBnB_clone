#!/usr/bin/python3
"""
Contains the TestCityDocs classes
"""

from datetime import datetime
import inspect
import models
from models import city
from models.base_model import BaseModel
import pep8
import unittest
City = city.City


class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_f = inspect.getmembers(City, inspect.isfunction)
