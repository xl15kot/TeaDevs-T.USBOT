"""
Команда .deposit — положить в банк
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .deposit <сумма>"
    try:
        amt = int(args[0])
        balance = db.get_balance(event.sender_id)
        if balance[0] < amt:
            return f"❌ Недостаточно монет (у вас: {balance[0]})"
        db.add_balance(event.sender_id, -amt)
        db.add_bank(event.sender_id, amt)
        return f"🏦 Положено в банк: {amt} монет"
    except:
        return "❌ .deposit <сумма>"
