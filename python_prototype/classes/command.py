from typing import Optional, List, Any, Dict, Callable, Awaitable

class Command:
    def __init__(self, definition: Dict[str, Any]):
        self.name: str = definition["Name"]
        self.aliases: List[str] = definition.get("Aliases") or []
        self.description: str = definition.get("Description")
        self.cooldown: int = definition.get("Cooldown", 5000)
        self.flags: List[str] = definition.get("Flags", [])
        self.code: Callable[['Context', Any], Awaitable[Dict[str, Any]]] = definition["Code"]

    async def execute(self, context: 'Context', *args: str) -> Dict[str, Any]:
        return await self.code(context, *args)

class Context:
    def __init__(self, command: Command, user, platform, channel=None, invocation=None, params=None):
        self.command = command
        self.user = user
        self.platform = platform
        self.channel = channel
        self.invocation = invocation or command.name
        self.params = params or {}
        self.args = []

    async def reply(self, message: str):
        if self.channel:
            await self.channel.send(message)
        else:
            await self.platform.pm(message, self.user)
