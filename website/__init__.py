# __init__.py
from flask import Flask, app
from flask_mysqldb import MySQL


mysql = MySQL()  # Initialize MySQL instance globally


def create_app():
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'new_password'
    app.config['MYSQL_DB'] = 'drama_llama'
    app.config['MYSQL_PORT'] = 3306
    app.config['MYSQL_USE_SSL'] = False
    
    app.config['SECRET_KEY'] = '69_2024_0030'


    mysql.init_app(app)  # Attach MySQL to Flask app

    from .routes import routes
    from.views import views  
    
    app.register_blueprint(routes)
    app.register_blueprint(views)  # Register Blueprints

    return app
