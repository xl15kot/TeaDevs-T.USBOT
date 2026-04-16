"""
Команда .propose — предложение
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .propose @user"
    return f"💍 {args[0]}, выйди за меня! 💍"
