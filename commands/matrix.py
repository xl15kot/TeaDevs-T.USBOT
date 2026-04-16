import asyncio

"""
Команда .matrix — эффект матрицы
"""
async def execute(event, args, client, db):
    frames = [
        "`01001000 01100101`",
        "`01001000 01100101 01101100`",
        "`01001000 01100101 01101100 01101100`",
        "`01001000 01100101 01101100 01101100 01101111`\n\n🤖 Hello World!"
    ]
    msg = await event.edit("💊 THE MATRIX")
    for f in frames:
        await asyncio.sleep(0.6)
        await msg.edit(f"💊 THE MATRIX\n{f}")
    return None
