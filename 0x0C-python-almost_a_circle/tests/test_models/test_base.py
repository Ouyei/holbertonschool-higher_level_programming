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
	def test_id(self):
		b1 = Base(89)
		self.assertEqual(b1.id, 89)
