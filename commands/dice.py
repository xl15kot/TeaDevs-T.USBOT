"""
Команда .dice — бросить кубик
"""
import random
async def execute(event, args, client, db):
    sides = int(args[0]) if args and args[0].isdigit() else 6
    sides = max(2, min(sides, 100))
    return f"🎲 d{sides}: **{random.randint(1, sides)}**"
