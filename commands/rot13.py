"""
Команда .rot13 — шифр ROT13
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .rot13 <текст>"
    text = " ".join(args)
    result = "".join(chr((ord(c)-97+13)%26+97) if c.islower() else chr((ord(c)-65+13)%26+65) if c.isupper() else c for c in text)
    return f"🔐 ROT13: `{result}`"
