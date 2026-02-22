import re
from typing import Optional, List, Any, Dict, Callable, Awaitable, Tuple

class Command:
    def __init__(self, definition: Dict[str, Any]):
        self.name: str = definition["Name"]
        self.aliases: List[str] = definition.get("Aliases") or []
        self.description: str = definition.get("Description")
        self.cooldown: int = definition.get("Cooldown", 5000)
        self.flags: List[str] = definition.get("Flags", [])
        self.params_def: List[Dict[str, str]] = definition.get("Params") or []
        self.code: Callable[['Context', Any], Awaitable[Dict[str, Any]]] = definition["Code"]

    async def execute(self, context: 'Context', *args: str) -> Dict[str, Any]:
        return await self.code(context, *args)

class Parser:
    @staticmethod
    def parse_params(params_def: List[Dict[str, str]], args: List[str]) -> Tuple[Dict[str, Any], List[str]]:
        params = {}
        remaining_args = []

        args_str = " ".join(args)
        # Simplificação do parser de parâmetros do Supibot (param:valor)
        for param in params_def:
            name = param["name"]
            match = re.search(f"{name}:(\"([^\"]*)\"|([^\\s]*))", args_str)
            if match:
                value = match.group(2) or match.group(3)
                params[name] = value
                # Remove do args_str para não sobrar no remaining_args
                args_str = args_str.replace(match.group(0), "").strip()

        remaining_args = [a for a in args_str.split(" ") if a]
        return params, remaining_args

class Context:
    def __init__(self, command: Command, user, platform, channel=None, invocation=None, raw_args=None):
        self.command = command
        self.user = user
        self.platform = platform
        self.channel = channel
        self.invocation = invocation or command.name

        # Phase 3: Parsing
        self.params, self.args = Parser.parse_params(command.params_def, raw_args or [])

    async def reply(self, message: str):
        if self.channel:
            await self.channel.send(message)
        else:
            await self.platform.pm(message, self.user)
