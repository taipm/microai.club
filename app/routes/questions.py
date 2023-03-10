from flask import Blueprint, jsonify, request, render_template
from app.models.Answer import Answer
from app.models.Question import Question
from . import question_bp
#question_bp = Blueprint('questions', __name__)
#question_bp = Blueprint('questions', __name__, url_prefix='/questions')

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


# @questions_bp.route('/<int:id>', methods=['GET'])
# def get_question(id):
#     question = Question.get_by_id(id)
#     if not question:
#         return jsonify({'message': 'Question not found.'}), 404

#     return jsonify({'question': question})


# @questions_bp.route('/<int:id>', methods=['PUT'])
# def update_question(id):
#     question = Question.get_by_id(id)
#     if not question:
#         return jsonify({'message': 'Question not found.'}), 404

#     text = request.json.get('text', None)
#     if not text:
#         return jsonify({'message': 'Question text is required.'}), 400

#     question.text = text
#     question.save()

#     return jsonify({'question': question})


# @questions_bp.route('/<int:id>', methods=['DELETE'])
# def delete_question(id):
#     question = Question.get_by_id(id)
#     if not question:
#         return jsonify({'message': 'Question not found.'}), 404

#     question.delete()

#     return jsonify({'message': 'Question deleted.'})

# from flask import Blueprint, jsonify, request
# from app.models.Question import Question
# from app.models.Answer import Answer
# from app.routes import question_bp, answer_bp

# #questions_bp = Blueprint('questions_bp', __name__, url_prefix='/questions')

# @question_bp.route('/', methods=['GET'])
# def list_questions():
#     questions = Question.list()
#     return jsonify({'questions': questions})

# # @questions_bp.route('/', methods=['POST'])
# # def create_question():
# #     text = request.json.get('text', None)
# #     if not text:
# #         return jsonify({'message': 'Question text is required.'}), 400

# #     question = Question(text=text)
# #     question.save()

# #     return jsonify({'question': question})

# # @questions_bp.route('/<int:id>', methods=['GET'])
# # def get_question(id):
# #     question = Question.get_by_id(id)
# #     if not question:
# #         return jsonify({'message': 'Question not found.'}), 404

# #     return jsonify({'question': question})

# # @questions_bp.route('/<int:id>', methods=['PUT'])
# # def update_question(id):
# #     question = Question.get_by_id(id)
# #     if not question:
# #         return jsonify({'message': 'Question not found.'}), 404

# #     text = request.json.get('text', None)
# #     if not text:
# #         return jsonify({'message': 'Question text is required.'}), 400

# #     question.text = text
# #     question.save()

# #     return jsonify({'question': question})

# # @questions_bp.route('/<int:id>', methods=['DELETE'])
# # def delete_question(id):
# #     question = Question.get_by_id(id)
# #     if not question:
# #         return jsonify({'message': 'Question not found.'}), 404

# #     question.delete()

# #     return jsonify({'message': 'Question deleted.'})

