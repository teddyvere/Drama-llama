from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/left_sidebar')
def left_sidebar():
    return render_template("left_sidebar.html")

@views.route('/right_sidebar')
def right_sidebar():
    return render_template("right_sidebar.html")

@views.route('/no_sidebar')
def no_sidebar():
    return render_template("no_sidebar.html")