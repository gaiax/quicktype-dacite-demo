from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from dacite import Config, from_dict


@dataclass
class Series:
    id: int
    title: str
    url: str


@dataclass
class Event:
    event_id: int
    title: str
    catch: str
    description: str
    event_url: str
    started_at: datetime
    ended_at: datetime
    limit: Optional[int]
    hash_tag: str
    event_type: str
    accepted: int
    waiting: int
    updated_at: datetime
    owner_id: int
    owner_nickname: str
    owner_display_name: str
    place: Optional[str]
    address: Optional[str]
    lat: Optional[str]
    lon: Optional[str]
    series: Optional[Series]


@dataclass
class Connpass:
    results_start: int
    results_returned: int
    results_available: int
    events: List[Event]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Connpass":
        return from_dict(cls, data, config=Config({datetime: datetime.fromisoformat}))

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
