# from configparser import ConfigParser
# from pymongo import MongoClient
# import certifi
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# class MongoHandler:
#     def __init__(self, uri, db_name, 
#                  posts_collection, 
#                  comments_collection,
#                  questions_collection,
#                  answers_collection):
#         self.client = MongoClient(uri,tlsCAFile=certifi.where())
#         self.db = self.client[db_name]
#         self.posts_collection = self.db[posts_collection]
#         self.comments_collection = self.db[comments_collection]
#         self.questions_collection = self.db[questions_collection]
#         self.answers_collection = self.db[answers_collection]

#     def get_latest_record(self, collection_name):
#         latest_record = self.db[collection_name].find_one({}, sort=[('_id', -1)])
#         return latest_record

# config = ConfigParser()
# config.read('/Users/taipm/Documents/GitHub/microai.club/config.ini')

# mongo_handler = MongoHandler(
#     config.get('mongodb', 'uri'),
#     config.get('mongodb', 'database'),
#     config.get('mongodb', 'posts'),
#     config.get('mongodb', 'comments'),
#     config.get('mongodb', 'questions'),
#     config.get('mongodb', 'answers')
# )
