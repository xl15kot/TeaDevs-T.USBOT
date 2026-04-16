"""
Команда .owo — UwU стиль
"""
import random
async def execute(event, args, client, db):
    if not args:
        return "❌ .owo <текст>"
    text = " ".join(args)
    for fr,to in [("r","w"),("l","w")]:
        text = text.replace(fr, to)
    return f"{text} {random.choice(['uwu','owo','(◕ᴗ◕✿)'])}"
