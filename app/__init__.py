from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.secret_key = "your-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.task import tasks_bp

    app.register_blueprint(auth_bp, url_prefix='/')      # good as is
    app.register_blueprint(tasks_bp)                     # ✅ Remove '/tasks' if you want home at '/'

    return app



