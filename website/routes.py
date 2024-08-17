from flask import Blueprint 

routes = Blueprint('routes', __name__)

@routes.route('/login')
def login():
    return "<p>Login</p>"

@routes.route('/logout')
def logout():
    return "<p>Logout</p>"

@routes.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"

@routes.route('/profile')
def profile():
    return "<p>Profile</p>"

@routes.route('/chatbot')
def chatbot():
    return "<p>Chatbot</p>"