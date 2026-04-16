"""
Команда .color — случайный цвет
"""
import random
async def execute(event, args, client, db):
    hx = f"#{random.randint(0,0xFFFFFF):06x}"
    return f"🎨 HEX: `{hx}`"
