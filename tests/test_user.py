import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_inheritance(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes_exist(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attributes_default(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
