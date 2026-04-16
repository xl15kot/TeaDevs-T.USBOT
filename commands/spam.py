import asyncio
async def execute(event, args, client, db):
    if len(args) < 2:
        return "❌ .spam <кол-во> <текст>"
    try:
        n = min(int(args[0]), 50)
        text = " ".join(args[1:])
        await event.delete()
        for i in range(n):
            await event.respond(f"{text}")
            await asyncio.sleep(0.35)
        return None
    except:
        return "❌ .spam <кол-во> <текст>"
