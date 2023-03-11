# import os
# from pymongo import MongoClient
# import certifi
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context

# #config = Config()
# print(f'Database name: ')
# MONGODB_URI = os.environ.get('uri')
# DATABASE_NAME = os.environ.get('database') #'micro_ai'
# print(f'Database name: {str(DATABASE_NAME)}')
# client = MongoClient(MONGODB_URI,tlsCAFile=certifi.where())
# db = client[DATABASE_NAME]
# #db = client[config.get('mongodb', 'database')]


import os
from pymongo import MongoClient
import certifi
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class Config:
    def __init__(self):
        from configparser import ConfigParser
        config = ConfigParser()
        config.read('config.ini')
        self.config = config

    def get(self, section, key):
        return self.config.get(section, key)


def get_database_uri():
    return os.environ.get('MONGODB_URI', 'mongodb+srv://taipm:OAMOHMEC8CPUHoz2@cluster0.nskndlz.mongodb.net/?retryWrites=true&w=majority')


def get_database_name():
    return os.environ.get('DATABASE_NAME', 'micro_ai')


def get_mongo_client():
    uri = get_database_uri()
    client = MongoClient(uri, tlsCAFile=certifi.where())
    return client


def get_database():
    client = get_mongo_client()
    db_name = get_database_name()
    db = client[db_name]
    return db

db = get_database()