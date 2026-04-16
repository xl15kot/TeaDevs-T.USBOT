"""
Команда .deltodo — удалить задачу
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .deltodo <номер>"
    try:
        tid = int(args[0])
        db.c.execute("DELETE FROM todos WHERE id=? AND user_id=?", (tid, event.sender_id))
        db.conn.commit()
        return f"🗑 Задача #{tid} удалена"
    except:
        return "❌ .deltodo <номер>"
