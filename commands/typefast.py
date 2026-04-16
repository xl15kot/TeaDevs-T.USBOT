import asyncio

"""
Команда .typefast — быстрая анимация печати
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .typefast <текст>"
    text = " ".join(args)
    msg = await event.edit("▒")
    typed = ""
    for ch in text:
        typed += ch
        await msg.edit(typed + "▒")
        await asyncio.sleep(0.025)
    await msg.edit(typed)
    return None
