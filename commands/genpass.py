"""
Команда .genpass — генератор паролей
"""
import random
import string
async def execute(event, args, client, db):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    pw = "".join(random.choice(chars) for _ in range(20))
    return f"🔑 `{pw}`"
