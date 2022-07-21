from flask import Flask
from decouple import config
from Global import *

app = Flask(__name__, static_folder='www/', template_folder='views/')
api = None  # Api(app)

Global.init(app, api)
Global.init_controllers()

if __name__ == "__main__":
    app.run(debug=True, port=config("PORT", 80))
