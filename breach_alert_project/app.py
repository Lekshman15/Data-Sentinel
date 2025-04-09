from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'cce8798131195b24acd5ce105b95f960c39226df'  # Replace with your key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    email = request.form['email']

    url = 'https://leakcheck.io/api/public'
    params = {
        'key': API_KEY,
        'check': email,
        'type': 'email'
    }

    response = requests.get(url, params=params)
    result = response.json()

    if result.get("success") and result.get("found"):
        return f"⚠️ Your email has been found in {result.get('sources')} breaches!"
    else:
        return "✅ Your email is safe! No breaches found."

# 💥 Run Flask without crashing Spyder
if __name__ == '__main__':
    import os
    os.environ["FLASK_ENV"] = "development"
    try:
        app.run(debug=True, use_reloader=False)
    except SystemExit:
        pass
