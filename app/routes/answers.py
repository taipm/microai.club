# from configparser import ConfigParser
# import os
from flask import Blueprint, jsonify, request
# from . import config
from app.ai.MicroAI import MicroAI
from app.models.Answer import Answer
from app.models.MongoDb import get_openai_key
from app.models.Question import Question
from . import answers_bp

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


@answers_bp.route('/microai_answer', methods=['POST'])
def microai_answer():
    question_id = request.form.get('question_id')
    question = Question.get_by_id(question_id)
    if not question:
        return jsonify({'success': False, 'message': 'Question not found'}), 404
    open_ai_key = get_openai_key()
    print(f'OpenAI: {open_ai_key}')
    text = MicroAI(api_key=open_ai_key).generate_answer(question.text)
    print(f'Micro-AI: {text}')
    answer = question.add_answer(text)
    return jsonify({'answer': text['answer']})
    #return jsonify({'answer': answer.to_dict()})
