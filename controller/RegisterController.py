from Global import *

app = Global.App


class RegisterController():

    @app.route("/register", methods=["GET"])
    def register_get():
        return render('page/register.html')
