"""
Команда .neofetch — красивый вывод информации
"""
import platform
async def execute(event, args, client, db):
    return f"""```\n        .=+*##*+=.          tguser@userbot\n      -#@@@@@@@@@@#-        OS: {platform.system()}\n     *@@@@@@@@@@@@@@*       Bot: T.UserBot\n    #@@@@@@@@@@@@@@@@#      Python: {platform.python_version()}\n   #@@@@@#=--=#@@@@@@@#     Prefix: .\n  #@@@@@*       *@@@@@@#    Lib: Telethon\n  @@@@@@-       -@@@@@@@@   Cmds: 2000+\n  @@@@@@-       -@@@@@@@@   \n  #@@@@@*       *@@@@@@#    🍵 TeaDevs\n   #@@@@@#=--=#@@@@@@@#     \n    #@@@@@@@@@@@@@@@@#      \n     *@@@@@@@@@@@@@@*\n      -#@@@@@@@@@@#-\n        .=+*##*+=.\n```"""
