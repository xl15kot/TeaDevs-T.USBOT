"""
Команда .howgay — измерить гейскость
"""
import random
async def execute(event, args, client, db):
    if not args:
        return "❌ .howgay @user"
    return f"🌈 {args[0]} гей на {random.randint(0,100)}%"
