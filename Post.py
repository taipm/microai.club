from bson.objectid import ObjectId
from pymongo import MongoClient
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

class MongoHandler:
    def __init__(self, uri, db_name, posts_collection, comments_collection):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.posts_collection = self.db[posts_collection]
        self.comments_collection = self.db[comments_collection]

mongo_handler = MongoHandler(
    config.get('mongodb', 'uri'),
    config.get('mongodb', 'db_name'),
    config.get('mongodb', 'posts_collection'),
    config.get('mongodb', 'comments_collection')
)

class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.comments = []

    def save(self):
        post_id = mongo_handler.posts_collection.insert_one({
            'title': self.title,
            'content': self.content,
            'comments': []
        }).inserted_id
        self.id = str(post_id)

    def add_comment(self, content):
        comment = Comment(post_id=self.id, content=content)
        comment.save()
        self.comments.append(comment.id)

    @staticmethod
    def get_by_id(post_id):
        post = mongo_handler.posts_collection.find_one({'_id': ObjectId(post_id)})
        if post:
            return Post.from_dict(post)
        else:
            return None

    @staticmethod
    def from_dict(post_dict):
        post = Post(title=post_dict['title'], content=post_dict['content'])
        post.id = str(post_dict['_id'])
        post.comments = post_dict['comments']
        return post

class Comment:
    def __init__(self, post_id, content):
        self.post_id = post_id
        self.content = content

    def save(self):
        comment_id = mongo_handler.comments_collection.insert_one({
            'post_id': self.post_id,
            'content': self.content
        }).inserted_id
        self.id = str(comment_id)

    @staticmethod
    def get_by_post_id(post_id):
        comments = mongo_handler.comments_collection.find({'post_id': post_id})
        return [Comment.from_dict(comment) for comment in comments]

    @staticmethod
    def from_dict(comment_dict):
        comment = Comment(post_id=comment_dict['post_id'], content=comment_dict['content'])
        comment.id = str(comment_dict['_id'])
        return comment
