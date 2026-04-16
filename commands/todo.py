"""
Команда .todo — добавить задачу
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .todo <текст>"
    task = " ".join(args)
    db.c.execute("INSERT INTO todos (user_id, task) VALUES (?,?)", (event.sender_id, task))
    db.conn.commit()
    tid = db.c.lastrowid
    return f"✅ Задача #{tid} добавлена: {task}"
