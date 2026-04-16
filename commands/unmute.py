"""
Команда .unmute — размут (симуляция)
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .unmute @user"
    return f"🔊 {args[0]} размучен (симуляция)"
