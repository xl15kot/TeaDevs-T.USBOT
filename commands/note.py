"""
Команда .note — создать заметку
"""
import time
async def execute(event, args, client, db):
    if len(args) < 2:
        return "❌ .note <название> <текст>"
    title = args[0]
    content = " ".join(args[1:])
    db.c.execute("INSERT INTO notes (user_id, title, content, created) VALUES (?,?,?,?)",
                (event.sender_id, title, content, time.time()))
    db.conn.commit()
    return f"✅ Заметка '{title}' сохранена!"
