#!/usr/bin/python3
"""Initializes the storage engine"""

from os import getenv

# Use DBStorage if env variable is set to 'db', else use FileStorage
if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Load existing data (or create tables in case of DBStorage)
storage.reload()
