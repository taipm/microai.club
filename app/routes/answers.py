from flask import Blueprint, jsonify, request
from translate import Translator
from app.models.Answer import Answer
from app.ai.MicroAI import MicroAI
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

@answers_bp.route('/answer', methods=['POST'])
def answer_question():
    # Lấy dữ liệu từ form trả lời câu hỏi
    question_id = request.form.get('question_id')
    answer_text = request.form.get('answer')
    print(f'Đang trả lời {question_id} : {answer_text}')
    # Tìm câu hỏi tương ứng trong cơ sở dữ liệu
    question = Question.get_by_id(question_id)    
    answer = Answer(text=answer_text, question_id=question_id)
    #answer.question_id = question_id

    # Lưu câu trả lời vào cơ sở dữ liệu
    answer.save()

    # Thêm câu trả lời vào danh sách các câu trả lời của câu hỏi tương ứng
    question.answers.append(answer)
    question.save()

    #return jsonify({'answer': answer_text})
    # Trả về thông tin của câu trả lời để cập nhật trang web
    return jsonify({
        'engine':'User',
        'answer': answer.text,
        'created_at': answer.created_at.strftime('%Y-%m-%d %H:%M:%S')
    })

@answers_bp.route('/microai_answer', methods=['POST'])
def microai_answer():    
    question_id = request.form.get('question_id')
    print(f'Đang gọi hàm micro_answer(){question_id}')
    question = Question.get_by_id(question_id)
    if not question:
        return jsonify({'success': False, 'message': 'Question not found'}), 404
    open_ai_key = get_openai_key()
    text = MicroAI(api_key=open_ai_key).generate_answer(question.text)
    answer = question.add_answer(text)
    return jsonify({'answer': text})

@answers_bp.route('/translate', methods=['POST'])
def translate():
    text = request.form.get('answer')
    print(f'Đang gọi hàm translate: {text}')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    translator = Translator(to_lang='vi', from_lang='en')
    try:
        transText = translator.translate(text=text)
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to translate text'}), 500
    return jsonify({'answer': transText})


