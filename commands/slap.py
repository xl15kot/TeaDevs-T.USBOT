"""
Команда .slap — дать пощёчину
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .slap @user"
    return f"👋 {args[0]}, ты получил пощёчину!"
