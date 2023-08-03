from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input', '').lower()

    if user_input == 'hello':
        api_url = 'http://localhost:5000/api/welcome'  # Replace with the actual Flask backend URL
        response = requests.post(api_url, json={'user_input': user_input})

        if response.status_code == 200:
            data = response.json()
            reply = data.get('reply', 'Unknown response')
            return jsonify({'reply': reply})
        else:
            return jsonify({'reply': f"Error: {response.status_code} - {response.text}"})
    else:
        return jsonify({'reply': 'Invalid input. Please enter "hello".'})

if __name__ == '__main__':
    app.run(port=4000)
