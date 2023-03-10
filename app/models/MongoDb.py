from configparser import ConfigParser
from pymongo import MongoClient
import certifi
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

config = ConfigParser()
config.read('/Users/taipm/Documents/GitHub/microai.club/config.ini')

client = MongoClient(config.get('mongodb', 'uri'),tlsCAFile=certifi.where())
db = client[config.get('mongodb', 'database')]