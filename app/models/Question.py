# from datetime import datetime
# from app.models import db

# # class Question:
# #     collection = db['questions']

# #     def __init__(self, text, answer=None):
# #         self.text = text
# #         self.answer = answer
# #         self.timestamp = datetime.utcnow()

# #     def save(self):
# #         if self.id:
# #             self.collection.update_one({'_id': self.id}, {'$set': {'text': self.text, 'answer': self.answer}})
# #         else:
# #             self.id = self.collection.insert_one({'text': self.text, 'answer': self.answer, 'timestamp': self.timestamp}).inserted_id


from bson.objectid import ObjectId
from .Answer import Answer
from .MongoDb import db

class Question:
    collection = db['questions']
    def __init__(self, text):        
        self.text = text
        self.answers = []

    def save(self):
        question_id = self.collection.insert_one({
            'text': self.text,
            'answers': []
        }).inserted_id
        self.id = str(question_id)

    def add_answer(self, text):
        answer = Answer(question_id=self.id, text=text)
        answer.save()
        self.answers.append(answer.id)
    
    @classmethod
    def list(cls):
        return list(cls.collection.find())
    
    @classmethod
    def get_by_id(cls, question_id):
        question = cls.collection.find_one({'_id': ObjectId(question_id)})
        if question:            
            return Question.from_dict(question)
        else:
            return None
        
    @staticmethod
    def from_dict(question_dict):
        question = Question(text=question_dict['text'])
        question.id = str(question_dict['_id'])
        question.answers = question_dict['answers']
        return question
