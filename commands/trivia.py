"""
Команда .trivia — викторина
"""
import random
quiz_question = None
async def execute(event, args, client, db):
    global quiz_question
    if not args:
        questions = [
            {"q": "Столица Франции?", "a": "париж"},
            {"q": "2+2*2?", "a": "6"},
            {"q": "Python это змея или язык?", "a": "язык"}
        ]
        q = random.choice(questions)
        quiz_question = q
        return f"❓ **ВИКТОРИНА**\n\n{q['q']}\n\n.answer <ответ>"
    if args[0].lower() == "answer" and len(args) > 1:
        if not quiz_question:
            return "❌ Нет активного вопроса. .trivia"
        ans = " ".join(args[1:]).lower()
        if ans == quiz_question["a"]:
            db.add_balance(event.sender_id, 10)
            quiz_question = None
            return f"✅ **Правильно!** +10 монет 🎉"
        else:
            correct = quiz_question["a"]
            quiz_question = None
            return f"❌ Неверно. Правильный ответ: **{correct}**"
    return "❌ .trivia | .answer <ответ>"
