"""
Команда .ban — бан (симуляция)
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .ban @user"
    return f"🔨 {args[0]} забанен (симуляция)"
