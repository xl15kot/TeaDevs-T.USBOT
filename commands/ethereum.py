"""
Команда .ethereum — курс Ethereum
"""
import random
async def execute(event, args, client, db):
    return f"⟠ ETH: ${random.randint(2500,4500):,}"
