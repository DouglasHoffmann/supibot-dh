import asyncio
from classes.user import User
from classes.channel import Channel
from classes.command import Command, Context
from classes.platform import Platform
from commands.ping import ping_definition
from commands.about import about_definition
from commands.afk import afk_definition

class MockPlatform(Platform):
    async def connect(self):
        print(f"Plataforma {self.name} conectada.")

    async def send(self, message: str, channel):
        print(f"[{self.name} > #{channel.name}] {message}")

    async def pm(self, message: str, user):
        print(f"[{self.name} > PM @{user.name}] {message}")

async def main():
    # 1. Setup
    platform = MockPlatform("Twitch", {"ID": 1})
    user = await User.get("supinic")
    channel = await Channel.get("supinic", platform)

    # 2. Registrar comandos
    registry = {
        "ping": Command(ping_definition),
        "about": Command(about_definition),
        "afk": Command(afk_definition)
    }

    # 3. Simular execução de comando com argumentos e parâmetros
    test_cases = [
        ("ping", []),
        ("about", []),
        ("afk", ["Indo", "almoçar"])
    ]

    for cmd_name, args in test_cases:
        print(f"\n--- Executando ${cmd_name} {' '.join(args)} ---")
        command = registry.get(cmd_name)
        # Contexto agora faz o parsing (Phase 3)
        ctx = Context(command, user, platform, channel, raw_args=args)

        result = await command.execute(ctx, *ctx.args)
        if result.get("reply"):
            await ctx.reply(result["reply"])

if __name__ == "__main__":
    asyncio.run(main())
