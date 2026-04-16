"""
Команда .kick — кик (симуляция)
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .kick @user"
    return f"👢 {args[0]} кикнут (симуляция)"
