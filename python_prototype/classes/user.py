from datetime import datetime
from typing import Optional, List, Dict, Any

class User:
    def __init__(self, data: Dict[str, Any]):
        self.id: int = data.get("ID")
        self.name: str = data.get("Name")
        self.twitch_id: Optional[str] = data.get("Twitch_ID")
        self.discord_id: Optional[str] = data.get("Discord_ID")
        self.started_using: datetime = data.get("Started_Using") or datetime.utcnow()
        self._data_cache: Dict[str, Any] = {}

    def __repr__(self):
        return f"<User name={self.name} id={self.id}>"

    @classmethod
    async def get(cls, identifier: Any) -> Optional['User']:
        # Mocking the get logic for the prototype
        print(f"Buscando usuário: {identifier}")
        return cls({"ID": 1, "Name": "supinic", "Twitch_ID": "12345"})

    async def get_data_property(self, property_name: str) -> Any:
        return self._data_cache.get(property_name)

    async def set_data_property(self, property_name: str, value: Any):
        self._data_cache[property_name] = value
