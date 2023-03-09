from app.models.Answer import Answer
from app.models.MongoHandler import mongo_handler

from bson.objectid import ObjectId

class Question:
    def __init__(self, text):
        self.text = text
        self.answers = []

    def save(self):
        question_id = mongo_handler.questions_collection.insert_one({
            'text': self.text,
            'answers': []
        }).inserted_id
        self.id = str(question_id)

    def add_answer(self, text):
        answer = Answer(question_id=self.id, text=text)
        answer.save()
        self.answers.append(answer.id)

    @staticmethod
    def list():
        questions = mongo_handler.questions_collection.find()
        return [Question.from_dict(q) for q in questions]
    
    @staticmethod
    def get_by_id(question_id):
        question = mongo_handler.questions_collection.find_one({'_id': ObjectId(question_id)})
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
