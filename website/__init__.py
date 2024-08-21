import dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()
class Config:
    MAIL_SERVER = 'smtp.gmail.com'  # Use your email service's SMTP server
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('EMAIL_USER')  # Set this in your environment
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')  # Set this in your environment
    MAIL_DEFAULT_SENDER = ('DramaLlama', os.environ.get('EMAIL_USER'))
    MAIL_MAX_EMAILS = None
    MAIL_ASCII_ATTACHMENTS = False

mail = Mail()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '69_2024_0030'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(Config)
    
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'routes.login'
    login_manager.init_app(app)
   
    mail.init_app(app)
    
    migrate.init_app(app, db) 

    
    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    

    from .routes import routes
    from .views import views  
    
    app.register_blueprint(routes, url_prefix='/')  # Register Blueprints
    app.register_blueprint(views, url_prefix='/')  # Register Blueprints
    

    return app
