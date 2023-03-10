from flask import Blueprint, render_template

# Tạo blueprint với tên home
home_bp = Blueprint('home', __name__)

# Định nghĩa route trang chủ
@home_bp.route('/')
def index():
    return render_template('index.html')
