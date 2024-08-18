# routes.py
from flask import Blueprint, render_template, request, flash, current_app
from . import get_db_connection

routes = Blueprint('routes', __name__)

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            flash("Logged in successfully!", category='success')
        else:
            flash("Invalid credentials, try again.", category='error')
    return render_template("login.html")

# Other route functions follow the same pattern

@routes.route('/logout')
def logout():
    return render_template("logout.html")

@routes.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        try:
            if len(email) < 4:
                flash("Email must be at least 4 characters long.", category='error')
                return render_template("sign-up.html")
            if len(firstName) < 2:
                flash("First name must be at least 2 characters long.", category='error')
                return render_template("sign-up.html")
            if password1 != password2:
                flash("Passwords do not match.", category='error')
                return render_template("sign-up.html")
            if len(password1) < 7:
                flash("Password must be at least 7 characters long.", category='error')
                return render_template("sign-up.html")

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (email, first_name, password) VALUES (?, ?, ?)", (email, firstName, password1))
            conn.commit()
            conn.close()
            flash("Registration successful!", category='success')
        except Exception as e:
            flash(f"Database error: {e}", category='error')

    return render_template("sign-up.html")

@routes.route('/profile')
def profile():
    return render_template("profile.html")

@routes.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

@routes.route('/about-us')
def about_us():
    return render_template("about-us.html")

# In routes.py or wherever you handle routes
@routes.route('/data-page')
def get_data():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM some_table")
    data = cursor.fetchall()
    cursor.close()
    return render_template('data-page.html')
