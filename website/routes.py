import traceback
from flask import Blueprint, jsonify, redirect, render_template, request, flash, url_for

from website.chatbot import Chat
from website.functions import get_poems_by_prompt_id, get_prompts_by_user_id
from .models import Prompt, User
from . import db
from .functions import add_poem, add_prompt, get_poems_by_prompt_id, get_prompts_by_user_id  # Correctly import from functions.py
from flask_login import login_user, logout_user, current_user, login_required

routes = Blueprint('routes', __name__)


@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email, password=password).first()
        
        if user:
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        else:
            flash("Invalid credentials, try again.", category='error')
    return render_template("login.html")




# Other route functions follow the same pattern
@routes.route('/logout')
@login_required  
def logout():
    logout_user()
    return redirect(url_for('routes.login'))

@routes.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must be at least 4 characters long.", category='error')
        elif len(first_name) < 2:
            flash("First name must be at least 2 characters long.", category='error')
        elif password1 != password2:
            flash("Passwords do not match.", category='error')
        elif len(password1) < 7:
            flash("Password must be at least 7 characters long.", category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=password1)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Registration successful!", category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html")



@routes.route('/profile')
@login_required
def profile():
    user_id = current_user.id
    # Fetch all prompts for the user
    prompts = get_prompts_by_user_id(user_id)
    # Count how many times the user has used the chatbot
    chat_count = len(prompts)
    # Get the most recent 5 questions
    recent_questions = [prompt.data for prompt in prompts][-5:]
    return render_template('profile.html', chat_count=chat_count, recent_questions=recent_questions)

@routes.route('/chatbot', methods=['GET', 'POST'])
@login_required
def chatbot():
    if request.method == 'POST':
        try:
            user_input = request.form.get('message')
            if not user_input:
                return jsonify({"error": "No message provided"}), 400

            # Save the user input as a new prompt
            add_prompt(data=user_input, user_id=current_user.id)

            # Create an instance of the Chat class
            chat_instance = Chat("You are a poetic assistant. Answer questions in short poems or hiakus.")
            
            # Get the chatbot's response
            response = chat_instance.response(user_input)

            # Fetch the last prompt added to get its ID
            last_prompt = Prompt.query.filter_by(user_id=current_user.id).order_by(Prompt.id.desc()).first()

            # Save the chatbot's response as a new poem related to the prompt
            add_poem(data=response, user_id=current_user.id, prompt_id=last_prompt.id)

            # Return the chatbot's response as JSON
            return jsonify({"response": response})

        except Exception as e:
            # Log the full traceback to understand the error
            print("Error occurred:", traceback.format_exc())
            
            # Return a JSON response with the error message
            return jsonify({"error": "Internal server error"}), 500
    
    # If GET request, render the chatbot page
    return render_template("chatbot.html")

@routes.route('/chatbot2', methods=['GET', 'POST'])
@login_required
def chatbot2():
    if request.method == 'POST':
        try:
            user_input = request.form.get('message')
            if not user_input:
                return jsonify({"error": "No message provided"}), 400

            # Save the user input as a new prompt
            add_prompt(data=user_input, user_id=current_user.id)

            # Create an instance of the Chat class
            chat_instance = Chat("You are a poetic assistant. Answer questions in a long poem.")
            
            # Get the chatbot's response
            response = chat_instance.response(user_input)

            # Fetch the last prompt added to get its ID
            last_prompt = Prompt.query.filter_by(user_id=current_user.id).order_by(Prompt.id.desc()).first()

            # Save the chatbot's response as a new poem related to the prompt
            add_poem(data=response, user_id=current_user.id, prompt_id=last_prompt.id)

            # Return the chatbot's response as JSON
            return jsonify({"response": response})

        except Exception as e:
            # Log the full traceback to understand the error
            print("Error occurred:", traceback.format_exc())
            
            # Return a JSON response with the error message
            return jsonify({"error": "Internal server error"}), 500
    
    # If GET request, render the chatbot page
    return render_template("chatbot2.html")

@routes.route('/chatbot3', methods=['GET', 'POST'])
@login_required
def chatbot3():
    if request.method == 'POST':
        try:
            user_input = request.form.get('message')
            if not user_input:
                return jsonify({"error": "No message provided"}), 400

            # Save the user input as a new prompt
            add_prompt(data=user_input, user_id=current_user.id)

            # Create an instance of the Chat class
            chat_instance = Chat("You are a surfer who loves making surfing analogies.")
            
            # Get the chatbot's response
            response = chat_instance.response(user_input)

            # Fetch the last prompt added to get its ID
            last_prompt = Prompt.query.filter_by(user_id=current_user.id).order_by(Prompt.id.desc()).first()

            # Save the chatbot's response as a new poem related to the prompt
            add_poem(data=response, user_id=current_user.id, prompt_id=last_prompt.id)

            # Return the chatbot's response as JSON
            return jsonify({"response": response})

        except Exception as e:
            # Log the full traceback to understand the error
            print("Error occurred:", traceback.format_exc())
            
            # Return a JSON response with the error message
            return jsonify({"error": "Internal server error"}), 500
    
    # If GET request, render the chatbot page
    return render_template("chatbot3.html")

@routes.route('/chatbot4', methods=['GET', 'POST'])
@login_required
def chatbot4():
    if request.method == 'POST':
        try:
            user_input = request.form.get('message')
            if not user_input:
                return jsonify({"error": "No message provided"}), 400

            # Save the user input as a new prompt
            add_prompt(data=user_input, user_id=current_user.id)

            # Create an instance of the Chat class
            chat_instance = Chat("You are a drill instructor who uses visuals to teach students and you love apple pie.")
            
            # Get the chatbot's response
            response = chat_instance.response(user_input)

            # Fetch the last prompt added to get its ID
            last_prompt = Prompt.query.filter_by(user_id=current_user.id).order_by(Prompt.id.desc()).first()

            # Save the chatbot's response as a new poem related to the prompt
            add_poem(data=response, user_id=current_user.id, prompt_id=last_prompt.id)

            # Return the chatbot's response as JSON
            return jsonify({"response": response})

        except Exception as e:
            # Log the full traceback to understand the error
            print("Error occurred:", traceback.format_exc())
            
            # Return a JSON response with the error message
            return jsonify({"error": "Internal server error"}), 500
    
    # If GET request, render the chatbot page
    return render_template("chatbot4.html")

@routes.route('/chatbot5', methods=['GET', 'POST'])
@login_required
def chatbot5():
    if request.method == 'POST':
        try:
            user_input = request.form.get('message')
            if not user_input:
                return jsonify({"error": "No message provided"}), 400

            # Save the user input as a new prompt
            add_prompt(data=user_input, user_id=current_user.id)

            # Create an instance of the Chat class
            chat_instance = Chat("You are mafia crime boss who is flamboyant and one step ahead of the law.")
            
            # Get the chatbot's response
            response = chat_instance.response(user_input)

            # Fetch the last prompt added to get its ID
            last_prompt = Prompt.query.filter_by(user_id=current_user.id).order_by(Prompt.id.desc()).first()

            # Save the chatbot's response as a new poem related to the prompt
            add_poem(data=response, user_id=current_user.id, prompt_id=last_prompt.id)

            # Return the chatbot's response as JSON
            return jsonify({"response": response})

        except Exception as e:
            # Log the full traceback to understand the error
            print("Error occurred:", traceback.format_exc())
            
            # Return a JSON response with the error message
            return jsonify({"error": "Internal server error"}), 500
    
    # If GET request, render the chatbot page
    return render_template("chatbot5.html")

@routes.route('/about-us')
def about_us():
    return render_template("about-us.html")

