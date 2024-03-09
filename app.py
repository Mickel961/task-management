from flask import Flask
from config.config import Config
from models.task import db
from controllers.taskController import task_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(task_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
