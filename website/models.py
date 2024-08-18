from . import get_db_connection
from pendulum import now

def add_prompt(data, user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "INSERT INTO prompt (data, date, user_id) VALUES (?, ?, ?)"
    cur.execute(query, (data, now().to_datetime_string(), user_id))
    conn.commit()
    conn.close()

def add_poem(data, user_id, prompt_id):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "INSERT INTO poem (data, date, user_id, prompt_id) VALUES (?, ?, ?, ?)"
    cur.execute(query, (data, now().to_datetime_string(), user_id, prompt_id))
    conn.commit()
    conn.close()

def add_user(email, password, first_name):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "INSERT INTO user (email, password, first_name) VALUES (?, ?, ?)"
    cur.execute(query, (email, password, first_name))
    conn.commit()
    conn.close()

def get_prompts_by_user_id(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT * FROM prompt WHERE user_id = ?"
    cur.execute(query, (user_id,))
    prompts = cur.fetchall()
    conn.close()
    return prompts

def get_poems_by_prompt_id(prompt_id):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT * FROM poem WHERE prompt_id = ?"
    cur.execute(query, (prompt_id,))
    poems = cur.fetchall()
    conn.close()
    return poems
