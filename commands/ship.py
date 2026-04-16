"""
Команда .ship — совместимость
"""
import random
async def execute(event, args, client, db):
    if len(args) < 2:
        return "❌ .ship @user1 @user2"
    return f"💕 {args[0]} + {args[1]} = {random.randint(0,100)}%"
