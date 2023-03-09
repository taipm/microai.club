import unittest

#from app.models.Post import Post
#from app.models.Comment import Comment
#from app.models.Question import Question
#from app.models.Answer import Answer
from app.app import app
from app.models.MongoHandler import mongo_handler
#from app import app, mongo_handler, Post, Comment
import certifi
import ssl

from app.models.Question import Question
ssl._create_default_https_context = ssl._create_unverified_context

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        #mongo_handler.posts_collection.delete_many({})
        #mongo_handler.comments_collection.delete_many({})
        mongo_handler.answers_collection.delete_many({})
        mongo_handler.questions_collection.delete_many({})

    def test_save_question(self):
        response = self.app.post('/api/question', json={'question': 'What is your favorite color?'})
        self.assertEqual(response.status_code, 200)

        post = mongo_handler.questions_collection.find_one({'title': 'What is your favorite color?'})
        self.assertIsNotNone(post)
        #self.assertEqual(post['content'], '')
        #self.assertEqual(post['comments'], [])
    

    def test_save_answer(self):
        post = Question(text='What is your favorite color?')
        post.save()

        response = self.app.post('/api/answer', json={'question_id': post.id, 'answer': 'My favorite color is blue.'})
        self.assertEqual(response.status_code, 200)

        comment = mongo_handler.answers_collection.find_one({'question_id': post.id})
        self.assertIsNotNone(comment)
        self.assertEqual(comment['content'], 'My favorite color is blue.')

if __name__ == '__main__':
    unittest.main()
