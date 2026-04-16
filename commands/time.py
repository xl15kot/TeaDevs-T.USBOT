"""
Команда .time — текущее время
"""
import time
async def execute(event, args, client, db):
    return f"🕐 {time.strftime('%H:%M:%S')}"
