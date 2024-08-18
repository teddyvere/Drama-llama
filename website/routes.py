from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)


@routes.route('/login')
def login():
    return render_template("login.html")

@routes.route('/logout')
def logout():
    return render_template("logout.html")

@routes.route('/sign-up')
def sign_up():
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