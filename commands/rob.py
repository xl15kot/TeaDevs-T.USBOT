"""
Команда .rob — ограбить
"""
import random
async def execute(event, args, client, db):
    if not args:
        return "❌ .rob @user"
    if random.random() < 0.35:
        amt = random.randint(10, 200)
        db.add_balance(event.sender_id, amt)
        return f"🦹 Ограбили {args[0]}! +{amt} монет"
    else:
        fine = random.randint(50, 300)
        db.add_balance(event.sender_id, -fine)
        return f"🚨 Поймали! Штраф: {fine} монет"
