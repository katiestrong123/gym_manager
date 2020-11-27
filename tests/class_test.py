import unittest
from models.class import *

class TestClass(unittest.TestClass):
    
    def setUp(self):
        self.class = Class("Cycho Spin Class", "HIIT", 60)

    def test_can_test(self):
        self.assertEqual(True, True)
