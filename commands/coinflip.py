"""
Команда .coinflip — монетка
"""
import random
async def execute(event, args, client, db):
    return f"🪙 {random.choice(['Орёл 🦅', 'Решка 💰'])}"
