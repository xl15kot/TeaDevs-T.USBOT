"""
Команда .compliment — комплимент
"""
import random
async def execute(event, args, client, db):
    if not args:
        return "❌ .compliment @user"
    compliments = [
        "{} — ты как Wi-Fi: соединяешь сердца! 💕",
        "{} — твоя улыбка лучшее, что есть в этом мире! 😊",
        "{} — ты как хороший код: красивый и эффективный! 💻"
    ]
    return f"💝 {random.choice(compliments).format(args[0])}"
