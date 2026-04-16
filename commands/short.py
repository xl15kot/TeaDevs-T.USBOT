"""
Команда .short — сократить ссылку
"""
import requests
async def execute(event, args, client, db):
    if not args:
        return "❌ .short <url>"
    url = args[0]
    api = f"https://tinyurl.com/api-create.php?url={url}"
    response = requests.get(api)
    if response.status_code == 200:
        return f"🔗 Короткая ссылка: {response.text}"
    return "❌ Ошибка сокращения"