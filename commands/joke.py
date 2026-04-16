"""
Команда .joke — случайная шутка
"""
import random
async def execute(event, args, client, db):
    jokes = [
        "Почему программисты не любят природу? Много багов! 🐛",
        "Git push — и молись. 🙏",
        "Что говорит один бит другому? — Дай байт! 💾",
        "Есть 10 типов людей: те, кто понимает бинарный код, и те, кто нет.",
        "try { любовь } catch(Exception e) { сон }"
    ]
    return f"😂 {random.choice(jokes)}"
