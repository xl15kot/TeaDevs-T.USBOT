"""
Команда .flip — перевёрнутый текст
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .flip <текст>"
    fm = str.maketrans("abcdefghijklmnopqrstuvwxyz", "ɐqɔpǝɟɓɥıɾʞʍɯuodbɹsʇnʌʍxʎz")
    return " ".join(args).translate(fm)[::-1]
