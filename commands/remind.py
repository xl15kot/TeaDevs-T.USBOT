import asyncio

"""
Команда .remind — напоминание
"""
async def execute(event, args, client, db):
    if len(args) < 2:
        return "❌ .remind <секунды> <текст>"
    try:
        secs = int(args[0])
        text = " ".join(args[1:])
        await event.edit(f"⏰ Напоминание через {secs}с: {text}")
        async def remind():
            await asyncio.sleep(secs)
            await event.respond(f"🔔 **НАПОМИНАНИЕ!**\n\n{text}")
        asyncio.create_task(remind())
        return None
    except:
        return "❌ .remind <секунды> <текст>"
