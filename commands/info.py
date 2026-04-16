"""
Команда .info — информация о пользователе
"""
async def execute(event, args, client, db):
    if args:
        try:
            u = await client.get_entity(args[0])
            return f"👤 **{u.first_name}**\n🆔 ID: `{u.id}`\n📝 @{u.username or 'нет'}"
        except:
            return "❌ Пользователь не найден"
    else:
        me = await client.get_me()
        return f"👤 **{me.first_name}**\n🆔 ID: `{me.id}`\n📝 @{me.username or 'нет'}"
