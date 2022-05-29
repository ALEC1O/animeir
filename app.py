from flask import Flask
from decouple import config

app = Flask(__name__)


@app.route('/')
def index():
    return "Index"


if __name__ == "__main__":
    app.run(port=config("PORT", 80), debug=True)
