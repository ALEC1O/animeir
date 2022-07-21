from Global import *

app = Global.App


class HomeController():

    @app.route("/", methods=["GET", "POST"])
    def get():
        return render('page/home.html')
