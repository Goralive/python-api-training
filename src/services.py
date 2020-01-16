import json
import os

import requests

import allure
from src.response import AssertableResponse


class ApiService(object):

    def __init__(self):
        self._base_url = os.environ['BASE_URL']
        self._headers = {'content-type': 'application/json'}

    def _post(self, url, body):
        # self._headers
        return requests.post("{}{}".format(self._base_url, url), data=json.dumps(body),
                             headers=self._headers)

    # def auth(self):
    #     return requests.post("").json()["token"]


class UserApiService(ApiService):

    def __init__(self):
        super().__init__()

    @allure.step
    def create_user(self, user):
        # token = self.auth()

        return AssertableResponse(self._post("/register", user))
