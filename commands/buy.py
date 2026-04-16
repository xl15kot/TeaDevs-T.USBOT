"""
Команда .buy — купить предмет
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .buy <предмет>"
    items = {"пицца": 100, "бургер": 50, "кофе": 30, "алмаз": 10000, "меч": 500}
    item = args[0].lower()
    if item not in items:
        return "❌ Товар не найден"
    price = items[item]
    balance = db.get_balance(event.sender_id)
    if balance[0] < price:
        return f"❌ Нужно {price}, у вас {balance[0]}"
    db.add_balance(event.sender_id, -price)
    return f"✅ Куплено: {item} за {price} монет"
