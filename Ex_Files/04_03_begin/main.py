from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, Nhu!"


app.run(debug=True)
