"""
Команда .lower — нижний регистр
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .lower <текст>"
    return " ".join(args).lower()
