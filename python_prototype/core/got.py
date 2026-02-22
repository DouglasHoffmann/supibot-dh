import httpx
from typing import Any, Dict, Optional

class Got:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def get(self, api_name: str, **kwargs) -> httpx.Response:
        # Simplificação: em um sistema real, api_name mapearia para URLs base
        url = kwargs.pop("url", None)
        return await self.client.get(url, **kwargs)

    async def post(self, api_name: str, **kwargs) -> httpx.Response:
        url = kwargs.pop("url", None)
        return await self.client.post(url, **kwargs)

    async def close(self):
        await self.client.aclose()

got = Got()
