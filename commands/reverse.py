"""
Команда .reverse — перевернуть текст
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .reverse <текст>"
    return " ".join(args)[::-1]
