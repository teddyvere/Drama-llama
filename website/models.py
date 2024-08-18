from pendulum import now
from flask_mysqldb import MySQL  # Make sure mysql is properly imported from where it's initialized
from . import mysql  # Adjust the import statement based on your actual app structure

# Function to add a prompt
def add_prompt(data, user_id):
    cur = mysql.connection.cursor()
    query = "INSERT INTO prompt (data, date, user_id) VALUES (%s, %s, %s)"
    cur.execute(query, (data, now().to_datetime_string(), user_id))
    mysql.connection.commit()
    cur.close()

# Function to add a poem
def add_poem(data, user_id, prompt_id):
    cur = mysql.connection.cursor()
    query = "INSERT INTO poem (data, date, user_id, prompt_id) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (data, now().to_datetime_string(), user_id, prompt_id))
    mysql.connection.commit()
    cur.close()

# Function to add a user
def add_user(email, password, first_name):
    cur = mysql.connection.cursor()
    query = "INSERT INTO user (email, password, first_name) VALUES (%s, %s, %s)"
    cur.execute(query, (email, password, first_name))
    mysql.connection.commit()
    cur.close()

# Function to fetch prompts by user ID
def get_prompts_by_user_id(user_id):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM prompt WHERE user_id = %s"
    cur.execute(query, (user_id,))
    prompts = cur.fetchall()
    cur.close()
    return prompts

# Function to fetch poems by prompt ID
def get_poems_by_prompt_id(prompt_id):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM poem WHERE prompt_id = %s"
    cur.execute(query, (prompt_id,))
    poems = cur.fetchall()
    cur.close()
    return poems
