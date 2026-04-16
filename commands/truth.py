"""
Команда .truth — правда
"""
import random
async def execute(event, args, client, db):
    truths = [
        "Какой твой самый неловкий момент?",
        "Врал ли ты когда-нибудь учителю?",
        "Кто тебе нравится?",
        "Твой худший поступок в жизни?"
    ]
    return f"🔮 **ПРАВДА:**\n_{random.choice(truths)}_"
