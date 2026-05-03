from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from app.config import Config

login_manager = LoginManager()
bcrypt = Bcrypt()

login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.db import init_db
    init_db(app)

    # Register blueprints (we will create these later)
    from app.routes.auth import auth_bp
    from app.routes.projects import projects_bp
    from app.routes.tasks import tasks_bp
    from app.routes.views import views_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(projects_bp, url_prefix='/api/projects')
    app.register_blueprint(tasks_bp, url_prefix='/api/tasks')
    app.register_blueprint(views_bp)

    return app
