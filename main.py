from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return ''

@app.route('/change', methods= ["POST"])
def change():
    data = request.get_json()
    print(data)

app.run('0.0.0.0')
