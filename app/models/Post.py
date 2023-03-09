from bson.objectid import ObjectId
from app.models.Comment import Comment
from app.models.MongoHandler import mongo_handler

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



# Tạo một đối tượng Post và lưu vào cơ sở dữ liệu
# post = Post(title='Test Post', content='This is a test post')
# post.save()

# # Thêm một comment vào post
# post.add_comment(content='This is a test comment')

# # Lấy một post theo id và in ra title và tất cả các comments của nó
# post_id = post.id
# post = Post.get_by_id(post_id)
# print('Title:', post.title)
# print('Comments:')
# for comment in post.comments:
#     print(comment.content)

