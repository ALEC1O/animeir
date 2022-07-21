from decouple import config
from flask import Flask
from flask_restx import Api, Model


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
        from controller import AccountController
