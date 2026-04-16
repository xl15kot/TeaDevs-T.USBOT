"""
Команда .notes — список заметок
"""
async def execute(event, args, client, db):
    db.c.execute("SELECT title, created FROM notes WHERE user_id=? ORDER BY created DESC LIMIT 10", (event.sender_id,))
    notes = db.c.fetchall()
    if not notes:
        return "📭 У вас нет заметок"
    text = "📝 **Ваши заметки:**\n"
    for t, c in notes:
        text += f"• {t}\n"
    return text
