"""
Команда .roast — подколоть
"""
import random
async def execute(event, args, client, db):
    if not args:
        return "❌ .roast @user"
    roasts = [
        "{} — ты как обновление Windows: все ждут, но никто не рад.",
        "{} — твой IQ меньше температуры в комнате.",
        "{} — даже Google не знает ответа на вопрос, зачем ты существуешь."
    ]
    return f"🔥 {random.choice(roasts).format(args[0])}"
