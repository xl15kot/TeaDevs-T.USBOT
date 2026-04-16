"""
Команда .rps — камень-ножницы-бумага
"""
import random
async def execute(event, args, client, db):
    if not args:
        return "❌ .rps камень/ножницы/бумага"
    choices = {"камень": "🪨", "ножницы": "✂️", "бумага": "📄"}
    user = args[0].lower()
    if user not in choices:
        return "❌ камень/ножницы/бумага"
    bot = random.choice(list(choices.keys()))
    wins = {("камень","ножницы"), ("ножницы","бумага"), ("бумага","камень")}
    if user == bot:
        res = "🤝 Ничья!"
    elif (user, bot) in wins:
        res = "🎉 Вы победили!"
    else:
        res = "💀 Вы проиграли!"
    return f"{choices[user]} vs {choices[bot]}\n{res}"
