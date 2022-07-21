from Global import *

app = Flask(__name__)
api = Api(app)

Global.init(app, api)
Global.init_controllers()

if __name__ == "__main__":
    app.run(debug=True, port=config("PORT", 80))
