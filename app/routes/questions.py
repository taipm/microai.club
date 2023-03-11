from flask import Blueprint, jsonify, request, render_template
from app.models.Question import Question
from app.models.Answer import Answer
#from Question import Question
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

# @question_bp.route('/create', methods=['POST'])
# def create_question():
#     print(f'Đang gọi hàm create_question')
#     text = request.json.get('text', None)
    
#     if not text:
#         return jsonify({'message': 'Question text is required.'}), 400

#     question = Question(text=text)
#     question.save()

#     return jsonify({'question': question})

@question_bp.route('/create', methods=['GET','POST'])
def create_question():
    question = request.form['question']
    print(f'Đang gọi hàm tạo câu hỏi {question}')
    question_id = request.form.get('question_id')
    print(f'{question_id} : {question}')
    if question_id:        
        existing_question = Question.get_by_id(question_id)
        #existing_question.answer = get_answer(existing_question)
        existing_question.save()
        return jsonify({'question_id': question_id})
        #return jsonify({'question_id': question_id, 'answer': existing_question.answer})
    
    new_question = Question(text=question)
    new_question.save()
    return jsonify({'question': question})
    #return jsonify({'question_id': new_question.id, 'answer': get_answer(new_question)})