"""
Команда .upper — верхний регистр
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .upper <текст>"
    return " ".join(args).upper()
