import logging

import allure


class AssertableResponse(object):

    def __init__(self, response):
        logging.info("Request url={} body={}".format(
            response.request.url, response.request.body))
        logging.info("Response {} status {}".format(
            response.text, response.status_code))

        self._response = response

    @allure.step
    def status_code(self, code):
        logging.info("Assert: status code should be {}".format(code))
        return self._response.status_code == code

    @allure.step
    def field(self, name):
        return self._response.json()[name]
