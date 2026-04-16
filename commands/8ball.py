"""
Команда .8ball — магический шар
"""
import random
async def execute(event, args, client, db):
    if not args:
        return "❌ .8ball <вопрос>"
    answers = ["✅ Определённо да", "❌ Нет, никогда", "🤔 Возможно", "🌟 Конечно!", "🚫 Нет шансов", "💫 Скорее всего да"]
    return f"🎱 **{' '.join(args)}**\n\n{random.choice(answers)}"
