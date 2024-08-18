from flask import Blueprint, render_template, request, flash

routes = Blueprint('routes', __name__)


@routes.route('/login', methods=['GET', 'POST'])  # Add POST method for form submission)
def login():
    data = request.form
    print(data)  # Print form data for debugging purposes
    return render_template("login.html")

@routes.route('/logout')
def logout():
    return render_template("logout.html")

@routes.route('/sign-up', methods=['GET', 'POST'])  # Add POST method for form submission)
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash("Email must be at least 4 characters long.", category='error')
        elif len(firstName) < 2:
            flash("First name must be at least 2 characters long.", category='error')
        elif len(password1) < 7:
            flash("Password must be at least 7 characters long.", category='error')
        elif password1 != password2:
            flash("Passwords do not match.", category='error')
        else:
            flash("Registration successful!", category='success')
    
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