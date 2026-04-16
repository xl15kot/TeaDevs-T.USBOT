import asyncio

"""
Команда .countdown — обратный отсчёт
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .countdown <секунды>"
    try:
        secs = int(args[0])
        for i in range(secs, 0, -1):
            await event.edit(f"⏳ {i}")
            await asyncio.sleep(1)
        await event.edit("🚀 **СТАРТ!**")
        return None
    except:
        return "❌ .countdown <секунды>"
