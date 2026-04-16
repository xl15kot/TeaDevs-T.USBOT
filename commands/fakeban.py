"""
Команда .fakeban — фейковый бан
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .fakeban @user"
    await event.delete()
    msg = await event.respond(f"🔨 {args[0]} ЗАБАНЕН!")
    await asyncio.sleep(3)
    await msg.edit(f"😂 Шутка! {args[0]} не забанен")
    return None
