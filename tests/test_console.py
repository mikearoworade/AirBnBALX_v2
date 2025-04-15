import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import sys
import os


class TestConsole(unittest.TestCase):

    def test_help_show(self):
        """Test help command for 'show'"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertIn("Prints the string representation of an instance", f.getvalue())

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            self.assertTrue(len(user_id) > 0)

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            self.assertIn(user_id, f.getvalue())

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {user_id}")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            self.assertIn("no instance found", f.getvalue().lower())

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertIn("User", f.getvalue())

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd(f'update User {user_id} first_name "Michael"')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            self.assertIn("Michael", f.getvalue())

    def test_dot_all(self):
        """Test User.all() style command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            self.assertIn("User", f.getvalue())

    def test_dot_count(self):
        """Test User.count()"""
        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            count = int(f.getvalue().strip())
            self.assertGreaterEqual(count, 1)

    def test_dot_update_with_dict(self):
        """Test User.update(<id>, <dictionary>)"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd(f'User.update("{user_id}", {{"first_name": "Mike", "email": "mike@hbnb.com"}})')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue()
            self.assertIn("Mike", output)
            self.assertIn("mike@hbnb.com", output)

    def test_create_with_params(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd('create Place name="Cozy_home" number_rooms=2 price_by_night=99.99')
            created_id = fake_out.getvalue().strip()
            self.assertIn(created_id, storage.all().keys())

            # Verify attributes were set
            from models.place import Place
            obj = storage.all()["Place." + created_id]
            self.assertEqual(obj.name, "Cozy home")
            self.assertEqual(obj.number_rooms, 2)
            self.assertAlmostEqual(obj.price_by_night, 99.99)

    def test_invalid_param_is_skipped(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd('create State name="California" invalidparam==oops')
            created_id = fake_out.getvalue().strip()
            from models.state import State
            obj = storage.all()["State." + created_id]
            self.assertEqual(obj.name, "California")
            self.assertFalse(hasattr(obj, 'invalidparam'))


if __name__ == "__main__":
    unittest.main()