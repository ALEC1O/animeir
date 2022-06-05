from flask import Flask
from decouple import config
from src.controller.HomeController import HomeController

app = Flask(__name__)

# init home manager
HomeController(app)


if __name__ == "__main__":
    app.run(port=config("PORT", 80), debug=True)
