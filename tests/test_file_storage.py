import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.test_model = BaseModel()
        self.test_key = f"BaseModel.{self.test_model.id}"
        self.storage._FileStorage__objects.clear()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_returns_dict(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        self.storage.new(self.test_model)
        self.assertIn(self.test_key, self.storage.all())

    def test_save_creates_file(self):
        self.storage.new(self.test_model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_loads_data(self):
        self.storage.new(self.test_model)
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        self.assertIn(self.test_key, self.storage.all())

    def test_reload_without_file(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        self.storage.reload()  # Should not raise any error

    def test_save_file_content(self):
        self.storage.new(self.test_model)
        self.storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertIn(self.test_key, data)

if __name__ == '__main__':
    unittest.main()