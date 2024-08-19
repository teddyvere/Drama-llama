from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '69_2024_0030'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drama_llama.db'  # Change this URI as needed
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'routes.login'
    login_manager.init_app(app)
    
    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    

    from .routes import routes
    from .views import views  
    
    app.register_blueprint(routes, url_prefix='/')  # Register Blueprints
    app.register_blueprint(views, url_prefix='/')  # Register Blueprints
    

    return app
