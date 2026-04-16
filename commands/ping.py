"""
Команда .ping — проверка задержки
"""
import time
async def execute(event, args, client, db):
    start = time.time()
    await event.edit("🏓")
    await asyncio.sleep(0.3)
    return f"🏓 {round((time.time()-start)*1000)}ms"
