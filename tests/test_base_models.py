import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import os
import models
import time

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_id_is_unique(self):
        another_model = BaseModel()
        self.assertNotEqual(self.model.id, another_model.id)

    def test_created_at_type(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected)

    def test_save_updates_updated_at(self):
        old_updated = self.model.updated_at
        time.sleep(0.01)  # sleep for 10ms
        self.model.save()
        self.assertNotEqual(old_updated, self.model.updated_at)

    def test_to_dict_contains_class(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_to_dict_datetime_format(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())

    def test_init_with_kwargs(self):
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)

    def test_init_with_kwargs_ignores_class(self):
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertNotIn("__class__", new_model.__dict__)

if __name__ == '__main__':
    unittest.main()