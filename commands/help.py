"""
Команда .help — список команд
"""
import os
async def execute(event, args, client, db):
    cmd_list = []
    if os.path.exists("commands"):
        for f in os.listdir("commands"):
            if f.endswith(".py") and f != "__init__.py":
                cmd_list.append(f[:-3])
    if os.path.exists("user_commands"):
        for f in os.listdir("user_commands"):
            if f.endswith(".py"):
                cmd_list.append(f"[USER] {f[:-3]}")
    cmds = "\n".join([f".{c}" for c in sorted(cmd_list)[:50]])
    return f"""📖 **T.UserBot Reborn | Доступные команды**

{cmds}

━━━━━━━━━━━━━━━━━━━━━━
📦 Всего команд: {len(cmd_list)}
🍵 TeaDevs — code with tea
━━━━━━━━━━━━━━━━━━━━━━
💡 Свои команды добавляй в папку user_commands/"""
