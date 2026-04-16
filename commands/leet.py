"""
Команда .leet — Leet speak
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .leet <текст>"
    lm = {"a":"4","e":"3","i":"1","o":"0","t":"7","s":"5"}
    text = " ".join(args)
    result = "".join(lm.get(c.lower(), c) for c in text)
    return f"🔥 `{result}`"
