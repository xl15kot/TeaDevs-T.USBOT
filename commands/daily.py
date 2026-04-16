"""
Команда .daily — ежедневный бонус
"""
import time
import random
async def execute(event, args, client, db):
    balance = db.get_balance(event.sender_id)
    now = time.time()
    if balance[6] and now - float(balance[6]) < 86400:
        return "⏰ Дейли уже получен. Приходи завтра!"
    bonus = random.randint(200, 800)
    db.add_balance(event.sender_id, bonus)
    db.c.execute("UPDATE economy SET last_daily=? WHERE user_id=?", (now, event.sender_id))
    db.conn.commit()
    return f"🎁 Дейли: +{bonus} монет!"
