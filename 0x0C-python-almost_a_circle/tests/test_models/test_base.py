#!/usr/bin/python3
# test_base.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines unittests for base.py."""
import unittest
import os
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """
    A class to test the Base Class
    """
    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )
