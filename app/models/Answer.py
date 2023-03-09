from models.MongoHandler import mongo_handler
from bson.objectid import ObjectId

class Answer:
    def __init__(self, question_id, text):
        self.question_id = question_id
        self.text = text

    def save(self):
        answer_id = mongo_handler.answers_collection.insert_one({
            'question_id': self.question_id,
            'text': self.text
        }).inserted_id
        self.id = str(answer_id)

    @staticmethod
    def get_by_question_id(question_id):
        answers = mongo_handler.answers_collection.find({'question_id': question_id})
        return [Answer.from_dict(answer) for answer in answers]

    @staticmethod
    def from_dict(answer_dict):
        answer = Answer(question_id=answer_dict['question_id'], text=answer_dict['text'])
        answer.id = str(answer_dict['_id'])
        return answer
