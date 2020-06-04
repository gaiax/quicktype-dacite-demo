from dataclasses import dataclass

from dacite import from_dict
import responder
import requests

from connpass import Connpass


api = responder.API()

API_URL = "https://connpass.com/api/v1/event/"


@api.route("/")
def index(req: responder.Request, resp: responder.Response):
    resp.media = {"status": "ok"}


@api.route("/connpass/titles")
def connpass_titles(req: responder.Request, resp: responder.Response):
    """connpass のイベントのタイトルのみ返す"""
    response = requests.get(API_URL, params=req.params)
    connpass = Connpass.from_dict(response.json())
    resp.media = [event.title for event in connpass.events]


if __name__ == "__main__":
    api.run()
