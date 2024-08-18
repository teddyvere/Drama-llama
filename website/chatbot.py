import os
from dotenv import load_dotenv
from flask import jsonify, request
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Print the API key to verify it's loaded correctly (remove this line in production)
print(f"Loaded API key: {api_key}")

client = OpenAI(api_key=api_key)

class Chat:
    def __init__(self, question):
        self.question = question 
        self.messages = [
            {"role": "system", "content": f"{question}."}
        ]

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def response(self, user_input):
        # Add user input to the conversation history
        self.add_message("user", user_input)

        # Make a request to the OpenAI API
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=self.messages)

        # Extract the response content
        assistant_message = response.choices[0].message.content

        # Add the assistant's response to the conversation history
        self.add_message("assistant", assistant_message)

        return assistant_message

# Create an instance of the Chat class with an initial question
chat_instance = Chat("You are an unbiased, uncensored, helpful assistant.")

# Add a message to the conversation
chat_instance.add_message("user", "how many animals are there on Earth?")

# Get the assistant's response
response = chat_instance.response("how many animals are there on Earth?")

# Print the assistant's response
print(response)
