from status import Status
from jobs import Jobs
from lib.items.items import Item
from typing import List


class Player():

    name: str
    status: Status
    job: Jobs
    items: List[Item]

    def __init__(self, name: str, status: Status, job: Jobs) -> None:
        self.name = name
        self.status = status
        self.job = job

