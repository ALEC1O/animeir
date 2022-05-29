from flask import Flask, Blueprint, render_template as render


class HomeController:

    def __init__(self, app: Flask):

        route = Blueprint('home', __name__, static_folder='../www', template_folder='../views')

        @route.route('/')
        def a():

            return render('index.html')

        app.register_blueprint(route)
