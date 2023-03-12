from flask import Blueprint, jsonify, render_template

# Tạo blueprint với tên home
home_bp = Blueprint('home', __name__)

# Định nghĩa route trang chủ
@home_bp.route('/')
def index():
    return render_template('index.html')

@home_bp.route('/time')
def get_time():
    # Lấy thời gian hiện tại và chuyển đổi thành chuỗi
    import datetime
    time_now = datetime.datetime.now().strftime('%H:%M:%S')

    # Trả về kết quả dưới dạng JSON
    return jsonify({'time': time_now})