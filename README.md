# Summary
Drama Llama
Drama Llama is a unique conversational AI chatbot that brings poetry to life. This project combines the power of Python, Flask, and web development to create a chatbot that responds to user queries in various poetic forms like haikus, sonnets, free verse, and more.

Table of Contents
Introduction
Features
Installation
Usage
Environment Variables
Contributing
License
Contact
Introduction
In a world where chatbots are becoming increasingly common, Drama Llama stands out by adding a touch of artistry to AI. Our vision is to create a platform where users can engage with a chatbot that responds exclusively in poems. Whether you're seeking advice, looking for a bit of fun, or just want to experience the magic of poetry, Drama Llama is your go-to companion.

Features
Poetic Responses: Engage with a chatbot that responds in various poetic forms.
Multiple Modes: Choose between haiku, free verse, sonnet, acrostic, and more.
User Profiles: Track how many times you've interacted with the chatbot and see your recent questions.
Social Sharing: Share your poetic interactions with friends via social media.
Email Support: Send feedback or inquiries through the integrated email form.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/drama-llama.git
cd drama-llama
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

bash
Copy code
flask db init
flask db migrate
flask db upgrade
Run the Flask app:

bash
Copy code
flask run
Usage
Visit the homepage to interact with the Drama Llama chatbot.
Choose from different poetic styles by selecting from the options.
Enter your message, and let Drama Llama craft a poetic response.
Share the generated poems or save them for later.
Check your profile to see how many times you've interacted with the chatbot and view your recent queries.
Environment Variables
Make sure you have the following environment variables set:

FLASK_APP: The Flask application entry point (usually set to main.py).
FLASK_ENV: Set to development for development mode, production for production.
DATABASE_URL: The URL of your database.
SECRET_KEY: A secret key for securing sessions and cookies.
MAIL_USERNAME: The email address to be used for sending emails.
MAIL_PASSWORD: The password for the email account.
Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome contributions of all types, from bug fixes to new features.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any questions, suggestions, or feedback, feel free to contact us:

Project Maintainer: Your Name
Email: teddyvere@gmail.com



# setup venv
python3 -m venv venv
source venv/bin/activate  

# setup API KEY

create an .env and place your pi key inside


# install libraries 

pip3 install Flask --break-system-packages

pip3 install flask_login --break-system-packages

pip3 install mysqlclient --break-system-packages

pip3 install Flask-Migrate  --break-system-packages

pip3 install Flask-Mail --break-system-packages


# Run main App
python3 main.py