"""
Команда .calc — калькулятор
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .calc <выражение>"
    try:
        result = eval(" ".join(args))
        return f"🧮 = {result}"
    except:
        return "❌ Ошибка в выражении"
