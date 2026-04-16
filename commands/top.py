"""
Команда .top — топ богачей
"""
async def execute(event, args, client, db):
    db.c.execute("SELECT user_id, balance+bank as total FROM economy ORDER BY total DESC LIMIT 10")
    rows = db.c.fetchall()
    if not rows:
        return "📊 Нет данных"
    medals = ["🥇", "🥈", "🥉"] + [f"{i}️⃣" for i in range(4, 11)]
    text = "🏆 **ТОП БОГАЧЕЙ**\n" + "─"*15 + "\n"
    for i, (uid, total) in enumerate(rows):
        text += f"{medals[i]} ID {uid}: **{total}** монет\n"
    return text
