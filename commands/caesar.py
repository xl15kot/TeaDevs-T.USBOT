"""
Команда .caesar — шифр Цезаря
"""
async def execute(event, args, client, db):
    if len(args) < 2:
        return "❌ .caesar <сдвиг> <текст>"
    try:
        shift = int(args[0])
        text = " ".join(args[1:])
        result = "".join(chr((ord(c)-97+shift)%26+97) if c.islower() else chr((ord(c)-65+shift)%26+65) if c.isupper() else c for c in text)
        return f"🔐 Цезарь ({shift}): `{result}`"
    except:
        return "❌ .caesar <сдвиг> <текст>"
