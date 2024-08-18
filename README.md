# setup venv
python3 -m venv venv
source venv/bin/activate  

# setup databases

go into init.py and link your mysql database and 
create the tables referenced

CREATE DATABASE drama_llama;
USE drama_llama;

-- Create a Users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(150) NOT NULL,
    first_name VARCHAR(150) NOT NULL
);

-- Create a Prompts table
CREATE TABLE prompts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data TEXT NOT NULL,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create a Poems table
CREATE TABLE poems (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data TEXT NOT NULL,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    prompt_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (prompt_id) REFERENCES prompts(id)
);

# install libraries 

pip3 install Flask --break-system-packages

pip3 install flask_login --break-system-packages

pip install mysqlclient --break-system-packages

# Run main App
python3 main.py