"""
Команда .rate — оценка пользователя
"""
import random
async def execute(event, args, client, db):
    if not args:
        return "❌ .rate @user"
    return f"⭐ {args[0]}: {random.randint(0,10)}/10"
