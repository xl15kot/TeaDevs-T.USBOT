"""
Команда .hug — обнять
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .hug @user"
    return f"🤗 {args[0]}, ты получил обнимашки!"
