"""
Команда .duel — дуэль
"""
import random
async def execute(event, args, client, db):
    if not args:
        return "❌ .duel @user"
    res = random.choice(["🏆 и победил!", "💀 и проиграл!", "🤝 Ничья!"])
    return f"⚔️ Вызвал на дуэль {args[0]} {res}"
