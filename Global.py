from decouple import config
from flask import Flask, render_template as render, request, redirect, url_for
from flask_restx import Api, Resource


class Global:

    @staticmethod
    def init(app: Flask, api: Api, api_url: str):
        Global.App = app
        Global.Api = api
        Global.ApiUrl = api_url

        Global.AppKey = config("APP_kEY", "")
        Global.ApiKey = config("API_KEY", "")

    @staticmethod
    def init_controllers():
        from controller import HomeController
        from controller import LoginController
        from controller import RegisterController
        from controller import AccountController
