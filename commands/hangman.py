"""
Команда .hangman — виселица
"""
import random
hangman_games = {}
def hangman_pic(wrong):
    stages = [
        "  ___
 |   |
 |
 |
 |
_|_",
        "  ___
 |   |
 |   😐
 |
 |
_|_",
        "  ___
 |   |
 |   😐
 |   |
 |
_|_",
        "  ___
 |   |
 |   😐
 |  /|
 |
_|_",
        "  ___
 |   |
 |   😐
 |  /|\
 |
_|_",
        "  ___
 |   |
 |   😐
 |  /|\
 |  /
_|_",
        "  ___
 |   |
 |   😵
 |  /|\
 |  / \
_|_"
    ]
    return stages[min(wrong, 6)]
async def execute(event, args, client, db):
    uid = event.sender_id
    words = ["python", "telegram", "userbot", "программа", "компьютер"]
    if not args:
        word = random.choice(words)
        hangman_games[uid] = {"word": word, "guessed": set(), "wrong": 0}
        disp = " ".join("_" for _ in word)
        return f"🪢 **ВИСЕЛИЦА**\n```\n{hangman_pic(0)}\n```\nСлово: `{disp}`\n.hg <буква>"
    cmd = args[0].lower()
    if cmd == "hg" and len(args) > 1:
        if uid not in hangman_games:
            return "❌ .hangman — начать"
        g = hangman_games[uid]
        let = args[1].lower()
        if let in g["guessed"]:
            return f"⚠️ Буква '{let}' уже угадана"
        g["guessed"].add(let)
        if let in g["word"]:
            disp = " ".join(ch if ch in g["guessed"] else "_" for ch in g["word"])
            if "_" not in disp:
                del hangman_games[uid]
                return f"🎉 **ПОБЕДА!**\nСлово: {g['word']}"
            return f"✅ Есть буква '{let}'!\n```\n{hangman_pic(g['wrong'])}\n```\n`{disp}`"
        else:
            g["wrong"] += 1
            disp = " ".join(ch if ch in g["guessed"] else "_" for ch in g["word"])
            if g["wrong"] >= 6:
                word = g["word"]
                del hangman_games[uid]
                return f"💀 **ПРОИГРЫШ**\n```\n{hangman_pic(6)}\n```\nСлово: {word}"
            return f"❌ Нет '{let}' (попыток: {6-g['wrong']})\n```\n{hangman_pic(g['wrong'])}\n```\n`{disp}`"
    elif cmd == "word" and len(args) > 1:
        if uid not in hangman_games:
            return "❌ .hangman — начать"
        g = hangman_games[uid]
        if args[1].lower() == g["word"]:
            del hangman_games[uid]
            return f"🎉 **ПОБЕДА!**\nСлово: {g['word']}"
        else:
            g["wrong"] = min(g["wrong"]+2, 6)
            if g["wrong"] >= 6:
                word = g["word"]
                del hangman_games[uid]
                return f"💀 **ПРОИГРЫШ**\nСлово: {word}"
            return f"❌ Неверно! Попыток: {6-g['wrong']}"
    return "❌ .hangman | .hg <буква> | .word <слово>"
