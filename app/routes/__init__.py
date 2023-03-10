from flask import Blueprint

question_bp = Blueprint('questions', __name__, url_prefix='/questions')
answers_bp = Blueprint('answers', __name__, url_prefix='/answers')
home_bp = Blueprint('home', __name__)

from . import questions, answers, home