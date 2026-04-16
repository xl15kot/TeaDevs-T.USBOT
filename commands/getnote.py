"""
Команда .getnote — показать заметку
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .getnote <название>"
    db.c.execute("SELECT content FROM notes WHERE user_id=? AND title=?", (event.sender_id, args[0]))
    note = db.c.fetchone()
    if note:
        return f"📄 **{args[0]}**\n\n{note[0]}"
    else:
        return "❌ Заметка не найдена"
