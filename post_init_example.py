from dataclasses import dataclass
from datetime import datetime
from typing import Union

from dacite import from_dict


@dataclass
class Sample:
    text: str
    created_at: Union[str, datetime]
    timestamp: Union[int, datetime]

    def __post_init__(self):
        self.__convert_created_at()
        self.__convert_timestamp()

    def __convert_created_at(self):
        if type(self.created_at) is str:
            self.created_at =datetime.strptime(self.created_at, "%a %b %d %H:%M:%S %z %Y")

    def __convert_timestamp(self):
        if type(self.timestamp) is int:
            self.timestamp = datetime.fromtimestamp(self.timestamp)

def run():
    data = {"text": "hello world", "created_at": "Thu Jun 04 11:27:06 +0900 2020",  "timestamp": 1591237626}
    sample = from_dict(Sample, data)
    print(sample)


if __name__ == "__main__":
    run()
