"""
Команда .date — текущая дата
"""
import time
async def execute(event, args, client, db):
    return f"📅 {time.strftime('%d.%m.%Y')}"
