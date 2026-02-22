from datetime import datetime
import psutil

async def ping_code(context, *args):
    # Simulação de uptime e memória
    uptime = datetime.now() # Simplificado
    memory = psutil.virtual_memory().percent

    reply = f"Pong! 🏓 Memória usada: {memory}%"
    return {"success": True, "reply": reply}

ping_definition = {
    "Name": "ping",
    "Description": "Ping!",
    "Cooldown": 5000,
    "Code": ping_code
}
