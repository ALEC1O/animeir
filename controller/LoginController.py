from flask import session
from repos.Req import Req
from Global import *
app = Global.App


class LoginController():

    @app.route("/login", methods=["GET"])
    def login_get():
        return render('page/login.html')

    @app.route("/login", methods=["POST"])
    def login_post():
        email = request.form.get("email")
        password = request.form.get("password")

        message = {}

        # check if email exist
        if not email:
            message["error"] = "email not found"
            return render("page/login.html", message=message)

        # check if password exist
        if not password:
            message["error"] = "password not found"
            return render("page/login.html", message=message)

        # check user and password in api

        req = Req(method="GET", url=f"{Global.ApiUrl}/v1/login")
        req.add_bearer(Global.ApiKey)
        req.add_data("email", email)
        req.add_data("password", password)

        result = req.submit()

        if result.status_code != 200:
            message["error"] = "email or password invalid"
            return render("page/login.html", message=message)

        if len(result.json()) <= 0:
            message["error"] = "internal error"
            return render("page/login.html", message=message)

        data = result.json()

        name = data["name"]
        email = data["email"]

        # save session
        login = {"name": name, "email": email}
        session["login"] = login

        return login
