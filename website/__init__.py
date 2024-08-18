from flask import Flask
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('drama_llama.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            first_name TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prompt (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            date TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS poem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            date TEXT NOT NULL,
            user_id INTEGER,
            prompt_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (prompt_id) REFERENCES prompt(id)
        )
    ''')
    
    conn.commit()
    conn.close()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '69_2024_0030'
    
    init_db()  # Initialize the database

    from .routes import routes
    from .views import views  
    
    app.register_blueprint(routes)
    app.register_blueprint(views)  # Register Blueprints

    return app
