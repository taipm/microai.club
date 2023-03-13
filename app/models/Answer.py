import datetime
from bson import ObjectId
import pymongo
from app.models.MongoDb import db
from flask import jsonify


class Answer:
    collection = db['answers']

    def __init__(self, question_id, text):
        self.question_id = question_id
        self.text = text
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        answer_id = self.collection.insert_one({
            'question_id': self.question_id,
            'text': self.text,
            'created_at':self.created_at
        }).inserted_id
        self.id = str(answer_id)

    def to_dict(self):
        return {'id': self.id, 'question_id': self.question_id, 'text': self.text,'created_at':self.created_at}

    @classmethod
    def list(cls):
        #return list(cls.collection.find())
        return list(cls.collection.find().sort('created_at', pymongo.DESCENDING))

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
        answer = Answer(question_id=answer_dict['question_id'], text = answer_dict['text'])
        answer.id = str(answer_dict['_id'])
        return answer
