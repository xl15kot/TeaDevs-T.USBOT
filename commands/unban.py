"""
Команда .unban — разбан (симуляция)
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .unban @user"
    return f"🔓 {args[0]} разбанен (симуляция)"
