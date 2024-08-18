from flask import Flask
from flask_mysqldb import MySQL



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '69-003-1590'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'new_password'
    app.config['MYSQL_DB'] = 'drama_llama'
    db.init_app(app)
    
    from .views import views
    from .routes import routes
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(routes, url_prefix='/')    
    return app