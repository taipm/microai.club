from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes.questions import question_bp
    app.register_blueprint(question_bp)

    from .routes.answers import answers_bp
    app.register_blueprint(answers_bp)

    from .routes.home import home_bp
    app.register_blueprint(home_bp)

    return app
