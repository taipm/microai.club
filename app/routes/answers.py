from flask import Blueprint, jsonify, request

from app.models.Answer import Answer
from . import answers_bp
#answers_bp = Blueprint('answers', __name__, url_prefix='/')

@answers_bp.route('/')
def list_answers():
    answers = Answer.list()
    return jsonify({'answers': answers})

@answers_bp.route('/answers/<answer_id>')
def get_answer(answer_id):
    answer = Answer.get_by_id(answer_id)
    if not answer:
        return jsonify({'message': 'Answer not found'}), 404
    return jsonify({'answer': answer.to_dict()})

@answers_bp.route('/answers', methods=['POST'])
def create_answer():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    text = data.get('text')
    if not text:
        return jsonify({'message': 'Answer text is required'}), 400

    question_id = data.get('question_id')
    if not question_id:
        return jsonify({'message': 'Question ID is required'}), 400

    answer = Answer(text=text, question_id=question_id)
    answer.save()

    return jsonify({'answer': answer.to_dict()}), 201

@answers_bp.route('/answers/<answer_id>', methods=['PUT'])
def update_answer(answer_id):
    answer = Answer.get_by_id(answer_id)
    if not answer:
        return jsonify({'message': 'Answer not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    text = data.get('text')
    if not text:
        return jsonify({'message': 'Answer text is required'}), 400

    answer.text = text
    answer.save()

    return jsonify({'answer': answer.to_dict()})
