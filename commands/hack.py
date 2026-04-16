import asyncio

"""
Команда .hack — шуточный взлом
"""
import random
async def execute(event, args, client, db):
    msg = await event.edit("🔐 Взлом Пентагона... 0%")
    for i in range(0, 101, random.randint(5, 15)):
        bar = "█" * (i//5) + "░" * (20 - i//5)
        await msg.edit(f"🔐 Взлом Пентагона...\n[{bar}] {i}%")
        await asyncio.sleep(0.1)
    await msg.edit("🟢 **ПЕНТАГОН ВЗЛОМАН!**\n📁 Найдены мемы и рецепт пиццы\n😂 Шутка")
    return None
