"""
Команда .del — удалить сообщение
"""
async def execute(event, args, client, db):
    if event.is_reply:
        r = await event.get_reply_message()
        await r.delete()
    await event.delete()
    return None
