import os
from pymongo import MongoClient
import certifi
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#config = Config()
print(f'Database name: ')
MONGODB_URI = os.environ.get('uri')
DATABASE_NAME = os.environ.get('database') #'micro_ai'
print(f'Database name: {str(DATABASE_NAME)}')
client = MongoClient(MONGODB_URI,tlsCAFile=certifi.where())
db = client[DATABASE_NAME]
#db = client[config.get('mongodb', 'database')]