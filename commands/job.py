"""
Команда .job — работа
"""
async def execute(event, args, client, db):
    jobs = ["💻 Программист (200-500)", "👨‍🍳 Повар (100-250)", "👮 Полицейский (150-350)", "👨‍⚕️ Врач (300-600)"]
    if args:
        job_name = " ".join(args)
        db.c.execute("UPDATE economy SET job=? WHERE user_id=?", (job_name, event.sender_id))
        db.conn.commit()
        return f"💼 Профессия изменена на: {job_name}"
    else:
        return "💼 **Доступные профессии:**\n" + "\n".join(jobs)
