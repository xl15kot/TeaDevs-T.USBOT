"""
Команда .deln — удалить заметку
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .deln <название>"
    db.c.execute("DELETE FROM notes WHERE user_id=? AND title=?", (event.sender_id, args[0]))
    db.conn.commit()
    return f"🗑 Заметка '{args[0]}' удалена"
