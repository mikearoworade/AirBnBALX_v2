import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_inheritance(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes_exist(self):
        self.assertTrue(hasattr(self.state, "name"))

    def test_default_values(self):
        self.assertEqual(self.state.name, "")
