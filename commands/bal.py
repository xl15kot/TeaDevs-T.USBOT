"""
Команда .bal — баланс
"""
async def execute(event, args, client, db):
    balance = db.get_balance(event.sender_id)
    return f"💰 **Кошелёк:** {balance[0]} монет\n🏦 **Банк:** {balance[1]} монет\n💼 **Работа:** {balance[2]}\n⭐ **Уровень {balance[4]}**"
