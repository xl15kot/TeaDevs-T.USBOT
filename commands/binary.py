"""
Команда .binary — текст в бинарный код
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .binary <текст>"
    text = " ".join(args)
    return f"💾 `{'  '.join(f'{ord(c):08b}' for c in text)}`"
