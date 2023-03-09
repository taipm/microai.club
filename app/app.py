from datetime import datetime
import os
from flask import Flask, render_template, jsonify
from flask import request
from models.Answer import Answer
from models.Question import Question

app = Flask(__name__)

@app.route('/')
def home():
    print(f'Home')
    return render_template('index.html')

@app.route('/api/time')
def get_time():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Thời gian:{time}')
    return jsonify({'time': time})

@app.route('/questions')
def list_questions():
    questions = Question.list()
    return render_template('questions.html', questions=questions)

@app.route('/questions/<question_id>')
def question_detail(question_id):
    question = Question.get_by_id(question_id)
    if not question:
        return render_template('404.html'), 404
    
    answers = Answer.get_by_question_id(question_id=question_id)
    print(f'{len(answers)}')
    return render_template('question_detail.html', question=question, answers=answers)

@app.route('/api/question', methods=['GET','POST'])
def create_question():
    
    question = request.form['question']
    print(f'Đang gọi hàm tạo câu hỏi {question}')
    question_id = request.form.get('question_id')
    print(f'{question_id} : {question}')
    if question_id:        
        existing_question = Question.get_by_id(question_id)
        #existing_question.answer = get_answer(existing_question)
        existing_question.save()
        return jsonify({'question_id': question_id, 'answer': existing_question.answer})
    
    new_question = Question(text=question)
    new_question.save()
    return jsonify({'question_id': new_question.id, 'answer': get_answer(new_question)})

@app.route('/api/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        question = request.form['question']
        question_id = request.form.get('question_id')

        if question_id:
            existing_question = Question.get_by_id(question_id)
            existing_question.answer = get_answer(existing_question)
            existing_question.save()
            return jsonify({'question_id': question_id, 'answer': existing_question.answer})

        new_question = Question(text=question)
        new_question.save()
        return jsonify({'question_id': new_question.id, 'answer': get_answer(new_question)})
    return render_template('ask.html')

@app.route('/api/answer', methods=['POST'])
def add_answer():
    question_id = request.form.get('question_id')
    text = request.form.get('answer')
    question = Question.get_by_id(question_id)
    if not question:
        return jsonify({'success': False, 'message': 'Question not found'}), 404
    question.add_answer(text)
    return jsonify({'success': True})

def get_answer(q:Question):
    # Implement your logic for generating the answer based on the question
    answer = "This is the answer to your question."
    # a = Answer(question_id=q.id,text=answer)
    # a.save()
    return answer#a.text

@app.route('/api/answers')
def list_answers():
    answers = Answer.list()
    return render_template('answers.html', answers=answers)

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=5000)
    app.run(debug=True, threaded=True)

