"""
Команда .slots — слоты
"""
import random
async def execute(event, args, client, db):
    balance = db.get_balance(event.sender_id)
    if balance[0] < 50:
        return f"❌ Нужно 50 монет, у вас {balance[0]}"
    db.add_balance(event.sender_id, -50)
    symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "💎"]
    reels = [random.choice(symbols) for _ in range(3)]
    if reels[0] == reels[1] == reels[2]:
        prizes = {"💎": 5000, "⭐": 1000, "🍒": 500}
        prize = prizes.get(reels[0], 300)
        db.add_balance(event.sender_id, prize)
        return f"🎰 [{reels[0]} {reels[1]} {reels[2]}]\n🎉 ДЖЕКПОТ! +{prize} монет!"
    elif reels[0] == reels[1] or reels[1] == reels[2]:
        db.add_balance(event.sender_id, 75)
        return f"🎰 [{reels[0]} {reels[1]} {reels[2]}]\n✨ Почти! +75 монет"
    else:
        return f"🎰 [{reels[0]} {reels[1]} {reels[2]}]\n😢 Проигрыш -50 монет"
