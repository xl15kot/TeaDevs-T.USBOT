"""
Команда .fact — интересный факт
"""
import random
async def execute(event, args, client, db):
    facts = [
        "Осьминог имеет 3 сердца! 🐙",
        "Слоны не умеют прыгать 🐘",
        "Бананы — это ягоды 🍌",
        "Мёд никогда не портится 🍯",
        "Кошки проводят 70% жизни во сне 😴"
    ]
    return f"📚 {random.choice(facts)}"
