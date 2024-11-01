from pymongo import MongoClient
from typing import Any

DB_URI = "mongodb+srv://dedstinguerdsds:ceam12345@cluster0.njoajat.mongodb.net/patients-db"
database: Any = MongoClient(DB_URI)
conn: Any = database['patients-db']
