import sys

async def execute(event, args, client, db):
    await event.edit("🛑 Выключение...")
    sys.exit(0)