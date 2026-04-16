"""
Команда .purge — очистка (симуляция)
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .purge <количество>"
    try:
        n = min(int(args[0]), 50)
        await event.delete()
        tmp = await event.respond(f"✅ Удалено {n} сообщений (симуляция)")
        await asyncio.sleep(3)
        await tmp.delete()
        return None
    except:
        return "❌ .purge <количество>"
