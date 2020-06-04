import json
from datetime import datetime

from connpass import Connpass


def run():
    with open("connpass.json", "r") as f:
        data = json.load(f)
    connpass = Connpass.from_dict(data)
    print(connpass.events)


if __name__ == "__main__":
    run()
