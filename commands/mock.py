"""
Команда .mock — SpOnGeBoB стиль
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .mock <текст>"
    text = " ".join(args)
    return "".join(c.upper() if i%2==0 else c.lower() for i,c in enumerate(text))
