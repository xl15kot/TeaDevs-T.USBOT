"""
Команда .todos — список задач
"""
async def execute(event, args, client, db):
    db.c.execute("SELECT id, task, done FROM todos WHERE user_id=? ORDER BY done, id", (event.sender_id,))
    todos = db.c.fetchall()
    if not todos:
        return "📭 У вас нет задач"
    text = "📋 **Список задач:**\n"
    for tid, task, done in todos:
        status = "✅" if done else "⬜"
        text += f"{status} #{tid}: {task}\n"
    return text
