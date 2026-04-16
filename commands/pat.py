"""
Команда .pat — погладить
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .pat @user"
    return f"🖐 {args[0]}, тебя погладили по голове!"
