import asyncio

"""
Команда .timer — таймер
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .timer <секунды>"
    try:
        secs = int(args[0])
        msg = await event.edit(f"⏰ Таймер: {secs}с")
        for i in range(secs-1, 0, -1):
            await asyncio.sleep(1)
            if i <= 5 or i % 10 == 0:
                await msg.edit(f"⏰ Таймер: {i}с")
        await msg.edit("🔔 **ВРЕМЯ ВЫШЛО!**")
        return None
    except:
        return "❌ .timer <секунды>"
