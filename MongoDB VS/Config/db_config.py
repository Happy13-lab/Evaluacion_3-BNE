import pymongo as pm
from pymongo import MongoClient

class db_config:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["acme_salmons"]


