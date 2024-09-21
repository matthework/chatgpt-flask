import os

from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Allow only specific origin (the URL of frontend app)
# CORS(app, resources={r"/*": {"origins": os.getenv("CLIENT_URL")}})
# Enable CORS for all routes
CORS(app)


# Load environment variables from a .env file
load_dotenv(override=True)

# OpenAI API v1.46.1
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


@app.route("/")
def home():
    return "Server is ready!"


@app.route("/api/chatgpt", methods=["POST"])
def chat():
    try:
        # Get user input from the React frontend
        data = request.json
        user_input = data.get("message")

        # Make a request to OpenAI API 1.47+
        chat_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
        )

        # Get the response text
        response = chat_completion.choices[0].message.content

        # Send back the response to the frontend
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    if os.getenv("FLASK_ENV") == "production":
        app.config["DEBUG"] = False
    else:
        app.config["DEBUG"] = True

    app.run()
