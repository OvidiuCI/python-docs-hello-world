from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Ovidiu! this is the python app!"
