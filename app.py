from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import requests

load_dotenv()
app = Flask(__name__)

DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')

healthcare_prompt = """You are a medical assistant specializing in:
- Symptom analysis (using CDC guidelines)
- Medication interactions
- Preventive care recommendations
- Mental health first aid
- Always recommend consulting a doctor"""

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.form.get("message")
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [
            {"role": "system", "content": healthcare_prompt},
            {"role": "user", "content": user_query}
        ],
        "model": "deepseek-chat",
        "temperature": 0.1,
        "max_tokens": 300
    }
    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers=headers,
        json=payload
    )
    data = response.json()
    print("API response:", data)  # <--- Add this line

    # Try to extract the chatbot's reply
    reply = data.get("choices", [{}])[0].get("message", {}).get("content", "Sorry, I couldn't get a response.")
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(port=5000)
