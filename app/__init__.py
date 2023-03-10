from flask import Flask

def create_app():
    # Tạo instance của Flask với tên app
    app = Flask(__name__)

    # Import các routes
    from app.routes.questions import question_bp
    #from app.routes.answers import answer_bp
    from app.routes.home import home_bp

    # Register các blueprint
    app.register_blueprint(question_bp)
    # app.register_blueprint(answer_bp)
    app.register_blueprint(home_bp)

    return app