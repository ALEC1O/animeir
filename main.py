from Global import *

app = Flask(__name__, static_folder='www/', template_folder='views/')
api = None  # Api(app)
api_url = config("API_URL", "http://localhost:5206")

Global.init(app, api, api_url)
Global.init_controllers()

if __name__ == "__main__":
    app.run(debug=True, port=config("PORT", 80))
