"""
Команда .mute — мут (симуляция)
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .mute @user"
    return f"🔇 {args[0]} замучен (симуляция)"
