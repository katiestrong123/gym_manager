import unittest

from models.exercise_class import *

class TestExerciseClass(unittest.TestCase):
    def setUp(self):
        self.exercise_class = ExerciseClass("Cycho Spin Class", "HIIT", 60, "2020-12-3")

    def test_can_test(self):
        self.assertEqual(True, True)

    def test_class_has_name(self):
        self.assertEqual("Cycho Spin Class", self.exercise_class.name)
   
    def test_class_has_type(self):
        self.assertEqual("HIIT", self.exercise_class.type)

    def test_class_has_duration(self):
        self.assertEqual(60, self.exercise_class.duration)