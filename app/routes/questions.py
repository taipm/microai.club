from flask import Blueprint, jsonify, request, render_template
from models.Answer import Answer
from models.Question import Question
from . import question_bp

@question_bp.route('/', methods=['GET'])
def list_questions():
    questions = Question.list()
    return render_template('questions.html', questions=questions)

@question_bp.route('/show/<id>', methods=['GET'])
def show(id):
    print(f'Đang gọi show với : {id}')
    question = Question.get_by_id(question_id=id)
    if not question:
        return render_template('404.html'), 404
    
    answers = Answer.get_by_question_id(question_id=id)
    print(f'{len(answers)}')
    return render_template('question_detail.html', question=question, answers=answers)

@question_bp.route('/', methods=['POST'])
def create_question():
    text = request.json.get('text', None)
    if not text:
        return jsonify({'message': 'Question text is required.'}), 400

    question = Question(text=text)
    question.save()

    return jsonify({'question': question})