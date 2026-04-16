"""
Команда .bitcoin — курс Bitcoin
"""
import random
async def execute(event, args, client, db):
    return f"₿ BTC: ${random.randint(55000,75000):,}"
