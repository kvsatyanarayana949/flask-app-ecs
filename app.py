from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hey, welcome to DevOps My flask app"

@app.route('/health')
def health():
    return {"status": "UP"}, 20
