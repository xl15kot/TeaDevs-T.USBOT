"""
Команда .iq — измерить IQ
"""
import random
async def execute(event, args, client, db):
    if not args:
        return "❌ .iq @user"
    iq = random.randint(40, 200)
    lvl = "Гений" if iq > 140 else "Умный" if iq > 110 else "Средний" if iq > 85 else "Ниже среднего"
    return f"🧠 IQ {args[0]}: **{iq}**\nУровень: {lvl}"
