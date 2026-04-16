"""
Команда .bonk — бонк
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .bonk @user"
    return f"🔨 {args[0]} отправлен в рогалик!"
