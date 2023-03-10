from configparser import ConfigParser

class ConfigParser:
    def __init__(self):
        self.config = ConfigParser()
        #self.config.read('config.ini')
        self.config.read('/Users/taipm/Documents/GitHub/microai.club/config.ini')

    def get(self, section, key):
        return self.config.get(section, key)

# import os

# class Config(object):
#     DEBUG = False
#     TESTING = False
#     CSRF_ENABLED = True
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
#     MONGODB_URI = os.environ.get('MONGODB_URI') or 'mongodb://localhost:27017/microai'
#     MONGODB_NAME = os.environ.get('MONGODB_NAME') or 'microai'
#     OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or 'my-openai-api-key'

# class ProductionConfig(Config):
#     DEBUG = False

# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True

# class DevelopmentConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True

# class TestingConfig(Config):
#     TESTING = True
