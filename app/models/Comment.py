
# from app.models.MongoHandler import mongo_handler


# class Comment:
#     def __init__(self, post_id, content):
#         self.post_id = post_id
#         self.content = content

#     def save(self):
#         comment_id = mongo_handler.comments_collection.insert_one({
#             'post_id': self.post_id,
#             'content': self.content
#         }).inserted_id
#         self.id = str(comment_id)

#     @staticmethod
#     def get_by_post_id(post_id):
#         comments = mongo_handler.comments_collection.find({'post_id': post_id})
#         return [Comment.from_dict(comment) for comment in comments]

#     @staticmethod
#     def from_dict(comment_dict):
#         comment = Comment(post_id=comment_dict['post_id'], content=comment_dict['content'])
#         comment.id = str(comment_dict['_id'])
#         return comment