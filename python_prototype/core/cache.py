from typing import Any, Optional

class Cache:
    def __init__(self):
        self._store = {}

    async def get_by_prefix(self, prefix: str) -> Optional[Any]:
        return self._store.get(prefix)

    async def set_by_prefix(self, prefix: str, value: Any, options: dict = None):
        self._store[prefix] = value

    async def delete(self, key: str):
        if key in self._store:
            del self._store[key]

cache = Cache()
