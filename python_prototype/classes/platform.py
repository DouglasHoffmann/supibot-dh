from abc import ABC, abstractmethod
from typing import Optional

class Platform(ABC):
    def __init__(self, name: str, config: dict):
        self.name = name
        self.config = config
        self.id = config.get("ID")

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def send(self, message: str, channel):
        pass

    @abstractmethod
    async def pm(self, message: str, user):
        pass
