from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.questions import question_bp
    app.register_blueprint(question_bp)

    from app.routes.answers import answers_bp
    app.register_blueprint(answers_bp)

    from app.routes.home import home_bp
    app.register_blueprint(home_bp)

    from app.routes.intraday import intraday_bp
    #app.register_blueprint(intraday_bp)
    app.register_blueprint(intraday_bp)



    return app
