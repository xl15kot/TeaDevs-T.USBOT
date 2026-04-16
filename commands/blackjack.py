"""
Команда .blackjack — блэкджек
"""
import random
async def execute(event, args, client, db):
    balance = db.get_balance(event.sender_id)
    if balance[0] < 100:
        return f"❌ Нужно 100 монет, у вас {balance[0]}"
    db.add_balance(event.sender_id, -100)
    player = random.randint(15, 21)
    dealer = random.randint(15, 21)
    if player > dealer or dealer > 21:
        db.add_balance(event.sender_id, 200)
        return f"🃏 Вы: {player} | Дилер: {dealer}\n🎉 Победа! +200 монет"
    elif player < dealer:
        return f"🃏 Вы: {player} | Дилер: {dealer}\n💀 Проигрыш -100 монет"
    else:
        db.add_balance(event.sender_id, 100)
        return f"🃏 Вы: {player} | Дилер: {dealer}\n🤝 Ничья! Ставка возвращена"
