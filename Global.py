from decouple import config
from flask import Flask, render_template as render
from flask_restx import Api, Resource


class Global:

    @staticmethod
    def init(app: Flask, api: Api):
        Global.App = app
        Global.Api = api

        Global.AppKey = config("APP_kEY", "")
        Global.ApiKey = config("API_KEY", "")

    @staticmethod
    def init_controllers():
        from controller import HomeController
        from controller import LoginController
        from controller import AccountController
