from typing import Optional, Set, Dict, Any

class Channel:
    def __init__(self, data: Dict[str, Any], platform):
        self.id: int = data.get("ID")
        self.name: str = data.get("Name")
        self.platform = platform
        self.mode: str = data.get("Mode", "Write")
        self.nsfw: bool = data.get("NSFW", False)
        self.message_limit: Optional[int] = data.get("Message_Limit")
        self._data_cache: Dict[str, Any] = {}

    def __repr__(self):
        return f"<Channel name={self.name} platform={self.platform.name}>"

    async def send(self, message: str):
        await self.platform.send(message, self)

    async def get_data_property(self, property_name: str) -> Any:
        return self._data_cache.get(property_name)
