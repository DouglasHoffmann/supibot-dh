from datetime import datetime
from typing import Optional, List, Dict, Any
from core import core

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
        # Simulando busca no Cache ou DB via core
        cache_key = f"sb-user-{identifier}"
        cached = await core.Cache.get_by_prefix(cache_key)
        if cached:
            return cls(cached)

        # Simulação de busca no DB
        db_user = await core.Query.get_recordset(lambda rs: rs.select("*").from_("chat_data", "User_Alias").where("Name = %s", identifier).single())

        # Mock para o protótipo
        mock_data = {"ID": 1, "Name": str(identifier), "Twitch_ID": "12345"}
        await core.Cache.set_by_prefix(cache_key, mock_data)
        return cls(mock_data)

    async def get_data_property(self, property_name: str) -> Any:
        return self._data_cache.get(property_name)

    async def set_data_property(self, property_name: str, value: Any):
        self._data_cache[property_name] = value
