import unittest

from models.trainer import *

class TestTrainer(unittest.TestCase):
    
    def setUp(self):
        self.trainer = Trainer("Rosa Herx", "rosaherx@fit__init.com", 7733029343, "Weight loss")

    def test_can_test(self):
        self.assertEqual(True, True)

    def test_trainer_has_name(self):
        self.assertEqual("Rosa Herx", self.trainer.name)

    def test_trainer_has_email(self):
        self.assertEqual("rosaherx@fit__init.com", self.trainer.email)

    def test_trainer_has_number(self):
        self.assertEqual(7733029343, self.trainer.phone)

    def test_trainer_has_specialism(self):
        self.assertEqual("Weight loss", self.trainer.specialism)

    