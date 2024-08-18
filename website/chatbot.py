from flask import jsonify, request
import openai

openai.api_key = "Your_OPENAI_API_KEY_HERE"

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
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.messages
        )

        # Extract the response content
        assistant_message = response['choices'][0]['message']['content']

        # Add the assistant's response to the conversation history
        self.add_message("assistant", assistant_message)

        return assistant_message
