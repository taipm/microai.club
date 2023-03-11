# from app.models.MongoDb import db
# class Answer:
#     collection = db['answers']

#     def __init__(self, question_id, text):
#         self.question_id = question_id
#         self.text = text

#     def save(self):
#         answer_id = self.collection.insert_one({
#             'question_id': self.question_id, 
#             'text': self.text
#         }).inserted_id
#         self.id = str(answer_id)
        
#     # def save(self):
#     #     self.collection.insert_one({'question_id': self.question_id, 'text': self.text})

#     @classmethod
#     def list(cls):
#         return list(cls.collection.find())

#     @classmethod
#     def get_by_question_id(cls,question_id):
#         answers = cls.collection.find({'question_id': question_id})
#         return [Answer.from_dict(answers) for answer in answers]
    
#     @staticmethod
#     def from_dict(answer_dict):
#         answer = Answer(question_id=answer_dict['question_id'], text=answer_dict['text'])
#         answer.id = str(answer_dict['_id'])
#         return answer
from bson import ObjectId
from app.models.MongoDb import db
from flask import jsonify


class Answer:
    collection = db['answers']

    def __init__(self, question_id, text):
        self.question_id = question_id
        self.text = text

    def save(self):
        answer_id = self.collection.insert_one({
            'question_id': self.question_id,
            'text': self.text
        }).inserted_id
        self.id = str(answer_id)

    def to_dict(self):
        return {'id': self.id, 'question_id': self.question_id, 'text': self.text}

    @classmethod
    def list(cls):
        return list(cls.collection.find())

    @classmethod
    def get_by_question_id(cls, question_id):
        answers = cls.collection.find({'question_id': question_id})
        return [Answer.from_dict(answer) for answer in answers]

    def update(self):
        self.collection.update_one(
            {'_id': ObjectId(self.id)},
            {'$set': {'text': self.text}}
        )

    def delete(self):
        self.collection.delete_one({'_id': ObjectId(self.id)})

    @staticmethod
    def from_dict(answer_dict):
        answer = Answer(question_id=answer_dict['question_id'], text=answer_dict['text'])
        answer.id = str(answer_dict['_id'])
        return answer
