"""
Команда .length — длина текста
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .length <текст>"
    return f"📏 {len(' '.join(args))} символов"
