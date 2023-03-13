from flask import Blueprint

question_bp = Blueprint('questions', __name__, url_prefix='/questions')
answers_bp = Blueprint('answers', __name__, url_prefix='/answers')
home_bp = Blueprint('home', __name__)
intraday_bp= Blueprint('intraday', __name__,url_prefix='/intraday')

# from . import questions, answers, home
# from models import Question, Answer