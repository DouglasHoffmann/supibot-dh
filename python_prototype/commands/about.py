async def about_code(context, *args):
    reply = (
        "Eu sou um robô de utilidade e variedade, migrando para Python! 🐍\n"
        "Originalmente desenvolvido em Node.js desde 2018."
    )
    return {"success": True, "reply": reply}

about_definition = {
    "Name": "about",
    "Description": "Sobre o bot.",
    "Cooldown": 30000,
    "Code": about_code
}
