"""
Команда .kiss — поцеловать
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .kiss @user"
    return f"😘 {args[0]}, ты получил поцелуй!"
