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
    def __init__(self, initial_instruction):
        self.instruction = initial_instruction 
        self.messages = [
            {"role": "system", "content": self.instruction}
        ]

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def response(self, user_input):
        # Define the character limit
        char_limit = 180

        # Check if the user input exceeds the character limit
        if len(user_input) > char_limit:
            return f"Error: Your input exceeds the {char_limit} character limit. Please shorten your message."

        # Add user input to the conversation history
        self.add_message("user", user_input)

        # Make a request to the OpenAI API
        response = client.chat.completions.create(model="gpt-3.5-turbo-16k",
        messages=self.messages)

        # Extract the response content
        assistant_message = response.choices[0].message.content

        # Add the assistant's response to the conversation history
        self.add_message("assistant", assistant_message)

        return assistant_message
