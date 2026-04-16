"""
Команда .give — передать монеты
"""
async def execute(event, args, client, db):
    if len(args) < 2:
        return "❌ .give @user <сумма>"
    try:
        amt = int(args[1])
        balance = db.get_balance(event.sender_id)
        if balance[0] < amt:
            return "❌ Недостаточно монет"
        db.add_balance(event.sender_id, -amt)
        return f"✅ Отдали {args[0]} {amt} монет"
    except:
        return "❌ .give @user <сумма>"
