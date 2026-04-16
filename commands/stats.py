"""
Команда .stats — статистика бота
"""
async def execute(event, args, client, db):
    db.c.execute("SELECT SUM(count) FROM cmd_stats")
    total = db.c.fetchone()[0] or 0
    return f"📊 **Статистика**\n🔥 Команд использовано: {total}\n📦 Команд доступно: 2000+\n🍵 TeaDevs"
