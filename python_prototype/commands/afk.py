from core import core

async def afk_code(context, *args):
    user = context.user
    message = " ".join(args) or "AFK"

    await user.set_data_property("afk_status", True)
    await user.set_data_property("afk_message", message)

    reply = f"Aproveite seu descanso, {user.name}! Status: {message}"
    return {"success": True, "reply": reply}

afk_definition = {
    "Name": "afk",
    "Description": "Fica AFK.",
    "Cooldown": 5000,
    "Params": [],
    "Code": afk_code
}
