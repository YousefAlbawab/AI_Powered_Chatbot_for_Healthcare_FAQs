# AI-Powered Chatbot for Healthcare FAQs

A simple web-based healthcare FAQ chatbot powered by Python and Flask.  
Ask health-related questions and get instant AI-powered responses in your browser!

## Features

- Easy to run locally (just Python required)
- Simple web interface (no extra software needed)
- Uses DeepSeek API (requires your own free API key)
- No medical advice given-always consult a professional!

## Setup Instructions

### 1. Clone the Repository

git clone 

### 2. Create and Activate a Virtual Environment

python -m venv .venv

On Windows:
.venv\Scripts\activate

On Mac/Linux:
source .venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Get Your Own DeepSeek API Key

- Sign up at [DeepSeek Platform](https://platform.deepseek.com/)
- Go to **API Keys** in your account dashboard
- Click **Create New Key**
- Copy your API key (keep it private!)

### 5. Add Your API Key to a `.env` File

Create a file named `.env` in the project root with this line (replace with your actual key):

DEEPSEEK_API_KEY=your_deepseek_api_key_here

### 6. Run the Chatbot

python app.py

Open your browser and go to http://127.0.0.1:5000/

## Usage

- Type your healthcare question in the chat box and press "Send".
- The bot will reply using the DEEPSEEK model.
- **Note:** This chatbot is for informational purposes only and does not provide medical advice.

## License

This project is licensed under the MIT License.

## Credits

- [Flask](https://flask.palletsprojects.com/)
- [DeepSeek API](https://platform.deepseek.com/)