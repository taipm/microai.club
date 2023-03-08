from pymongo import MongoClient
from bson.objectid import ObjectId

class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.comments = []

    def save(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['blog_database']
        posts_collection = db['posts']
        post_id = posts_collection.insert_one({
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
        client = MongoClient('mongodb://localhost:27017/')
        db = client['blog_database']
        posts_collection = db['posts']
        post = posts_collection.find_one({'_id': ObjectId(post_id)})
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
        client = MongoClient('mongodb://localhost:27017/')
        db = client['blog_database']
        comments_collection = db['comments']
        comment_id = comments_collection.insert_one({
            'post_id': self.post_id,
            'content': self.content
        }).inserted_id
        self.id = str(comment_id)

    @staticmethod
    def get_by_post_id(post_id):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['blog_database']
        comments_collection = db['comments']
        comments = []
        for comment_dict in comments_collection.find({'post_id': post_id}):
            comment = Comment.from_dict(comment_dict)
            comments.append(comment)
        return comments

    @staticmethod
    def from_dict(comment_dict):
        comment = Comment(post_id=str(comment_dict['post_id']), content=comment_dict['content'])
        comment.id = str(comment_dict['_id'])
        return comment
