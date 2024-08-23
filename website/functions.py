from datetime import datetime
from .models import db, Users, Prompt, Poem
from pendulum import now

def add_prompt(data, user_id):
    # Use datetime.now() to get the current date and time as a datetime object
    new_prompt = Prompt(data=data, date=datetime.now(), user_id=user_id)
    db.session.add(new_prompt)
    db.session.commit()

def add_poem(data, user_id, prompt_id):
    # Use datetime.now() to get the current date and time as a datetime object
    new_poem = Poem(data=data, date=datetime.now(), user_id=user_id, prompt_id=prompt_id)
    db.session.add(new_poem)
    db.session.commit()

def add_user(email, password, first_name):
    new_user = Users(email=email, password=password, first_name=first_name)
    db.session.add(new_user)
    db.session.commit()

def get_prompts_by_user_id(user_id):
    return Prompt.query.filter_by(user_id=user_id).all()

def get_poems_by_prompt_id(prompt_id):
    return Poem.query.filter_by(prompt_id=prompt_id).all()
