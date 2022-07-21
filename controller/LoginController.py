from Global import *

app = Global.App


class LoginController():

    @app.route("/login", methods=["GET"])
    def login_get():
        return render('page/login.html')
