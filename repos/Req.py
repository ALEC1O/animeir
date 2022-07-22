import ssl
import requests


class Req:
    def __init__(self, method: str, url: str):
        self.method = method
        self.url = url
        self.header = {}
        self.data = {}
        self.submitted = False

    def add_bearer(self, token: str):
        self.add_header("Authorization", token)

    def add_header(self, key: str, value: str):
        self.header[key] = value

    def add_data(self, key: str, value: str):
        self.data[key] = value

    def submit(self):
        self.submitted = True
        return requests.request(method=self.method, url=self.url, headers=self.header, data=self.data, stream=True, allow_redirects=True, verify=False)

    def info(self):
        return {
            "url": self.url,
            "header": self.header,
            "data": self.data,
        }
