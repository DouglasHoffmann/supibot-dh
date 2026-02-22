from datetime import datetime
import psutil
from core import core

async def ping_code(context, *args):
    # Simulação de uptime e memória usando o core.Utils
    memory = psutil.virtual_memory().percent

    reply = f"Pong! 🏓 Memória usada: {memory}%"
    return {"success": True, "reply": reply}

ping_definition = {
    "Name": "ping",
    "Description": "Ping!",
    "Cooldown": 5000,
    "Params": [],
    "Code": ping_code
}
