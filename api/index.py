import sys
import os

import mycode
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app
from flask import request, jsonify

# Vercel will look for 'app' variable 

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    action = data.get('action')
    input_text = data.get('inputText')
    if action == 'encrypt':
        output = mycode.encrypt(input_text)
    elif action == 'decrypt':
        output = mycode.decrypt(input_text)
    else:
        output = 'Invalid action'
    return jsonify({'output': output}) 