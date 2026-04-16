"""
Команда .donetodo — выполнить задачу
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .donetodo <номер>"
    try:
        tid = int(args[0])
        db.c.execute("UPDATE todos SET done=1 WHERE id=? AND user_id=?", (tid, event.sender_id))
        db.conn.commit()
        return f"✅ Задача #{tid} выполнена!"
    except:
        return "❌ .donetodo <номер>"
