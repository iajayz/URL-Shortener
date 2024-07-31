# app.py
from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)

# Dictionary to store mappings between short codes and long URLs
url_database = {}

# Function to generate a random short code
def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))  # 6-character short code
    return short_code

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# URL shortening route
@app.route('/shorten_url', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    short_code = generate_short_code()
    url_database[short_code] = long_url
    short_url = request.host_url + short_code
    return render_template('result.html', short_url=short_url)

# Redirect route for short URLs
@app.route('/<short_code>')
def redirect_to_long_url(short_code):
    long_url = url_database.get(short_code)
    if long_url:
        return redirect(long_url)
    else:
        return "Short URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
