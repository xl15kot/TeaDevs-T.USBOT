"""
Команда .currency — курс валют
"""
async def execute(event, args, client, db):
    if len(args) < 3:
        return "❌ .currency <сумма> <из> <в>"
    try:
        amt = float(args[0])
        rates = {("USD","RUB"): 92, ("RUB","USD"): 0.0109, ("EUR","RUB"): 99.5}
        fr, to = args[1].upper(), args[2].upper()
        key = (fr, to)
        if key in rates:
            return f"💱 {amt} {fr} = {amt*rates[key]:.2f} {to}"
        else:
            return "❌ Неизвестная пара. Поддержка: USD/RUB/EUR"
    except:
        return "❌ .currency <сумма> <из> <в>"
