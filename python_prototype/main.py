import asyncio
from classes.user import User
from classes.channel import Channel
from classes.command import Command, Context
from classes.platform import Platform
from commands.ping import ping_definition
from commands.about import about_definition

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
    channel = Channel({"ID": 1, "Name": "supinic"}, platform)

    # 2. Registrar comandos
    ping_cmd = Command(ping_definition)
    about_cmd = Command(about_definition)
    registry = {
        "ping": ping_cmd,
        "about": about_cmd
    }

    # 3. Simular execução de comando
    for cmd_name in ["ping", "about"]:
        print(f"\n--- Executando ${cmd_name} ---")
        command = registry.get(cmd_name)
        ctx = Context(command, user, platform, channel)

        result = await command.execute(ctx)
        if result.get("reply"):
            await ctx.reply(result["reply"])

if __name__ == "__main__":
    asyncio.run(main())
