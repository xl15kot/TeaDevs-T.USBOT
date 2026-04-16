"""
Команда .guess — угадай число
"""
import random
guess_numbers = {}
async def execute(event, args, client, db):
    uid = event.sender_id
    if not args:
        guess_numbers[uid] = random.randint(1, 100)
        return "🎯 Загадал число от 1 до 100\n.guess <число>"
    if args[0].isdigit():
        if uid not in guess_numbers:
            return "❌ Начните: .guess"
        g = int(args[0])
        n = guess_numbers[uid]
        if g < n:
            return "📈 Больше!"
        elif g > n:
            return "📉 Меньше!"
        else:
            del guess_numbers[uid]
            return f"🎉 Правильно! Число было {n}"
    return "❌ Введите число"
