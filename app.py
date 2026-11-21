from flask import Flask, jsonify
import socket

app = Flask(__Sourav__)

@app.route('/')
def home():
    return f"<h1>End-to-End DevOps CI/CD Project!</h1><p>Pod: {socket.gethostname()}</p>"

@app.route('/health')
def health():
    return jsonify(status="UP", pod=socket.gethostname()), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
