import os
from flask import Flask, jsonify, Response, request, render_template
import mycode  # Pastikan file mycode.py ada di direktori yang sama

app = Flask(__name__)

# Error 404 handler


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

# Error 405 handler


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(error=str(e)), 405

# Error 401 handler


@app.errorhandler(401)
def unauthorized(e):
    return Response("API Key required.", 401)


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['text']
        encrypt_text = mycode.encrypt(user_input)
        decrypt_text = mycode.decrypt(encrypt_text)
        return render_template('index.html', encrypt_text=encrypt_text, decrypt_text=decrypt_text)
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8888))
    app.run(host='0.0.0.0', port=port)
