from flask import Flask, request, jsonify, render_template
import google.generativeai as gen

app = Flask(__name__)

# Configure the Google generative AI model
API_KEY = "AIzaSyA4CNpHvZPgiWqXyE-KvDinyXHecSzk-xA"
gen.configure(api_key=API_KEY)
model = gen.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def chat_api():
    data = request.get_json()
    message = data['message']
    response = chat.send_message(message)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)
