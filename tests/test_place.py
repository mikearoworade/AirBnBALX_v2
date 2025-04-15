import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_inheritance(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes_exist(self):
        attrs = ["city_id", "user_id", "name", "description", "number_rooms",
                 "number_bathrooms", "max_guest", "price_by_night", "latitude",
                 "longitude", "amenity_ids"]
        for attr in attrs:
            self.assertTrue(hasattr(self.place, attr))

    def test_default_values(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
