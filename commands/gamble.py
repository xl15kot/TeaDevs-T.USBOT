"""
Команда .gamble — ставка
"""
import random
async def execute(event, args, client, db):
    if not args:
        return "❌ .gamble <сумма>"
    try:
        bet = int(args[0])
        balance = db.get_balance(event.sender_id)
        if balance[0] < bet:
            return f"❌ Не хватает монет! У вас {balance[0]}"
        elif random.random() < 0.45:
            db.add_balance(event.sender_id, bet)
            return f"🎉 ВЫ ВЫИГРАЛИ! +{bet} монет!"
        else:
            db.add_balance(event.sender_id, -bet)
            return f"💸 Вы проиграли -{bet} монет"
    except:
        return "❌ .gamble <сумма>"
