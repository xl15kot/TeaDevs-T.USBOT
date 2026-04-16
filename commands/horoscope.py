"""
Команда .horoscope — гороскоп
"""
import random
async def execute(event, args, client, db):
    if not args:
        return "❌ .horoscope <знак>"
    preds = ["День будет удачным! 🌟", "Ожидайте сюрпризов 🎁", "Время новых начинаний 🚀", "Будьте осторожны в финансах 💰"]
    return f"🔮 Гороскоп для {args[0]}:\n{random.choice(preds)}"
